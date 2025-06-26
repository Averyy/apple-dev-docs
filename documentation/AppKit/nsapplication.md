# NSApplication

**Framework**: AppKit  
**Kind**: class

An object that manages an app’s main event loop and resources used by all of that app’s objects.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSApplication
```

## Mentions

- [Choosing a Specific Appearance for Your macOS App](choosing-a-specific-appearance-for-your-macos-app.md)
- [Passing control from one app to another with cooperative activation](passing-control-from-one-app-to-another-with-cooperative-activation.md)

#### Overview

Every app uses a single instance of [`NSApplication`](nsapplication.md) to control the main event loop, keep track of the app’s windows and menus, distribute events to the appropriate objects (that’s, itself or one of its windows), set up autorelease pools, and receive notification of app-level events. An [`NSApplication`](nsapplication.md) object has a delegate (an object that you assign) that’s notified when the app starts or terminates, is hidden or activated, should open a file selected by the user, and so forth. By setting the delegate and implementing the delegate methods, you customize the behavior of your app without having to subclass [`NSApplication`](nsapplication.md). In your app’s `main()` function, create the [`NSApplication`](nsapplication.md) instance by calling the [`shared`](nsapplication/shared.md) class method. After creating the application object, the `main()` function should load your app’s main nib file and then start the event loop by sending the application object a [`run()`](nsapplication/run().md) message. If you create an Application project in Xcode, this `main()` function is created for you. The `main()` function Xcode creates begins by calling a function named `NSApplicationMain()`, which is functionally similar to the following:

```objc
void NSApplicationMain(int argc, char *argv[]) {
    [NSApplication sharedApplication];
    [NSBundle loadNibNamed:@"myMain" owner:NSApp];
    [NSApp run];
}
```

The [`shared`](nsapplication/shared.md) class method initializes the display environment and connects your program to the window server and the display server. The [`NSApplication`](nsapplication.md) object maintains a list of all the [`NSWindow`](nswindow.md) objects the app uses, so it can retrieve any of the app’s [`NSView`](nsview.md) objects. The [`shared`](nsapplication/shared.md) method also initializes the global variable `NSApp`, which you use to retrieve the [`NSApplication`](nsapplication.md) instance. [`shared`](nsapplication/shared.md) only performs the initialization once. If you invoke it more than once, it returns the application object it created previously.

The shared [`NSApplication`](nsapplication.md) object performs the important task of receiving events from the window server and distributing them to the proper [`NSResponder`](nsresponder.md) objects. `NSApp` translates an event into an [`NSEvent`](nsevent.md) object, then forwards the event object to the affected [`NSWindow`](nswindow.md) object. All keyboard and mouse events go directly to the [`NSWindow`](nswindow.md) object associated with the event. The only exception to this rule is if the Command key is pressed when a key-down event occurs; in this case, every [`NSWindow`](nswindow.md) object has an opportunity to respond to the event. When a window object receives an [`NSEvent`](nsevent.md) object from `NSApp`, it distributes it to the objects in its view hierarchy.

[`NSApplication`](nsapplication.md) is also responsible for dispatching certain Apple events received by the app. For example, macOS sends Apple events to your app at various times, such as when the app is launched or reopened. [`NSApplication`](nsapplication.md) installs Apple event handlers to handle these events by sending a message to the appropriate object. You can also use the [`NSAppleEventManager`](https://developer.apple.com/documentation/Foundation/NSAppleEventManager) class to register your own Apple event handlers. The [`applicationWillFinishLaunching(_:)`](nsapplicationdelegate/applicationwillfinishlaunching(_:).md) method is generally the best place to do so. For more information on how events are handled and how you can modify the default behavior, including information on working with Apple events in scriptable apps, see [`How Cocoa Applications Handle Apple Events`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_handle_AEs/SAppsHandleAEs.html#//apple_ref/doc/uid/20001239) in [`Cocoa Scripting Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164).

The [`NSApplication`](nsapplication.md) class sets up `@autorelease` block during initialization and inside the event loop—specifically, within its initialization (or [`shared`](nsapplication/shared.md)) and [`run()`](nsapplication/run().md) methods. Similarly, the methods AppKit adds to [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) employ `@autorelease` blocks during the loading of nib files. These `@autorelease` blocks aren’t accessible outside the scope of the respective [`NSApplication`](nsapplication.md) and [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) methods. Typically, an app creates objects either while the event loop is running or by loading objects from nib files, so this lack of access usually isn’t a problem. However, if you do need to use Cocoa classes within the `main()` function itself (other than to load nib files or to instantiate [`NSApplication`](nsapplication.md)), you should create an `@autorelease` block to contain the code using the classes.

##### The Delegate and Notifications

You can assign a delegate to your [`NSApplication`](nsapplication.md) object. The delegate responds to certain messages on behalf of the object. Some of these messages, such as [`application(_:openFile:)`](nsapplicationdelegate/application(_:openfile:).md), ask the delegate to perform an action. Another message, [`applicationShouldTerminate(_:)`](nsapplicationdelegate/applicationshouldterminate(_:).md), lets the delegate determine whether the app should be allowed to quit. The [`NSApplication`](nsapplication.md) class sends these messages directly to its delegate.

[`NSApplication`](nsapplication.md) also posts notifications to the app’s default notification center. Any object may register to receive one or more of the notifications posted by [`NSApplication`](nsapplication.md) by sending the message [`addObserver(_:selector:name:object:)`](https://developer.apple.com/documentation/Foundation/NotificationCenter/addObserver(_:selector:name:object:)) to the default notification center (an instance of the `NSNotificationCenter` class). The delegate of [`NSApplication`](nsapplication.md) is automatically registered to receive these notifications if it implements certain delegate methods. For example, [`NSApplication`](nsapplication.md) posts notifications when it’s about to be done launching the app and when it’s done launching the app ([`willFinishLaunchingNotification`](nsapplication/willfinishlaunchingnotification.md) and [`didFinishLaunchingNotification`](nsapplication/didfinishlaunchingnotification.md)). The delegate has an opportunity to respond to these notifications by implementing the methods [`applicationWillFinishLaunching(_:)`](nsapplicationdelegate/applicationwillfinishlaunching(_:).md) and [`applicationDidFinishLaunching(_:)`](nsapplicationdelegate/applicationdidfinishlaunching(_:).md). If the delegate wants to be informed of both events, it implements both methods. If it needs to know only when the app is finished launching, it implements only [`applicationDidFinishLaunching(_:)`](nsapplicationdelegate/applicationdidfinishlaunching(_:).md).

##### System Services

`NSApplication` interacts with the system services architecture to provide services to your app through the Services menu.

##### Subclassing Notes

You rarely should find a real need to create a custom `NSApplication` subclass. Unlike some object-oriented libraries, Cocoa doesn’t require you to subclass `NSApplication` to customize app behavior. Instead it gives you many other ways to customize an app. This section discusses both some of the possible reasons to subclass `NSApplication` and some of the reasons  to subclass `NSApplication`.

To use a custom subclass of `NSApplication`, send [`shared`](nsapplication/shared.md) to your subclass rather than directly to `NSApplication`. If you create your app in Xcode, you can accomplish this by setting your custom app class to be the principal class. In Xcode, double-click the app target in the Groups and Files list to open the Info window for the target. Then display the Properties pane of the window and replace “NSApplication” in the Principal Class field with the name of your custom class. The `NSApplicationMain` function sends [`shared`](nsapplication/shared.md) to the principal class to obtain the global app instance (`NSApp`)—which in this case will be an instance of your custom subclass of `NSApplication`.

> ❗ **Important**:  Many AppKit classes rely on the `NSApplication` class and may not work properly until this class is fully initialized. As a result, you should not, for example, attempt to invoke methods of other AppKit classes from an initialization method of an `NSApplication` subclass.

###### Methods to Override

Generally, you subclass `NSApplication` to provide your own special responses to messages that are routinely sent to the global app object (`NSApp`). `NSApplication` doesn’t have primitive methods in the sense of methods that you must override in your subclass. Here are four methods that are possible candidates for overriding:

- Override [`run()`](nsapplication/run().md) if you want the app to manage the main event loop differently than it does by default. (This a critical and complex task, however, that you should only attempt with good reason).
- Override [`sendEvent(_:)`](nsapplication/sendevent(_:).md) if you want to change how events are dispatched or perform some special event processing.
- Override [`requestUserAttention(_:)`](nsapplication/requestuserattention(_:).md) if you want to modify how your app attracts the attention of the user (for example, offering an alternative to the bouncing app icon in the Dock).
- Override [`target(forAction:)`](nsapplication/target(foraction:).md) to substitute another object for the target of an action message.

###### Special Considerations

The global app object uses `@autorelease` blocks in its [`run()`](nsapplication/run().md) method; if you override this method, you’ll need to create your own `@autorelease` blocks.

Do not override [`shared`](nsapplication/shared.md). The default implementation, which is essential to app behavior, is too complex to duplicate on your own.

###### Alternatives to Subclassing

`NSApplication` defines numerous [`Delegation`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) methods that offer opportunities for modifying specific aspects of app behavior. Instead of making a custom subclass of `NSApplication`, your app delegate may be able to implement one or more of these methods to accomplish your design goals. In general, a better design than subclassing `NSApplication` is to put the code that expresses your app’s special behavior into one or more custom objects called controllers. Methods defined in your controllers can be invoked from a small dispatcher object without being closely tied to the global app object.

## Topics

### Getting the shared app object
- [class var shared: NSApplication](nsapplication/shared.md)
  Returns the application instance, creating it if it doesn’t exist yet.
- [var NSApp: NSApplication!](nsapp.md)
  The global variable for the shared app instance.
### Managing the app’s behavior
- [var delegate: (any NSApplicationDelegate)?](nsapplication/delegate.md)
  The app delegate object.
- [protocol NSApplicationDelegate](nsapplicationdelegate.md)
  A set of methods that manage your app’s life cycle and its interaction with common system services.
### Managing the event loop
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](nsapplication/nextevent(matching:until:inmode:dequeue:).md)
  Returns the next event matching a given mask, or `nil` if no such event is found before a specified expiration date.
- [func discardEvents(matching: NSEvent.EventTypeMask, before: NSEvent?)](nsapplication/discardevents(matching:before:).md)
  Removes all events matching the given mask and generated before the specified event.
- [var currentEvent: NSEvent?](nsapplication/currentevent.md)
  The last event object that the app retrieved from the event queue.
- [var isRunning: Bool](nsapplication/isrunning.md)
  A Boolean value indicating whether the main event loop is running.
- [func run()](nsapplication/run.md)
  Starts the main event loop.
- [func finishLaunching()](nsapplication/finishlaunching.md)
  Activates the app, opens any files specified by the `NSOpen` user default, and unhighlights the app’s icon.
- [func stop(Any?)](nsapplication/stop(_:).md)
  Stops the main event loop.
- [func sendEvent(NSEvent)](nsapplication/sendevent(_:).md)
  Dispatches an event to other objects.
- [func postEvent(NSEvent, atStart: Bool)](nsapplication/postevent(_:atstart:).md)
  Adds a given event to the receiver’s event queue.
### Posting actions
- [func tryToPerform(Selector, with: Any?) -> Bool](nsapplication/trytoperform(_:with:).md)
  Dispatches an action message to the specified target.
- [func sendAction(Selector, to: Any?, from: Any?) -> Bool](nsapplication/sendaction(_:to:from:).md)
  Sends the given action message to the given target.
- [func target(forAction: Selector) -> Any?](nsapplication/target(foraction:).md)
  Returns the object that receives the action message specified by the given selector.
- [func target(forAction: Selector, to: Any?, from: Any?) -> Any?](nsapplication/target(foraction:to:from:).md)
  Searches for an object that can receive the message specified by the given selector.
### Terminating the app
- [func terminate(Any?)](nsapplication/terminate(_:).md)
  Terminates the receiver.
- [func reply(toApplicationShouldTerminate: Bool)](nsapplication/reply(toapplicationshouldterminate:).md)
  Responds to `NSTerminateLater` once the app knows whether it can terminate.
### Activating and deactivating the app
- [Passing control from one app to another with cooperative activation](passing-control-from-one-app-to-another-with-cooperative-activation.md)
  Request focus for your app, and coordinate passing control from one app to another.
- [func activate()](nsapplication/activate.md)
  Activates the receiver app, if appropriate.
- [func deactivate()](nsapplication/deactivate.md)
  Deactivates the receiver.
- [var isActive: Bool](nsapplication/isactive.md)
  A Boolean value indicating whether this is the active app.
- [func yieldActivation(to: NSRunningApplication)](nsapplication/yieldactivation(to:).md)
  Explicitly allows another app to make itself active.
- [func yieldActivation(toApplicationWithBundleIdentifier: String)](nsapplication/yieldactivation(toapplicationwithbundleidentifier:).md)
  Explicitly allows another app to make itself active.
- [NSApplication.ActivationOptions](nsapplication/activationoptions.md)
  The following flags are for [`activate(options:)`](nsrunningapplication/activate(options:).md).
### Managing relaunch on login
- [func disableRelaunchOnLogin()](nsapplication/disablerelaunchonlogin.md)
  Disables relaunching the app on login.
- [func enableRelaunchOnLogin()](nsapplication/enablerelaunchonlogin.md)
  Enables relaunching the app on login.
### Managing remote notifications
- [func registerForRemoteNotifications()](nsapplication/registerforremotenotifications.md)
  Register for notifications sent by Apple Push Notification service (APNs).
- [func unregisterForRemoteNotifications()](nsapplication/unregisterforremotenotifications.md)
  Unregister for notifications received from Apple Push Notification service.
- [var enabledRemoteNotificationTypes: NSApplication.RemoteNotificationType](nsapplication/enabledremotenotificationtypes.md)
  The types of push notifications that the app accepts.
- [func registerForRemoteNotifications(matching: NSApplication.RemoteNotificationType)](nsapplication/registerforremotenotifications(matching:).md)
  Register to receive notifications of the specified types from a provider through the Apple Push Notification service.
- [var isRegisteredForRemoteNotifications: Bool](nsapplication/isregisteredforremotenotifications.md)
  A Boolean value indicating whether the app is registered with Apple Push Notification service (APNs).
- [NSApplication.RemoteNotificationType](nsapplication/remotenotificationtype.md)
  These constants determine whether apps launched by remote notifications display a badge.
### Managing the app’s appearance
- [var appearance: NSAppearance?](nsapplication/appearance.md)
  The appearance associated with the app’s windows.
- [var effectiveAppearance: NSAppearance](nsapplication/effectiveappearance.md)
  The appearance that AppKit uses to draw the app’s interface.
- [var currentSystemPresentationOptions: NSApplication.PresentationOptions](nsapplication/currentsystempresentationoptions.md)
  The set of app presentation options that are currently in effect for the system.
- [var presentationOptions: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.property.md)
  The presentation options that should be in effect for the system when this app is active.
- [NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct.md)
  Constants that control the presentation of the app, typically for fullscreen apps such as games or kiosks.
- [var applicationShouldSuppressHighDynamicRangeContent: Bool](nsapplication/applicationshouldsuppresshighdynamicrangecontent.md)
  A boolean value indicating whether your application should suppress HDR content based on established policy. Built-in AppKit components such as NSImageView will automatically behave correctly with HDR content. You should use this value in conjunction with notifications (`NSApplicationShouldBeginSuppressingHighDynamicRangeContentNotification` and `NSApplicationShouldEndSuppressingHighDynamicRangeContentNotification`) to suppress HDR content in your application when signaled to do so.
### Managing windows, panels, and menus
- [App Windows](app-windows.md)
  Show, hide, minimize, arrange, and update your app’s windows.
- [Modal Windows and Panels](modal-windows-and-panels.md)
  Display a modal window or show one of the standard app panels, such as the app’s About panel.
- [Menus](menus.md)
  Access the app’s main menu items and update the window and services menus.
### User interface layout direction
- [var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection](nsapplication/userinterfacelayoutdirection.md)
  The layout direction of the user interface.
- [enum NSUserInterfaceLayoutDirection](nsuserinterfacelayoutdirection.md)
  Specifies the directional flow of the user interface.
### Accessing the dock tile
- [var dockTile: NSDockTile](nsapplication/docktile.md)
  The app’s Dock tile.
- [var applicationIconImage: NSImage!](nsapplication/applicationiconimage.md)
  The image used for the app’s icon.
### Customizing the Touch Bar
- [func toggleTouchBarCustomizationPalette(Any?)](nsapplication/toggletouchbarcustomizationpalette(_:).md)
  Show or hides the interface for customizing the Touch Bar.
### Managing user attention requests
- [func requestUserAttention(NSApplication.RequestUserAttentionType) -> Int](nsapplication/requestuserattention(_:).md)
  Starts a user attention request.
- [NSApplication.RequestUserAttentionType](nsapplication/requestuserattentiontype.md)
  These constants specify the level of severity of a user attention request and are used by [`cancelUserAttentionRequest(_:)`](nsapplication/canceluserattentionrequest(_:).md) and [`requestUserAttention(_:)`](nsapplication/requestuserattention(_:).md).
- [func cancelUserAttentionRequest(Int)](nsapplication/canceluserattentionrequest(_:).md)
  Cancels a previous user attention request.
- [func reply(toOpenOrPrint: NSApplication.DelegateReply)](nsapplication/reply(toopenorprint:).md)
  Handles errors that might occur when the user attempts to open or print files.
- [NSApplication.DelegateReply](nsapplication/delegatereply.md)
  Constants that indicate whether a copy or print operation was successful, was canceled, or failed.
### Providing help information
- [func registerUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](nsapplication/registeruserinterfaceitemsearchhandler(_:).md)
  Register an object that provides help data to your app.
- [func searchString(String, inUserInterfaceItemString: String, range: NSRange, found: UnsafeMutablePointer<NSRange>?) -> Bool](nsapplication/searchstring(_:inuserinterfaceitemstring:range:found:).md)
  Searches for the string in the user interface.
- [func unregisterUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](nsapplication/unregisteruserinterfaceitemsearchhandler(_:).md)
  Unregister an object that provides help data to your app.
- [func showHelp(Any?)](nsapplication/showhelp(_:).md)
  If your project is properly registered, and the necessary keys have been set in the property list, this method launches Help Viewer and displays the first page of your app’s help book.
- [func activateContextHelpMode(Any?)](nsapplication/activatecontexthelpmode(_:).md)
  Places the receiver in context-sensitive help mode.
- [var helpMenu: NSMenu?](nsapplication/helpmenu.md)
  The help menu used by the app.
### Providing services
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](nsapplication/validrequestor(forsendtype:returntype:).md)
  Indicates whether the receiver can send and receive the specified pasteboard types.
- [var servicesProvider: Any?](nsapplication/servicesprovider.md)
  The object that provides the services the current app advertises in the Services menu of other apps.
### Determining access to the keyboard
- [var isFullKeyboardAccessEnabled: Bool](nsapplication/isfullkeyboardaccessenabled.md)
  A Boolean value indicating whether Full Keyboard Access is enabled in the Keyboard preference pane.
### Hiding apps
- [func hideOtherApplications(Any?)](nsapplication/hideotherapplications(_:).md)
  Hides all apps, except the receiver.
- [func unhideAllApplications(Any?)](nsapplication/unhideallapplications(_:).md)
  Unhides all apps, including the receiver.
### Managing threads
- [class func detachDrawingThread(Selector, toTarget: Any, with: Any?)](nsapplication/detachdrawingthread(_:totarget:with:).md)
  Creates and executes a new thread based on the specified target and selector.
### Logging exceptions
- [func reportException(NSException)](nsapplication/reportexception(_:).md)
  Logs a given exception by calling `NSLog()`.
### Configuring the activation policy
- [func activationPolicy() -> NSApplication.ActivationPolicy](nsapplication/activationpolicy.md)
  Returns the app’s activation policy.
- [func setActivationPolicy(NSApplication.ActivationPolicy) -> Bool](nsapplication/setactivationpolicy(_:).md)
  Attempts to modify the app’s activation policy.
- [NSApplication.ActivationPolicy](nsapplication/activationpolicy-swift.enum.md)
  Activation policies (used by [`activationPolicy`](nsrunningapplication/activationpolicy.md)) that control whether and how an app may be activated.
### Scripting your app
- [var orderedDocuments: [NSDocument]](nsapplication/ordereddocuments.md)
  An array of document objects arranged according to the front-to-back ordering of their associated windows.
- [var orderedWindows: [NSWindow]](nsapplication/orderedwindows.md)
  An array of window objects arranged according to their front-to-back ordering on the screen.
### Notifications
- [class let didBecomeActiveNotification: NSNotification.Name](nsapplication/didbecomeactivenotification.md)
  Posted immediately after the app becomes active.
- [class let didChangeScreenParametersNotification: NSNotification.Name](nsapplication/didchangescreenparametersnotification.md)
  Posted when the configuration of the displays attached to the computer is changed.
- [class let didFinishLaunchingNotification: NSNotification.Name](nsapplication/didfinishlaunchingnotification.md)
  Posted at the end of the [`finishLaunching()`](nsapplication/finishlaunching().md) method to indicate that the app has completed launching and is ready to run.
- [class let didHideNotification: NSNotification.Name](nsapplication/didhidenotification.md)
  Posted at the end of the [`hide(_:)`](nsapplication/hide(_:).md) method to indicate that the app is now hidden.
- [class let didResignActiveNotification: NSNotification.Name](nsapplication/didresignactivenotification.md)
  Posted immediately after the app gives up its active status to another app.
- [class let didUnhideNotification: NSNotification.Name](nsapplication/didunhidenotification.md)
  Posted at the end of the [`unhideWithoutActivation()`](nsapplication/unhidewithoutactivation().md) method to indicate that the app is now visible.
- [class let didUpdateNotification: NSNotification.Name](nsapplication/didupdatenotification.md)
  Posted at the end of the [`updateWindows()`](nsapplication/updatewindows().md) method to indicate that the app has finished updating its windows.
- [class let willBecomeActiveNotification: NSNotification.Name](nsapplication/willbecomeactivenotification.md)
  Posted immediately before the app becomes active.
- [class let willFinishLaunchingNotification: NSNotification.Name](nsapplication/willfinishlaunchingnotification.md)
  Posted at the start of the [`finishLaunching()`](nsapplication/finishlaunching().md) method to indicate that the app has completed its initialization process and is about to finish launching.
- [class let willHideNotification: NSNotification.Name](nsapplication/willhidenotification.md)
  Posted at the start of the [`hide(_:)`](nsapplication/hide(_:).md) method to indicate that the app is about to be hidden.
- [class let willResignActiveNotification: NSNotification.Name](nsapplication/willresignactivenotification.md)
  Posted immediately before the app gives up its active status to another app.
- [class let willTerminateNotification: NSNotification.Name](nsapplication/willterminatenotification.md)
  Sends a notification to termintate the app.
- [class let willUnhideNotification: NSNotification.Name](nsapplication/willunhidenotification.md)
  Posted at the start of the [`unhideWithoutActivation()`](nsapplication/unhidewithoutactivation().md) method to indicate that the app is about to become visible.
- [class let willUpdateNotification: NSNotification.Name](nsapplication/willupdatenotification.md)
  Posted at the start of the [`updateWindows()`](nsapplication/updatewindows().md) method to indicate that the app is about to update its windows.
- [class let didFinishRestoringWindowsNotification: NSNotification.Name](nsapplication/didfinishrestoringwindowsnotification.md)
  Posted when the app has finished restoring windows.
- [class let didChangeOcclusionStateNotification: NSNotification.Name](nsapplication/didchangeocclusionstatenotification.md)
  Posted when the app’s occlusion state changes.
### Loading Cocoa bundles
- [static func loadApplication()](nsapplication/loadapplication.md)
### Displaying high dynamic resolution (HDR) content
- [var applicationShouldSuppressHighDynamicRangeContent: Bool](nsapplication/applicationshouldsuppresshighdynamicrangecontent.md)
  A boolean value indicating whether your application should suppress HDR content based on established policy. Built-in AppKit components such as NSImageView will automatically behave correctly with HDR content. You should use this value in conjunction with notifications (`NSApplicationShouldBeginSuppressingHighDynamicRangeContentNotification` and `NSApplicationShouldEndSuppressingHighDynamicRangeContentNotification`) to suppress HDR content in your application when signaled to do so.
- [NSApplication.ShouldBeginSuppressingHighDynamicRangeContent](nsapplication/shouldbeginsuppressinghighdynamicrangecontent.md)
- [NSApplication.ShouldEndSuppressingHighDynamicRangeContent](nsapplication/shouldendsuppressinghighdynamicrangecontent.md)
### Deprecated
- [Deprecated Symbols](nsapplication-deprecated-symbols.md)
  Review symbols that are no longer supported, and find the replacements to use instead.
### Instance Methods
- [func addSceneRepresentation<C>(NSHostingSceneRepresentation<C>)](nsapplication/addscenerepresentation(_:).md)
  Adds the specified SwiftUI scene representation to the current application.

## Relationships

### Inherits From
- [NSResponder](nsresponder.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSMenuItemValidation](nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceValidations](nsuserinterfacevalidations.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSRunningApplication](nsrunningapplication.md)
  An object that can manipulate and provide information for a single instance of an app.
- [protocol NSApplicationDelegate](nsapplicationdelegate.md)
  A set of methods that manage your app’s life cycle and its interaction with common system services.
- [func NSApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> Int32](nsapplicationmain(_:_:).md)
  Called by the main function to create and run the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication)*