# Managing ongoing background processes in your Mac

**Framework**: AppKit  
**Role**: Article

Configure your app to help people understand when background processes may continue after they close your app.

#### Overview

macOS provides a number of ways for apps and services to perform useful tasks for people, including:

- macOS apps with familiar user interfaces, including windows, a menu bar, and so on.
- macOS apps that provide some of their functionality through long-running background tasks that the main app initiates, such as through helper apps.
- macOS apps that launch background services using agents, XPC services, or exec’ed processes that the main app starts and interacts with through some interprocess communications mechanism.
- Any combination of these.

For apps that provide background processing of any kind, it‘s not always readily visible to a person using the app that there’s activity happing in the background. It’s the responsibility of all apps to terminate any background processing when the app quits, or make it possible for a person to do so.

When an app doesn’t terminate background processes after someone quits, macOS shows a Dock indicator for the app and adds a Dock menu item, as shown below, to stop running the app in the background. Clicking on the menu item terminates the app’s background processes. If someone stops an app’s background activity multiple times, macOS presents an alert that allows people to either continue to allow the app to run in the background in the future, or to prevent its future background activity. The system only shows this alert a limited number of times when a person chooses the “Stop running in background” option.

An application which transitions away from the Foreground type to a UIElement or BackgroundOnly type, using either [`setActivationPolicy(_:)`](./nsapplication/setactivationpolicy%28_%29.md) or [`TransformProcessType(_:_:)`](../applicationservices/api-1462420-transformprocesstype.md), disappears from the Dock and doesn’t show the indicator, but the system still presents a notification.

![An screenshot of the Doc that shows a an popover that tells someone that an app is running in the background.](https://developer.apple.com/tutorials/images/com.apple.appkit/background-app-running-dock@2x.png)

![An screenshot of an alert that asks someone if an app should continue to run in background in the future and that gives instructions on how to manage this capability.](https://developer.apple.com/tutorials/images/com.apple.appkit/background-app-running-alert@2x.png)

When an app runs in the background for the first time, macOS also presents a notification. Clicking on the notification brings the person using the app to Settings > Login Items & Extensions, where they can see and manage each app’s background activity.

![An screenshot of a notification that informs someone that an app they quit has background processes that continue to run.](https://developer.apple.com/tutorials/images/com.apple.appkit/background-app-running-notification@2x.png)

#### Keep people in charge of what’s running

People need to have control over when an app runs and how it utilizes the resources on their Mac: a best practice is to ensure apps running in macOS are visible. This means an app is visible in the Dock, menu bar, Control Center, or listed in the Background Items list in System Settings. Helper apps, services, or other processes that an app starts also need to end when an app quits or need to give people the capability to stop them.

Apps running in macOS have a number of options available to manage their use of background processes, depending on what kinds of background services the app uses. The following scenarios describe how to keep people informed on what an app is doing on their behalf and enable them to control when and for how long these apps and services run.

#### Provide a control to manage long running work after an app quits

In the scenarios where an app has to finish up a long running task (such as cloud syncing operations, or importing or exporting data) after someone quits, having a visible UI element, such as a progress bar indicates to the system that the background processing can continue. Another strategy is to use a [`MenuBarExtra`](../SwiftUI/menubarextra.md) to provide progress updates and include some way to control the action. You can implement this either by a menu bar extra command that returns the app to a visible state — which makes the app reappear in the Dock — or by giving people additional options in menu bar extra such as the ability to suspend or cancel the background activity (for example, through a “Quit” or “Stop XXX activity” command), or both.

#### Manage a persistent app-related background service

If your app needs a persistent background service to support its activities, consider using the [Service Management](../ServiceManagement/ServiceManagement.md) framework to register a launch agent or launch daemon. Registering a service using the [`SMAppService`](../ServiceManagement/smappservice.md) notifies someone about the new background item. Someone can then, if necessary, disable registered services in System Settings.

Test your app when the service is in a disabled state (toggled off) in the System Settings to ensure it works as expected. You can use the `SMAppService`.[`status`](../ServiceManagement/smappservice/status-swift.property.md) property to programmatically examine the current state of the service. If your background service needs configuration — such as a database server — a best practice is to provide a preference pane in System Settings that allows someone to configure the service, as well as to start and stop it. For more information on creating preference panes, see [Preference Panes](../PreferencePanes/PreferencePanes.md).

![An screenshot of System Settings that shows details of apps that start at login or run in the background.](https://developer.apple.com/tutorials/images/com.apple.appkit/background-app-settings@2x.png)

#### Control apps without a user interface (UI)

Some apps don’t have a UI. For example, an app that handles a custom URL scheme in the form of links for a cloud storage service. Such an app may contact a server to determine the content type and then launch a different app to open the provided URL. The system may detect these apps as a background apps. If the app isn’t visible and continues to run, the system presents the background process continuation alert as shown above.

Non-UI apps may use one or the other of these options (doing both also works, but isn’t required) to ensure termination when the app’s main UI quits:

- Set the property [`automaticTerminationSupportEnabled`](../Foundation/processinfo/automaticterminationsupportenabled.md) or [`NSSupportsSuddenTermination`](../BundleResources/information-property-list/nssupportssuddentermination.md) in the app’s Information Property List in Xcode, depending on whether your Non-UI app needs a graceful shutdown (`NSSupportsAutomaticTermination`) or can tolerate a sudden termination with no warning (`NSSupportsSuddenTermination`).
- If it doesn’t show UI (such as a [`MenuBarExtra`](../SwiftUI/menubarextra.md)), the app should quit a few seconds after finishing any work, this allows the app to process any possible queued system events before quitting.

> **Note**: The system doesn’t honor runtime changes to the [`automaticTerminationOptOutCounter`](../Foundation/nsprocessinfo/automaticterminationoptoutcounter.md) property in [`ProcessInfo`](../Foundation/processinfo.md) for this purpose. Use one of the options described above, such as the Information Property List settings instead.

For an example of a GUI-less agent app, see [Updating your app package installer to use the new Service Management API](../ServiceManagement/updating-your-app-package-installer-to-use-the-new-service-management-api.md).

#### Understand how implementation decisions affect processes management

> **Note**: These best practices are not mutually exclusive, and depend on the your app’s specific architecture. You may need to use these in combination to ensure your background processes terminate properly depending on your app’s components and how their specific implementations work.

##### Send quit or terminate events to purely background apps

If your visible application directly launches background / non-visible applications to perform work, you should ensure the applications you launched terminate before your visible applications completes its own exit process. You can ensure this by using one of two methods:

1. By sending your background app a quit [Apple Events](../coreservices/apple_events.md) when or before your GUI app exits, for example:

```swift
    let targetBundleID = "com.example.myBackgroundApp"
    if let targetURL = NSWorkspace.shared.urlForApplication(withBundleIdentifier: targetBundleID) {
        let targetDescriptor = NSAppleEventDescriptor(bundleIdentifier: targetBundleID)
        let quitEvent = NSAppleEventDescriptor(
            eventClass: AEEventClass(kCoreEventClass),
            eventID: AEEventID(kAEQuitApplication),
            targetDescriptor: targetDescriptor,
            returnID: AEReturnID(kAutoGenerateReturnID),
            transactionID: AETransactionID(kAnyTransactionID)
        )
        try? quitEvent.sendEvent(options: .defaultOptions)
    }
```

1. Set the property [`automaticTerminationSupportEnabled`](../Foundation/processinfo/automaticterminationsupportenabled.md) or [`NSSupportsSuddenTermination`](../BundleResources/information-property-list/nssupportssuddentermination.md) in the app’s [`Information Property List`](../BundleResources/information-property-list.md) in Xcode. The choice of which method to use depends on whether your non-UI app needs a graceful shutdown (`NSSupportsAutomaticTermination`) or whether it can tolerate a sudden termination with no warning (`NSSupportsSuddenTermination`).

#### Managing Exec’ed Processes

If your app creates background processes using `system()` , `fork()`, or `posix_spawn()` to start other processes from your app, then ensure that these processes are terminated as your app quits by adopting one of these best practices.

- Consider moving this functionality into an XPC service or an extension inside your app. This allows the system to track this relationship between the app and the service and terminate these processes for you automatically. For more information, see [Creating XPC services](../XPC/creating-xpc-services.md).
- If your app needs to start a long-term process which runs after your app terminates, consider using a launch agent managed with [`SMAppService`](../ServiceManagement/smappservice.md) instead of using `fork()`, `posix_spawn()`, or `system()`, which allows a person to control this in the System Settings app pane.
- If your app needs to share information or processing between a group of apps, look into a per-user XPC service or a launch agent. For more information on launch agents, see [Service Management](../ServiceManagement/ServiceManagement.md).

#### Manage self-backgrounding apps

There are certain types of apps that start as GUI apps, but then remove themselves from the Dock using [`TransformProcessType(_:_:)`](../applicationservices/api-1462420-transformprocesstype.md). Apps which are not present in the Dock, or which transition between being present in the Dock while running and not-present in the Dock while remaining running have a different status, depending on how they present themselves after launch:

- For an app which is present in the Dock that launches a secondary (launched) app, the system allows the launched app to run without posting a notification as long as the app which launched them is still present in the Dock (excluding system-launching apps like Finder).
- The background termination rules don’t apply to apps which have a visible presence on screen, such as an icon in the upper right part of the menu bar, or a visible window.
- Apps which are running, and which are not present in the Dock, alert people after a short period of time. The System Settings app pane allows someone to disable the ability of these apps to continue to run without appearing in the Dock. If a person chooses to disable the ability of such an app to execute in the background, the system terminates that app when it determines that it is running without a visible menu bar icon or window.

Developers need to update their apps to ensure that they always have a presence or update their documentation to clarify what functionality someone would lose by disabling background activity for the app.

For additional information on background task management, see [Background task management declarative configuration for Apple devices]([`TransformProcessType(_:_:)`](../applicationservices/api-1462420-transformprocesstype.md). )

## See Also

### Life Cycle
- [class NSApplication](./nsapplication.md)
  An object that manages an app’s main event loop and resources used by all of that app’s objects.
- [class NSRunningApplication](./nsrunningapplication.md)
  An object that can manipulate and provide information for a single instance of an app.
- [protocol NSApplicationDelegate](./nsapplicationdelegate.md)
  A set of methods that manage your app’s life cycle and its interaction with common system services.
- [func NSApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> Int32](./nsapplicationmain%28_,_%29.md)
  Called by the main function to create and run the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/managing-ongoing-background-processes-in-your-mac)*