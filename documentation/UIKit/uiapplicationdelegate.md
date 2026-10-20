# UIApplicationDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods to manage shared behaviors for your app.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
@MainActor
protocol UIApplicationDelegate : NSObjectProtocol
```

```objc
@protocol UIApplicationDelegate <NSObject>
```

## Mentions

- [Transitioning to the UIKit scene-based life cycle](./transitioning-to-the-uikit-scene-based-life-cycle.md)
- [About app development with UIKit](./about-app-development-with-uikit.md)

#### Overview

Your app delegate object manages your app’s shared behaviors. The app delegate is effectively the root object of your app, and it works in conjunction with [`UIApplication`](./uiapplication.md) to manage some interactions with the system. Like the [`UIApplication`](./uiapplication.md) object, UIKit creates your app delegate object early in your app’s launch cycle so it’s always present.

Use your app delegate object to handle the following tasks:

- Initializing your app’s central data structures
- Configuring your app’s scenes
- Responding to notifications originating from outside the app, such as low-memory warnings, download completion notifications, and more
- Responding to events that target the app itself, and aren’t specific to your app’s scenes, views, or view controllers
- Registering for any required services at launch time, such as Apple Push Notification service

For more information about how you use the app delegate object to initialize your app at launch time, see [Responding to the launch of your app](./responding-to-the-launch-of-your-app.md).

##### Life-cycle management in iOS 12 and earlier

In iOS 12 and earlier, you use your app delegate to manage major life cycle events in your app. Specifically, you use methods of the app delegate to update the state of your app when it enters the foreground or moves to the background.

- For information on what to do when your app enters the foreground, see [Preparing your UI to run in the foreground](./preparing-your-ui-to-run-in-the-foreground.md).
- For information on what to do when your app enters the background, see [Preparing your UI to run in the background](./preparing-your-ui-to-run-in-the-background.md).
- For general information about the life cycle of your app, see [Managing your app’s life cycle](./managing-your-app-s-life-cycle.md).

## Topics

### Initializing the app
- [func application(UIApplication, willFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](./uiapplicationdelegate/application%28_,willfinishlaunchingwithoptions%29.md)
  Tells the delegate that the launch process has begun.
- [func application(UIApplication, didFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](./uiapplicationdelegate/application%28_,didfinishlaunchingwithoptions%29.md)
  Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [UIApplication.LaunchOptionsKey](./uiapplication/launchoptionskey.md)
  The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.
- [class let didFinishLaunchingNotification: NSNotification.Name](./uiapplication/didfinishlaunchingnotification.md)
  A notification that posts immediately after the app finishes launching.
### Configuring and discarding scenes
- [func application(UIApplication, configurationForConnecting: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration](./uiapplicationdelegate/application%28_,configurationforconnecting,options%29.md)
  Retrieves the configuration data for UIKit to use when creating a new scene.
- [func application(UIApplication, didDiscardSceneSessions: Set<UISceneSession>)](./uiapplicationdelegate/application%28_,diddiscardscenesessions%29.md)
  Tells the delegate that the user closed one or more of the app’s scenes from the app switcher.
### Responding to app life-cycle events
- [func applicationDidEnterBackground(UIApplication)](./uiapplicationdelegate/applicationdidenterbackground%28_%29.md)
  Tells the delegate that the app is now in the background.
- [func applicationWillTerminate(UIApplication)](./uiapplicationdelegate/applicationwillterminate%28_%29.md)
  Tells the delegate when the app is about to terminate.
- [class let didBecomeActiveNotification: NSNotification.Name](./uiapplication/didbecomeactivenotification.md)
  A notification that posts when the app becomes active.
- [class let didEnterBackgroundNotification: NSNotification.Name](./uiapplication/didenterbackgroundnotification.md)
  A notification that posts when the app enters the background.
- [class let willEnterForegroundNotification: NSNotification.Name](./uiapplication/willenterforegroundnotification.md)
  A notification that posts shortly before your app’s UI transitions to the foreground.
- [class let willResignActiveNotification: NSNotification.Name](./uiapplication/willresignactivenotification.md)
  A notification that posts when the app is no longer active and loses focus.
- [class let willTerminateNotification: NSNotification.Name](./uiapplication/willterminatenotification.md)
  A notification that posts when the app is about to terminate.
### Responding to environment changes
- [func applicationProtectedDataDidBecomeAvailable(UIApplication)](./uiapplicationdelegate/applicationprotecteddatadidbecomeavailable%28_%29.md)
  Tells the delegate that protected files are available now.
- [func applicationProtectedDataWillBecomeUnavailable(UIApplication)](./uiapplicationdelegate/applicationprotecteddatawillbecomeunavailable%28_%29.md)
  Tells the delegate that the protected files are about to become unavailable.
- [func applicationDidReceiveMemoryWarning(UIApplication)](./uiapplicationdelegate/applicationdidreceivememorywarning%28_%29.md)
  Tells the delegate when the app receives a memory warning from the system.
- [func applicationSignificantTimeChange(UIApplication)](./uiapplicationdelegate/applicationsignificanttimechange%28_%29.md)
  Tells the delegate when there is a significant change in the time.
- [class let protectedDataDidBecomeAvailableNotification: NSNotification.Name](./uiapplication/protecteddatadidbecomeavailablenotification.md)
  A notification that posts when the protected files become available for your code to access.
- [class let protectedDataWillBecomeUnavailableNotification: NSNotification.Name](./uiapplication/protecteddatawillbecomeunavailablenotification.md)
  A notification that posts shortly before protected files are locked down and become inaccessible.
- [class let didReceiveMemoryWarningNotification: NSNotification.Name](./uiapplication/didreceivememorywarningnotification.md)
  A notification that posts when the app receives a warning from the operating system about low memory availability.
- [class let significantTimeChangeNotification: NSNotification.Name](./uiapplication/significanttimechangenotification.md)
  A notification that posts when there’s a significant change in time.
### Managing app state restoration
- [func application(UIApplication, shouldSaveSecureApplicationState: NSCoder) -> Bool](./uiapplicationdelegate/application%28_,shouldsavesecureapplicationstate%29.md)
  Asks the delegate whether to securely preserve the app’s state.
- [func application(UIApplication, shouldRestoreSecureApplicationState: NSCoder) -> Bool](./uiapplicationdelegate/application%28_,shouldrestoresecureapplicationstate%29.md)
  Asks the delegate whether to restore the app’s saved state.
- [func application(UIApplication, viewControllerWithRestorationIdentifierPath: [String], coder: NSCoder) -> UIViewController?](./uiapplicationdelegate/application%28_,viewcontrollerwithrestorationidentifierpath,coder%29.md)
  Asks the delegate to provide the specified view controller.
- [func application(UIApplication, willEncodeRestorableStateWith: NSCoder)](./uiapplicationdelegate/application%28_,willencoderestorablestatewith%29.md)
  Tells your delegate to save any high-level state information at the beginning of the state preservation process.
- [func application(UIApplication, didDecodeRestorableStateWith: NSCoder)](./uiapplicationdelegate/application%28_,diddecoderestorablestatewith%29.md)
  Tells your delegate to restore any high-level state information as part of the state restoration process.
- [class let stateRestorationBundleVersionKey: String](./uiapplication/staterestorationbundleversionkey.md)
  The version of your app responsible for creating the restoration archive.
- [class let stateRestorationSystemVersionKey: String](./uiapplication/staterestorationsystemversionkey.md)
  The version of the system on which your app created the restoration archive.
- [class let stateRestorationTimestampKey: String](./uiapplication/staterestorationtimestampkey.md)
  The time your app created the restoration archive.
- [class let stateRestorationUserInterfaceIdiomKey: String](./uiapplication/staterestorationuserinterfaceidiomkey.md)
  The user interface idiom that was in effect when your app created the restoration archive.
- [class let stateRestorationViewControllerStoryboardKey: String](./uiapplication/staterestorationviewcontrollerstoryboardkey.md)
  A reference to the storyboard that contains the view controller.
### Downloading data in the background
- [func application(UIApplication, handleEventsForBackgroundURLSession: String, completionHandler: () -> Void)](./uiapplicationdelegate/application%28_,handleeventsforbackgroundurlsession,completionhandler%29.md)
  Tells the delegate that events related to a URL session are waiting to be processed.
- [enum UIBackgroundFetchResult](./uibackgroundfetchresult.md)
  Constants that indicate the result of a background fetch operation.
### Handling remote notification registration
- [func application(UIApplication, didRegisterForRemoteNotificationsWithDeviceToken: Data)](./uiapplicationdelegate/application%28_,didregisterforremotenotificationswithdevicetoken%29.md)
  Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [func application(UIApplication, didFailToRegisterForRemoteNotificationsWithError: any Error)](./uiapplicationdelegate/application%28_,didfailtoregisterforremotenotificationswitherror%29.md)
  Tells the delegate when Apple Push Notification service cannot successfully complete the registration process.
- [func application(UIApplication, didReceiveRemoteNotification: [AnyHashable : Any], fetchCompletionHandler: (UIBackgroundFetchResult) -> Void)](./uiapplicationdelegate/application%28_,didreceiveremotenotification,fetchcompletionhandler%29.md)
  Tells the app that a remote notification arrived that indicates there is data to be fetched.
### Interacting with WatchKit
- [func application(UIApplication, handleWatchKitExtensionRequest: [AnyHashable : Any]?, reply: ([AnyHashable : Any]?) -> Void)](./uiapplicationdelegate/application%28_,handlewatchkitextensionrequest,reply%29.md)
  Asks the delegate to respond to a request from a paired watchOS app.
### Interacting with HealthKit
- [func applicationShouldRequestHealthAuthorization(UIApplication)](./uiapplicationdelegate/applicationshouldrequesthealthauthorization%28_%29.md)
  Tells the delegate when your app should ask the user for access to his or her HealthKit data.
### Disallowing specified app extension types
- [func application(UIApplication, shouldAllowExtensionPointIdentifier: UIApplication.ExtensionPointIdentifier) -> Bool](./uiapplicationdelegate/application%28_,shouldallowextensionpointidentifier%29.md)
  Asks the delegate to grant permission to use app extensions that are based on a specified extension point identifier.
- [UIApplication.ExtensionPointIdentifier](./uiapplication/extensionpointidentifier.md)
  A structure that identifies types of extensions.
- [static let keyboard: UIApplication.ExtensionPointIdentifier](./uiapplication/extensionpointidentifier/keyboard.md)
  The identifier for custom keyboards.
### Handling SiriKit intents
- [func application(UIApplication, handlerFor: INIntent) -> Any?](./uiapplicationdelegate/application%28_,handlerfor%29.md)
  Asks the delegate for an intent handler capable of handling the specified intent.
### Localizing keyboard shortcuts
- [func applicationShouldAutomaticallyLocalizeKeyCommands(UIApplication) -> Bool](./uiapplicationdelegate/applicationshouldautomaticallylocalizekeycommands%28_%29.md)
  Returns a Boolean value that tells the system whether to remap menu shortcuts to support localized keyboards.
### Managing interface geometry
- [enum UIInterfaceOrientation](./uiinterfaceorientation.md)
  Constants that specify the orientation of the app’s user interface.
- [struct UIInterfaceOrientationMask](./uiinterfaceorientationmask.md)
  Constants that specify a view controller’s supported interface orientations.
- [class let invalidInterfaceOrientationException: NSExceptionName](./uiapplication/invalidinterfaceorientationexception.md)
  An exception that’s thrown if a view controller or the app returns an invalid set of supported interface orientations.
### Providing a window for storyboarding
- [var window: UIWindow?](./uiapplicationdelegate/window.md)
  The window to use when presenting a storyboard.
### Providing the main entry point
- [static func main()](./uiapplicationdelegate/main%28%29.md)
  Provides the top-level entry point for the app.
### Deprecated
- [func applicationDidFinishLaunching(UIApplication)](./uiapplicationdelegate/applicationdidfinishlaunching%28_%29.md)
  Tells the delegate when the app has finished launching.
- [Deprecated symbols](./uiapplicationdelegate-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Life cycle
- [Managing your app’s life cycle](./managing-your-app-s-life-cycle.md)
  Respond to system notifications when your app is in the foreground or background, and handle other significant system-related events.
- [Responding to the launch of your app](./responding-to-the-launch-of-your-app.md)
  Initialize your app’s data structures, prepare your app to run, and respond to any launch-time requests from the system.
- [class UIApplication](./uiapplication.md)
  The centralized point of control and coordination for apps running in iOS.
- [Scenes](./scenes.md)
  Manage multiple instances of your app’s UI simultaneously, and direct resources to the appropriate instance of your UI.
- [Transitioning to the UIKit scene-based life cycle](./transitioning-to-the-uikit-scene-based-life-cycle.md)
  Adopt the scene-based life cycle to replace the app delegate life cycle in UIKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate)*