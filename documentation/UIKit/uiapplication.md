# UIApplication

**Framework**: UIKit  
**Kind**: class

The centralized point of control and coordination for apps running in iOS.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIApplication
```

## Mentions

- [Using responders and the responder chain to handle events](using-responders-and-the-responder-chain-to-handle-events.md)
- [About App Development with UIKit](about-app-development-with-uikit.md)
- [About the app launch sequence](about-the-app-launch-sequence.md)
- [About the UI preservation process](about-the-ui-preservation-process.md)
- [Handling key presses made on a physical keyboard](handling-key-presses-made-on-a-physical-keyboard.md)

#### Overview

Every iOS app has exactly one instance of [`UIApplication`](uiapplication.md) (or, very rarely, a subclass of [`UIApplication`](uiapplication.md)). When an app launches, the system calls the [`UIApplicationMain(_:_:_:_:)`](uiapplicationmain(_:_:_:_:)-1yub7.md) function. Among its other tasks, this function creates a singleton [`UIApplication`](uiapplication.md) object that you access using [`shared`](uiapplication/shared.md).

Your app’s application object handles the initial routing of incoming user events. It dispatches action messages forwarded to it by control objects (instances of the [`UIControl`](uicontrol.md) class) to appropriate target objects. The application object maintains a list of open windows ([`UIWindow`](uiwindow.md) objects), which it can use to retrieve any of the app’s [`UIView`](uiview.md) objects.

The [`UIApplication`](uiapplication.md) class defines a delegate that conforms to the [`UIApplicationDelegate`](uiapplicationdelegate.md) protocol and must implement some of the protocol’s methods. The application object informs the delegate of significant runtime events—for example, app launch, low-memory warnings, and app termination—giving it an opportunity to respond appropriately.

Apps can cooperatively handle a resource, such as an email or an image file, through the [`open(_:options:completionHandler:)`](uiapplication/open(_:options:completionhandler:).md) method. For example, an app that calls this method with an email URL causes the Mail app to launch and display the message.

The APIs in this class allow you to manage device-specific behavior. Use your [`UIApplication`](uiapplication.md) object to do the following:

- Temporarily suspend incoming touch events ([`beginIgnoringInteractionEvents()`](uiapplication/beginignoringinteractionevents().md))
- Register for remote notifications ([`registerForRemoteNotifications()`](uiapplication/registerforremotenotifications().md))
- Trigger the undo-redo UI ([`applicationSupportsShakeToEdit`](uiapplication/applicationsupportsshaketoedit.md))
- Determine whether there is an installed app registered to handle a URL scheme ([`canOpenURL(_:)`](uiapplication/canopenurl(_:).md))
- Extend the execution of the app so that it can finish a task in the background ([`beginBackgroundTask(expirationHandler:)`](uiapplication/beginbackgroundtask(expirationhandler:).md) and [`beginBackgroundTask(withName:expirationHandler:)`](uiapplication/beginbackgroundtask(withname:expirationhandler:).md))
- Schedule and cancel local notifications ([`scheduleLocalNotification(_:)`](uiapplication/schedulelocalnotification(_:).md) and [`cancelLocalNotification(_:)`](uiapplication/cancellocalnotification(_:).md))
- Coordinate the reception of remote-control events ([`beginReceivingRemoteControlEvents()`](uiapplication/beginreceivingremotecontrolevents().md) and [`endReceivingRemoteControlEvents()`](uiapplication/endreceivingremotecontrolevents().md))
- Perform app-level state restoration tasks (methods in the [`Managing state restoration`](uiapplication#Managing-state-restoration.md) task group)

##### Subclassing Notes

Most apps don’t need to subclass [`UIApplication`](uiapplication.md). Instead, use an app delegate to manage interactions between the system and the app.

If your app must handle incoming events before the system does—a very rare situation—you can implement a custom event or action dispatching mechanism. To do this, subclass [`UIApplication`](uiapplication.md) and override the [`sendEvent(_:)`](uiapplication/sendevent(_:).md) and/or the [`sendAction(_:to:from:for:)`](uiapplication/sendaction(_:to:from:for:).md) methods. For every event you intercept, after you handle the event, dispatch it back to the system by calling:

```swift
super.sendEvent(event)
```

Intercepting events is only rarely required and you should avoid it if possible.

## Topics

### Accessing the shared application
- [class var shared: UIApplication](uiapplication/shared.md)
  The singleton app instance.
### Configuring your app’s behavior
- [var delegate: (any UIApplicationDelegate)?](uiapplication/delegate.md)
  The delegate of the app object.
- [protocol UIApplicationDelegate](uiapplicationdelegate.md)
  A set of methods to manage shared behaviors for your app.
### Registering for remote notifications
- [func registerForRemoteNotifications()](uiapplication/registerforremotenotifications.md)
  Registers to receive remote notifications through Apple Push Notification service.
- [func unregisterForRemoteNotifications()](uiapplication/unregisterforremotenotifications.md)
  Unregisters for all remote notifications received through Apple Push Notification service.
- [var isRegisteredForRemoteNotifications: Bool](uiapplication/isregisteredforremotenotifications.md)
  A Boolean value that indicates whether the app is currently registered for remote notifications.
### Getting the application state
- [var applicationState: UIApplication.State](uiapplication/applicationstate.md)
  The app’s current state, or that of its most active scene.
- [UIApplication.State](uiapplication/state.md)
  Constants that indicate the running states of an app.
### Getting scene information
- [var supportsMultipleScenes: Bool](uiapplication/supportsmultiplescenes.md)
  A Boolean value that indicates whether the app may display multiple scenes simultaneously.
- [var connectedScenes: Set<UIScene>](uiapplication/connectedscenes.md)
  The app’s currently connected scenes.
- [var openSessions: Set<UISceneSession>](uiapplication/opensessions.md)
  The sessions whose scenes are either currently active or archived by the system.
### Managing a scene’s life cycle
- [func activateSceneSession(for: UISceneSessionActivationRequest, errorHandler: ((any Error) -> Void)?)](uiapplication/activatescenesession(for:errorhandler:).md)
  Asks the system to activate an existing scene or create a new scene and associate it with your app.
- [func requestSceneSessionDestruction(UISceneSession, options: UISceneDestructionRequestOptions?, errorHandler: ((any Error) -> Void)?)](uiapplication/requestscenesessiondestruction(_:options:errorhandler:).md)
  Asks the system to dismiss an existing scene and remove it from the app switcher.
- [func requestSceneSessionRefresh(UISceneSession)](uiapplication/requestscenesessionrefresh(_:).md)
  Asks the system to update any system UI associated with the specified scene.
- [struct UISceneSessionActivationRequest](uiscenesessionactivationrequest-swift.struct.md)
  A collection of properties that you use to request activation of a scene.
- [UIScene.ActivationRequestOptions](uiscene/activationrequestoptions.md)
  An object that contains information you want the system to use when activating the session associated with a scene.
- [class UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md)
  An object you pass to UIKit to permanently remove a scene and its associated session from your app.
### Managing background tasks
- [var backgroundRefreshStatus: UIBackgroundRefreshStatus](uiapplication/backgroundrefreshstatus.md)
  Indicates whether the app can refresh content when running in the background.
- [enum UIBackgroundRefreshStatus](uibackgroundrefreshstatus.md)
  Constants that indicate whether background execution is enabled for the app.
- [class let backgroundRefreshStatusDidChangeNotification: NSNotification.Name](uiapplication/backgroundrefreshstatusdidchangenotification.md)
  A notification that posts when the app’s status for downloading content in the background changes.
- [func beginBackgroundTask(withName: String?, expirationHandler: (() -> Void)?) -> UIBackgroundTaskIdentifier](uiapplication/beginbackgroundtask(withname:expirationhandler:).md)
  Marks the start of a task with a custom name that should continue if the app enters the background.
- [func beginBackgroundTask(expirationHandler: (() -> Void)?) -> UIBackgroundTaskIdentifier](uiapplication/beginbackgroundtask(expirationhandler:).md)
  Marks the start of a task that should continue if the app enters the background.
- [func endBackgroundTask(UIBackgroundTaskIdentifier)](uiapplication/endbackgroundtask(_:).md)
  Marks the end of a specific long-running background task.
- [struct UIBackgroundTaskIdentifier](uibackgroundtaskidentifier.md)
  A unique token that identifies a request to run in the background.
- [var backgroundTimeRemaining: TimeInterval](uiapplication/backgroundtimeremaining.md)
  The maximum amount of time remaining for the app to run in the background.
### Fetching content in the background
- [class let backgroundFetchIntervalMinimum: TimeInterval](uiapplication/backgroundfetchintervalminimum.md)
  The smallest fetch interval supported by the system.
- [class let backgroundFetchIntervalNever: TimeInterval](uiapplication/backgroundfetchintervalnever.md)
  A fetch interval large enough to prevent fetch operations from occurring.
### Opening a URL resource
- [func open(URL, options: [UIApplication.OpenExternalURLOptionsKey : Any], completionHandler: ((Bool) -> Void)?)](uiapplication/open(_:options:completionhandler:).md)
  Attempts to asynchronously open the resource at the specified URL.
- [func canOpenURL(URL) -> Bool](uiapplication/canopenurl(_:).md)
  Returns a Boolean value that indicates whether an app is available to handle a URL scheme.
- [UIApplication.OpenExternalURLOptionsKey](uiapplication/openexternalurloptionskey.md)
  Options for opening a URL.
### Deep linking to custom settings
- [class let openSettingsURLString: String](uiapplication/opensettingsurlstring.md)
  The URL string you use to deep link to your app’s custom settings in the Settings app.
- [static let openNotificationSettingsURLString: String](uiapplication/opennotificationsettingsurlstring.md)
  The URL string you use to deep link to your app’s notification settings in the Settings app.
- [let UIApplicationOpenNotificationSettingsURLString: String](uiapplicationopennotificationsettingsurlstring.md)
  A constant that provides the URL string you use to deep link to your app’s notification settings in the Settings app.
- [class let openDefaultApplicationsSettingsURLString: String](uiapplication/opendefaultapplicationssettingsurlstring.md)
  The URL string used to select a default app in the Settings app.
### Managing the app’s idle timer
- [var isIdleTimerDisabled: Bool](uiapplication/isidletimerdisabled.md)
  A Boolean value that controls whether the idle timer is disabled for the app.
### Managing state restoration
- [func extendStateRestoration()](uiapplication/extendstaterestoration.md)
  Tells the app that your code is restoring state asynchronously.
- [func completeStateRestoration()](uiapplication/completestaterestoration.md)
  Tells the app that your code has finished any asynchronous state restoration.
- [func ignoreSnapshotOnNextApplicationLaunch()](uiapplication/ignoresnapshotonnextapplicationlaunch.md)
  Prevents the app from using the recent snapshot image during the next launch cycle.
- [class func registerObject(forStateRestoration: any UIStateRestoring, restorationIdentifier: String)](uiapplication/registerobject(forstaterestoration:restorationidentifier:).md)
  Registers a custom object for use with the state restoration system.
### Providing an app’s shortcut items
- [var shortcutItems: [UIApplicationShortcutItem]?](uiapplication/shortcutitems.md)
  The Home screen dynamic quick actions for your app; available on devices that support 3D Touch.
### Accessing protected content
- [var isProtectedDataAvailable: Bool](uiapplication/isprotecteddataavailable.md)
  A Boolean value that indicates whether content protection is active.
- [class let protectedDataDidBecomeAvailableNotification: NSNotification.Name](uiapplication/protecteddatadidbecomeavailablenotification.md)
  A notification that posts when the protected files become available for your code to access.
- [class let protectedDataWillBecomeUnavailableNotification: NSNotification.Name](uiapplication/protecteddatawillbecomeunavailablenotification.md)
  A notification that posts shortly before protected files are locked down and become inaccessible.
### Receiving remote control events
- [func beginReceivingRemoteControlEvents()](uiapplication/beginreceivingremotecontrolevents.md)
  Tells the app to begin receiving remote-control events.
- [func endReceivingRemoteControlEvents()](uiapplication/endreceivingremotecontrolevents.md)
  Tells the app to stop receiving remote-control events.
### Accessing the layout direction
- [var userInterfaceLayoutDirection: UIUserInterfaceLayoutDirection](uiapplication/userinterfacelayoutdirection.md)
  The layout direction of the user interface.
- [enum UIUserInterfaceLayoutDirection](uiuserinterfacelayoutdirection.md)
  Constants that specify the directional flow of the user interface.
### Controlling and handling events
- [func sendEvent(UIEvent)](uiapplication/sendevent(_:).md)
  Dispatches an event to the appropriate responder objects in the app.
- [func sendAction(Selector, to: Any?, from: Any?, for: UIEvent?) -> Bool](uiapplication/sendaction(_:to:from:for:).md)
  Sends an action message identified by the selector to a specified target.
- [var applicationSupportsShakeToEdit: Bool](uiapplication/applicationsupportsshaketoedit.md)
  A Boolean value that determines whether shaking the device displays the undo-redo user interface.
### Managing the app’s icon
- [var supportsAlternateIcons: Bool](uiapplication/supportsalternateicons.md)
  A Boolean value that indicates whether the app is allowed to change its icon.
- [var alternateIconName: String?](uiapplication/alternateiconname.md)
  The name of the icon the system displays for the app.
- [func setAlternateIconName(String?, completionHandler: (((any Error)?) -> Void)?)](uiapplication/setalternateiconname(_:completionhandler:).md)
  Changes the icon the system displays for the app.
### Managing the preferred content size
- [var preferredContentSizeCategory: UIContentSizeCategory](uiapplication/preferredcontentsizecategory.md)
  The font sizing option preferred by the user.
- [struct UIContentSizeCategory](uicontentsizecategory.md)
  Constants that indicate the preferred size of your content.
- [protocol UIContentSizeCategoryAdjusting](uicontentsizecategoryadjusting.md)
  A collection of methods that give controls an easy way to adopt automatic adjustment to content category changes.
- [static let didChangeNotification: NSNotification.Name](uicontentsizecategory/didchangenotification.md)
  A notification that posts when the user changes the preferred content size setting.
- [static let newValueUserInfoKey: String](uicontentsizecategory/newvalueuserinfokey.md)
  A key that reflects the new preferred content size.
### Specifying the supported interface orientations
- [func supportedInterfaceOrientations(for: UIWindow?) -> UIInterfaceOrientationMask](uiapplication/supportedinterfaceorientations(for:).md)
  Returns the default set of interface orientations to use for the view controllers in the specified window.
### Tracking controls in the run loop
- [static let tracking: RunLoop.Mode](../Foundation/RunLoop/Mode/tracking.md)
  The mode set while tracking in controls takes place.
### Detecting screenshots
- [class let userDidTakeScreenshotNotification: NSNotification.Name](uiapplication/userdidtakescreenshotnotification.md)
  A notification that posts when a person takes a screenshot on the device.
### Discovering if your app is the default app in a category
- [func isDefault(UIApplication.Category) throws -> Bool](uiapplication/isdefault(_:).md)
  Reports whether this app is the person’s default app in the given category.
- [UIApplication.Category](uiapplication/category.md)
  Constants that describe the types of apps in the system.
- [UIApplication.CategoryDefaultError](uiapplication/categorydefaulterror.md)
  Errors that can happen when the system checks if your app is the default app in a category.
### Deprecated
- [Deprecated symbols](uiapplication-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Structures
- [UIApplication.BackgroundRefreshStatusDidChangeMessage](uiapplication/backgroundrefreshstatusdidchangemessage.md)
- [UIApplication.DidBecomeActiveMessage](uiapplication/didbecomeactivemessage.md)
- [UIApplication.DidEnterBackgroundMessage](uiapplication/didenterbackgroundmessage.md)
- [UIApplication.DidFinishLaunchingMessage](uiapplication/didfinishlaunchingmessage.md)
- [UIApplication.DidReceiveMemoryWarningMessage](uiapplication/didreceivememorywarningmessage.md)
- [UIApplication.ProtectedDataDidBecomeAvailableMessage](uiapplication/protecteddatadidbecomeavailablemessage.md)
- [UIApplication.ProtectedDataWillBecomeUnavailableMessage](uiapplication/protecteddatawillbecomeunavailablemessage.md)
- [UIApplication.SignificantTimeChangeMessage](uiapplication/significanttimechangemessage.md)
- [UIApplication.UserDidTakeScreenshotMessage](uiapplication/userdidtakescreenshotmessage.md)
- [UIApplication.WillEnterForegroundMessage](uiapplication/willenterforegroundmessage.md)
- [UIApplication.WillResignActiveMessage](uiapplication/willresignactivemessage.md)
- [UIApplication.WillTerminateMessage](uiapplication/willterminatemessage.md)

## Relationships

### Inherits From
- [UIResponder](uiresponder.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [Managing your app’s life cycle](managing-your-app-s-life-cycle.md)
  Respond to system notifications when your app is in the foreground or background, and handle other significant system-related events.
- [Responding to the launch of your app](responding-to-the-launch-of-your-app.md)
  Initialize your app’s data structures, prepare your app to run, and respond to any launch-time requests from the system.
- [protocol UIApplicationDelegate](uiapplicationdelegate.md)
  A set of methods to manage shared behaviors for your app.
- [Scenes](scenes.md)
  Manage multiple instances of your app’s UI simultaneously, and direct resources to the appropriate instance of your UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication)*