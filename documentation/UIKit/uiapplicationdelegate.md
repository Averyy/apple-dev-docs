# UIApplicationDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of methods to manage shared behaviors for your app.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIApplicationDelegate : NSObjectProtocol
```

#### Overview

Your app delegate object manages your app’s shared behaviors. The app delegate is effectively the root object of your app, and it works in conjunction with [`UIApplication`](uiapplication.md) to manage some interactions with the system. Like the [`UIApplication`](uiapplication.md) object, UIKit creates your app delegate object early in your app’s launch cycle so it’s always present.

Use your app delegate object to handle the following tasks:

- Initializing your app’s central data structures
- Configuring your app’s scenes
- Responding to notifications originating from outside the app, such as low-memory warnings, download completion notifications, and more
- Responding to events that target the app itself, and aren’t specific to your app’s scenes, views, or view controllers
- Registering for any required services at launch time, such as Apple Push Notification service

For more information about how you use the app delegate object to initialize your app at launch time, see [`Responding to the launch of your app`](responding-to-the-launch-of-your-app.md).

##### Life Cycle Management in Ios 12 and Earlier

In iOS 12 and earlier, you use your app delegate to manage major life cycle events in your app. Specifically, you use methods of the app delegate to update the state of your app when it enters the foreground or moves to the background.

- For information on what to do when your app enters the foreground, see [`Preparing your UI to run in the foreground`](preparing-your-ui-to-run-in-the-foreground.md).
- For information on what to do when your app enters the background, see [`Preparing your UI to run in the background`](preparing-your-ui-to-run-in-the-background.md).
- For general information about the life cycle of your app, see [`Managing your app’s life cycle`](managing-your-app-s-life-cycle.md).

## Topics

### Initializing the app
- [func application(UIApplication, willFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md)
  Tells the delegate that the launch process has begun.
- [func application(UIApplication, didFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md)
  Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey.md)
  The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.
- [class let didFinishLaunchingNotification: NSNotification.Name](uiapplication/didfinishlaunchingnotification.md)
  A notification that posts immediately after the app finishes launching.
### Configuring and discarding scenes
- [func application(UIApplication, configurationForConnecting: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration](uiapplicationdelegate/application(_:configurationforconnecting:options:).md)
  Retrieves the configuration data for UIKit to use when creating a new scene.
- [func application(UIApplication, didDiscardSceneSessions: Set<UISceneSession>)](uiapplicationdelegate/application(_:diddiscardscenesessions:).md)
  Tells the delegate that the user closed one or more of the app’s scenes from the app switcher.
### Responding to app life-cycle events
- [func applicationDidBecomeActive(UIApplication)](uiapplicationdelegate/applicationdidbecomeactive(_:).md)
  Tells the delegate that the app has become active.
- [func applicationWillResignActive(UIApplication)](uiapplicationdelegate/applicationwillresignactive(_:).md)
  Tells the delegate that the app is about to become inactive.
- [func applicationDidEnterBackground(UIApplication)](uiapplicationdelegate/applicationdidenterbackground(_:).md)
  Tells the delegate that the app is now in the background.
- [func applicationWillEnterForeground(UIApplication)](uiapplicationdelegate/applicationwillenterforeground(_:).md)
  Tells the delegate that the app is about to enter the foreground.
- [func applicationWillTerminate(UIApplication)](uiapplicationdelegate/applicationwillterminate(_:).md)
  Tells the delegate when the app is about to terminate.
- [class let didBecomeActiveNotification: NSNotification.Name](uiapplication/didbecomeactivenotification.md)
  A notification that posts when the app becomes active.
- [class let didEnterBackgroundNotification: NSNotification.Name](uiapplication/didenterbackgroundnotification.md)
  A notification that posts when the app enters the background.
- [class let willEnterForegroundNotification: NSNotification.Name](uiapplication/willenterforegroundnotification.md)
  A notification that posts shortly before an app leaves the background state on its way to becoming the active app.
- [class let willResignActiveNotification: NSNotification.Name](uiapplication/willresignactivenotification.md)
  A notification that posts when the app is no longer active and loses focus.
- [class let willTerminateNotification: NSNotification.Name](uiapplication/willterminatenotification.md)
  A notification that posts when the app is about to terminate.
### Responding to environment changes
- [func applicationProtectedDataDidBecomeAvailable(UIApplication)](uiapplicationdelegate/applicationprotecteddatadidbecomeavailable(_:).md)
  Tells the delegate that protected files are available now.
- [func applicationProtectedDataWillBecomeUnavailable(UIApplication)](uiapplicationdelegate/applicationprotecteddatawillbecomeunavailable(_:).md)
  Tells the delegate that the protected files are about to become unavailable.
- [func applicationDidReceiveMemoryWarning(UIApplication)](uiapplicationdelegate/applicationdidreceivememorywarning(_:).md)
  Tells the delegate when the app receives a memory warning from the system.
- [func applicationSignificantTimeChange(UIApplication)](uiapplicationdelegate/applicationsignificanttimechange(_:).md)
  Tells the delegate when there is a significant change in the time.
- [class let protectedDataDidBecomeAvailableNotification: NSNotification.Name](uiapplication/protecteddatadidbecomeavailablenotification.md)
  A notification that posts when the protected files become available for your code to access.
- [class let protectedDataWillBecomeUnavailableNotification: NSNotification.Name](uiapplication/protecteddatawillbecomeunavailablenotification.md)
  A notification that posts shortly before protected files are locked down and become inaccessible.
- [class let didReceiveMemoryWarningNotification: NSNotification.Name](uiapplication/didreceivememorywarningnotification.md)
  A notification that posts when the app receives a warning from the operating system about low memory availability.
- [class let significantTimeChangeNotification: NSNotification.Name](uiapplication/significanttimechangenotification.md)
  A notification that posts when there’s a significant change in time.
### Managing app state restoration
- [func application(UIApplication, shouldSaveSecureApplicationState: NSCoder) -> Bool](uiapplicationdelegate/application(_:shouldsavesecureapplicationstate:).md)
  Asks the delegate whether to securely preserve the app’s state.
- [func application(UIApplication, shouldRestoreSecureApplicationState: NSCoder) -> Bool](uiapplicationdelegate/application(_:shouldrestoresecureapplicationstate:).md)
  Asks the delegate whether to restore the app’s saved state.
- [func application(UIApplication, viewControllerWithRestorationIdentifierPath: [String], coder: NSCoder) -> UIViewController?](uiapplicationdelegate/application(_:viewcontrollerwithrestorationidentifierpath:coder:).md)
  Asks the delegate to provide the specified view controller.
- [func application(UIApplication, willEncodeRestorableStateWith: NSCoder)](uiapplicationdelegate/application(_:willencoderestorablestatewith:).md)
  Tells your delegate to save any high-level state information at the beginning of the state preservation process.
- [func application(UIApplication, didDecodeRestorableStateWith: NSCoder)](uiapplicationdelegate/application(_:diddecoderestorablestatewith:).md)
  Tells your delegate to restore any high-level state information as part of the state restoration process.
- [class let stateRestorationBundleVersionKey: String](uiapplication/staterestorationbundleversionkey.md)
  The version of your app responsible for creating the restoration archive.
- [class let stateRestorationSystemVersionKey: String](uiapplication/staterestorationsystemversionkey.md)
  The version of the system on which your app created the restoration archive.
- [class let stateRestorationTimestampKey: String](uiapplication/staterestorationtimestampkey.md)
  The time your app created the restoration archive.
- [class let stateRestorationUserInterfaceIdiomKey: String](uiapplication/staterestorationuserinterfaceidiomkey.md)
  The user interface idiom that was in effect when your app created the restoration archive.
- [class let stateRestorationViewControllerStoryboardKey: String](uiapplication/staterestorationviewcontrollerstoryboardkey.md)
  A reference to the storyboard that contains the view controller.
### Downloading data in the background
- [func application(UIApplication, handleEventsForBackgroundURLSession: String, completionHandler: () -> Void)](uiapplicationdelegate/application(_:handleeventsforbackgroundurlsession:completionhandler:).md)
  Tells the delegate that events related to a URL session are waiting to be processed.
- [enum UIBackgroundFetchResult](uibackgroundfetchresult.md)
  Constants that indicate the result of a background fetch operation.
### Handling remote notification registration
- [func application(UIApplication, didRegisterForRemoteNotificationsWithDeviceToken: Data)](uiapplicationdelegate/application(_:didregisterforremotenotificationswithdevicetoken:).md)
  Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [func application(UIApplication, didFailToRegisterForRemoteNotificationsWithError: any Error)](uiapplicationdelegate/application(_:didfailtoregisterforremotenotificationswitherror:).md)
  Tells the delegate when Apple Push Notification service cannot successfully complete the registration process.
- [func application(UIApplication, didReceiveRemoteNotification: [AnyHashable : Any], fetchCompletionHandler: (UIBackgroundFetchResult) -> Void)](uiapplicationdelegate/application(_:didreceiveremotenotification:fetchcompletionhandler:).md)
  Tells the app that a remote notification arrived that indicates there is data to be fetched.
### Continuing user activity and handling quick actions
- [func application(UIApplication, willContinueUserActivityWithType: String) -> Bool](uiapplicationdelegate/application(_:willcontinueuseractivitywithtype:).md)
  Tells the delegate if your app takes responsibility for notifying users when a continuation activity takes longer than expected.
- [func application(UIApplication, continue: NSUserActivity, restorationHandler: ([any UIUserActivityRestoring]?) -> Void) -> Bool](uiapplicationdelegate/application(_:continue:restorationhandler:).md)
  Tells the delegate that the data for continuing an activity is available.
- [func application(UIApplication, didUpdate: NSUserActivity)](uiapplicationdelegate/application(_:didupdate:).md)
  Tells the delegate that the activity was updated.
- [func application(UIApplication, didFailToContinueUserActivityWithType: String, error: any Error)](uiapplicationdelegate/application(_:didfailtocontinueuseractivitywithtype:error:).md)
  Tells the delegate that the activity couldn’t be continued.
- [func application(UIApplication, performActionFor: UIApplicationShortcutItem, completionHandler: (Bool) -> Void)](uiapplicationdelegate/application(_:performactionfor:completionhandler:).md)
  Tells the delegate that the user selected a Home screen quick action for your app, except when you’ve intercepted the interaction in a launch method.
### Interacting with WatchKit
- [func application(UIApplication, handleWatchKitExtensionRequest: [AnyHashable : Any]?, reply: ([AnyHashable : Any]?) -> Void)](uiapplicationdelegate/application(_:handlewatchkitextensionrequest:reply:).md)
  Asks the delegate to respond to a request from a paired watchOS app.
### Interacting with HealthKit
- [func applicationShouldRequestHealthAuthorization(UIApplication)](uiapplicationdelegate/applicationshouldrequesthealthauthorization(_:).md)
  Tells the delegate when your app should ask the user for access to his or her HealthKit data.
### Opening a URL-specified resource
- [func application(UIApplication, open: URL, options: [UIApplication.OpenURLOptionsKey : Any]) -> Bool](uiapplicationdelegate/application(_:open:options:).md)
  Asks the delegate to open a resource specified by a URL, and provides a dictionary of launch options.
- [UIApplication.OpenURLOptionsKey](uiapplication/openurloptionskey.md)
  Keys you use to access values in the options dictionary when opening a URL.
### Disallowing specified app extension types
- [func application(UIApplication, shouldAllowExtensionPointIdentifier: UIApplication.ExtensionPointIdentifier) -> Bool](uiapplicationdelegate/application(_:shouldallowextensionpointidentifier:).md)
  Asks the delegate to grant permission to use app extensions that are based on a specified extension point identifier.
- [UIApplication.ExtensionPointIdentifier](uiapplication/extensionpointidentifier.md)
  A structure that identifies types of extensions.
- [static let keyboard: UIApplication.ExtensionPointIdentifier](uiapplication/extensionpointidentifier/keyboard.md)
  The identifier for custom keyboards.
### Handling SiriKit intents
- [func application(UIApplication, handlerFor: INIntent) -> Any?](uiapplicationdelegate/application(_:handlerfor:).md)
  Asks the delegate for an intent handler capable of handling the specified intent.
### Handling CloudKit invitations
- [func application(UIApplication, userDidAcceptCloudKitShareWith: CKShareMetadata)](uiapplicationdelegate/application(_:userdidacceptcloudkitsharewith:).md)
  Tells the delegate that the app now has access to shared information in CloudKit.
### Localizing keyboard shortcuts
- [func applicationShouldAutomaticallyLocalizeKeyCommands(UIApplication) -> Bool](uiapplicationdelegate/applicationshouldautomaticallylocalizekeycommands(_:).md)
  Returns a Boolean value that tells the system whether to remap menu shortcuts to support localized keyboards.
### Managing interface geometry
- [func application(UIApplication, supportedInterfaceOrientationsFor: UIWindow?) -> UIInterfaceOrientationMask](uiapplicationdelegate/application(_:supportedinterfaceorientationsfor:).md)
  Asks the delegate for the interface orientations to use for the view controllers in the specified window.
- [enum UIInterfaceOrientation](uiinterfaceorientation.md)
  Constants that specify the orientation of the app’s user interface.
- [struct UIInterfaceOrientationMask](uiinterfaceorientationmask.md)
  Constants that specify a view controller’s supported interface orientations.
- [class let invalidInterfaceOrientationException: NSExceptionName](uiapplication/invalidinterfaceorientationexception.md)
  An exception that’s thrown if a view controller or the app returns an invalid set of supported interface orientations.
### Providing a window for storyboarding
- [var window: UIWindow?](uiapplicationdelegate/window.md)
  The window to use when presenting a storyboard.
### Providing the main entry point
- [static func main()](uiapplicationdelegate/main.md)
  Provides the top-level entry point for the app.
### Deprecated
- [func applicationDidFinishLaunching(UIApplication)](uiapplicationdelegate/applicationdidfinishlaunching(_:).md)
  Tells the delegate when the app has finished launching.
- [Deprecated symbols](uiapplicationdelegate-deprecated-symbols.md)
  Symbols that are no longer supported.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Managing your app’s life cycle](managing-your-app-s-life-cycle.md)
  Respond to system notifications when your app is in the foreground or background, and handle other significant system-related events.
- [Responding to the launch of your app](responding-to-the-launch-of-your-app.md)
  Initialize your app’s data structures, prepare your app to run, and respond to any launch-time requests from the system.
- [class UIApplication](uiapplication.md)
  The centralized point of control and coordination for apps running in iOS.
- [Scenes](scenes.md)
  Manage multiple instances of your app’s UI simultaneously, and direct resources to the appropriate instance of your UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate)*