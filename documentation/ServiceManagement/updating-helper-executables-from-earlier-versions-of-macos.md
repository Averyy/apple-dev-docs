# Updating helper executables from earlier versions of macOS

**Framework**: Service Management

Simplify your app’s helper executables and support new authorization controls.

#### Overview

Launch daemons, launch agents, and startup items are helper executables that macOS starts on behalf of the user that extend the capabilities of apps or provide additional capabilities to users. For example, a `LaunchDaemon` can provide persistent background service for an app, a `LaunchAgent` can provide auxiliary UI capabilities like menu bar extras, and a `LoginItem` can provide the ability to automount remote directories or launch applications when the user logs in.

Prior to macOS 13, part of the application-design process of helper executables included scripts that installed one or more property lists into specific directories based on the type of service, such as the following locations of property lists:

`$HOME/Library/LaunchAgents`

`/Library/LaunchAgents`

`/Library/LaunchDaemons`

In macOS 13 and later, a new structure in the app bundle simplifies the installation of these login items and associated property lists. This new structure allows you to keep helper app resources inside the app’s bundle, which reduces the need for specialized installation scripts or permission to write files into system directories.

##### Upgrade Existing Projects

Upgrading an existing project requires the following general steps — some of which may be optional based on the type of services your app provides:

- Install the helper executable within the app bundle, such as in `Contents/Resources`.
- Install `LaunchAgent` property lists in the app bundle in `Contents/Library/LaunchAgents`.
- Install `LaunchDaemon` property lists in the app bundle in `Contents/Library/LaunchDaemons`.
- In the agents and daemons property lists, replace the `Program` key with the `BundleProgram` key and make the path relative to the bundle, such as `Contents/Resources/mydaemon`.

Apps that don’t use the new bundle structure can determine whether their app’s login items are in a disabled state by checking [`statusForLegacyPlist(at:)`](smappservice/statusforlegacyplist(at:).md), which returns one of the [`SMAppService.Status`](smappservice/status-swift.enum.md) constants that describes the authorization status. Then your app can alert the user to take an appropriate action depending on the importance of the helper executable.

In apps that target macOS 13 and later, your app needs to only use the property list locations outlined above.

> ❗ **Important**:  Tell users the purpose of the helper executables your app includes. If your app can’t run or operate correctly without helper executables, check the authorization status at launch. If helper executables don’t have authorization, alert the user, and call [`openSystemSettingsLoginItems()`](smappservice/opensystemsettingsloginitems().md) to suggest that they update the System Settings.

##### Connect Services to App Names in System Settings

Every app that supports a `LoginItem`, `LaunchAgent`, or `LaunchDaemon` has a corresponding switch in the Login Items panel in System Settings. The user can use this switch to allow the corresponding executables to run when they log in, or in the case of a `LaunchDaemon`, when the system starts up.

`LaunchAgents` and `LaunchDaemons` in the app bundle automatically associate with that app in the Login Items panel.

`LaunchAgents` and `LaunchDaemons` that aren’t using the app bundle can adopt the new `AssociatedBundleIdentifiers` key in their `launchd` property list. This optional key indicates which bundles the Login Items panel associates with the helper executable. If an app installs a legacy property list, the property list needs to include the `AssociatedBundleIdentifiers` key with a value of the app’s bundle identifier.

> ❗ **Important**:  The Team Identifier of the `Program` or `ProgramArguments` executable in the legacy property list must match that of the app bundle for the `AssociatedBundleIdentifiers` key. Launch Services needs to know about the apps that the `AssociatedBundleIdentifiers` key targets. If necessary, register the app using [`LSRegisterURL(_:_:)`](https://developer.apple.com/documentation/coreservices/1446350-lsregisterurl).

If a legacy `LaunchAgent` or `LaunchDaemon` doesn’t have the `AssociatedBundleIdentifiers` key in its property list, instead of the app name, System Settings displays the organization name in the app’s signing certificate.

If the system can’t attribute a `LaunchAgent` or `LaunchDaemon` to an app and the executable isn’t signed, System Settings displays the executable name from the `Program` or `ProgramArguments` key in the legacy property list.

##### Respond to Changes in System Settings

In macOS 13 and later, your app can check the authorization state in the System Settings using the `SMAppService` class to get the status of a `LoginItem`, `LaunchAgent`, or `LaunchDaemon`.

The example below demonstrates checking the authorization state of the three kinds of helper executables with the bundle identifier or property lists:

```swift
func initializer_demo() {
// The identifier must match the CFBundleIdentifier string in Info.plist.

// LoginItem path: $APP.app/Contents/Library/LoginItems/MyMenuExtra.app/Contents/Info.plist
let loginItem = SMAppService.loginItem(identifier: "com.example.mymenuextra")

// LaunchDaemon path: $APP.app/Contents/Library/LaunchDaemons/com.example.daemon.plist
let daemon = SMAppService.daemon(plistName: "com.example.daemon.plist");

// LaunchAgent path: $APP.app/Contents/Library/LaunchAgents/com.example.agent.plist
let agent = SMAppService.agent(plistName: "com.example.agent.plist");

// Retrieving the app reference if the main app itself needs to launch instead of a helper.
let mainApp = SMAppService.mainApp
}

```

The example below shows an approach to user interaction with the System Settings check box to register and unregister a helper executable:

```swift
func handle_checkbox_toggle(_ checked: Bool) {
    let service = SMAppService.loginItem(identifier:"com.example.mymenuextra")
    if (checked) {
        do {
           try service.register()
        } catch {
            os_log("Unable to register \(error)")
        }
    } else {
        service.unregister(completionHandler: { error in
        if let error = error {
            os_log("Unable to unregister \(error)")
        } else {
            // Successfully unregistered service.
        }
    })
  }
}

```

If your app uses launch daemons, it needs to register those first. Launch daemons require authentication by the user because the user is authorizing a system level-process. If the user authorizes the `LaunchDaemon`, the system approves all the other helper executables present in the app bundle, which results in fewer authorization interactions with the user. If your app doesn’t provide a `LauchDaemon`, it needs to register each `LoginItem` or `LaunchAgent`.

If your app depends on its helper executables to operate correctly, it needs to check the authorization state and allow the user to change the app’s authorization. If the user agrees, call [`openSystemSettingsLoginItems()`](smappservice/opensystemsettingsloginitems().md) to open the System Settings so they can enable or disable the app’s helper executables.

## See Also

- [Updating your app package installer to use the new Service Management API](updating-your-app-package-installer-to-use-the-new-service-management-api.md)
  Learn about the Service Management API with a GUI-less agent app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/updating-helper-executables-from-earlier-versions-of-macos)*