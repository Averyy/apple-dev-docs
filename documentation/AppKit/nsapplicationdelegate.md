# NSApplicationDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that manage your app’s life cycle and its interaction with common system services.

**Availability**:
- macOS

## Declaration

```swift
protocol NSApplicationDelegate : NSObjectProtocol
```

```objc
@protocol NSApplicationDelegate <NSObject>
```

## Topics

### Launching Applications
- [func applicationWillFinishLaunching(Notification)](./nsapplicationdelegate/applicationwillfinishlaunching%28_%29.md)
  Tells the delegate that the app’s initialization is about to complete.
- [func applicationDidFinishLaunching(Notification)](./nsapplicationdelegate/applicationdidfinishlaunching%28_%29.md)
  Tells the delegate that the app’s initialization is complete but it hasn’t received its first event.
- [NSApplicationDidFinishLaunching User Info Keys](./nsapplicationdidfinishlaunching-user-info-keys.md)
  The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.
### Managing Active Status
- [func applicationWillBecomeActive(Notification)](./nsapplicationdelegate/applicationwillbecomeactive%28_%29.md)
  Tells the delegate that the app is about to become active.
- [func applicationDidBecomeActive(Notification)](./nsapplicationdelegate/applicationdidbecomeactive%28_%29.md)
  Tells the delegate that the app is now active.
- [func applicationWillResignActive(Notification)](./nsapplicationdelegate/applicationwillresignactive%28_%29.md)
  Tells the delegate that the app is about to become inactive and will lose focus.
- [func applicationDidResignActive(Notification)](./nsapplicationdelegate/applicationdidresignactive%28_%29.md)
  Tells the delegate that the app is no longer active and doesn’t have focus.
### Terminating Applications
- [func applicationShouldTerminate(NSApplication) -> NSApplication.TerminateReply](./nsapplicationdelegate/applicationshouldterminate%28_%29.md)
  Returns a value that indicates if the app should terminate.
- [NSApplication.TerminateReply](./nsapplication/terminatereply.md)
  Constants that determine whether an app should terminate.
- [func applicationShouldTerminateAfterLastWindowClosed(NSApplication) -> Bool](./nsapplicationdelegate/applicationshouldterminateafterlastwindowclosed%28_%29.md)
  Returns a Boolean value that indicates if the app terminates once the last window closes.
- [func applicationWillTerminate(Notification)](./nsapplicationdelegate/applicationwillterminate%28_%29.md)
  Tells the delegate that the app is about to terminate.
### Hiding Applications
- [func applicationWillHide(Notification)](./nsapplicationdelegate/applicationwillhide%28_%29.md)
  Tells the delegate that the app is about to be hidden.
- [func applicationDidHide(Notification)](./nsapplicationdelegate/applicationdidhide%28_%29.md)
  Tells the delegate that the app is now hidden.
- [func applicationWillUnhide(Notification)](./nsapplicationdelegate/applicationwillunhide%28_%29.md)
  Tells the delegate that the app is about to become visible.
- [func applicationDidUnhide(Notification)](./nsapplicationdelegate/applicationdidunhide%28_%29.md)
  Tells the delegate that the app is now visible.
### Managing Windows
- [func applicationWillUpdate(Notification)](./nsapplicationdelegate/applicationwillupdate%28_%29.md)
  Tells the delegate that the app is about to update its windows.
- [func applicationDidUpdate(Notification)](./nsapplicationdelegate/applicationdidupdate%28_%29.md)
  Tells the delegate that the app’s windows did update.
- [func applicationShouldHandleReopen(NSApplication, hasVisibleWindows: Bool) -> Bool](./nsapplicationdelegate/applicationshouldhandlereopen%28_,hasvisiblewindows%29.md)
  Returns a Boolean value that indicates if the app responds to reopen AppleEvents.
### Managing the Dock Menu
- [func applicationDockMenu(NSApplication) -> NSMenu?](./nsapplicationdelegate/applicationdockmenu%28_%29.md)
  Returns the app’s dock menu.
### Localizing Keyboard Shortcuts
- [func applicationShouldAutomaticallyLocalizeKeyEquivalents(NSApplication) -> Bool](./nsapplicationdelegate/applicationshouldautomaticallylocalizekeyequivalents%28_%29.md)
  Returns a Boolean value that tells the system whether to remap menu shortcuts to support localized keyboards.
### Displaying Errors
- [func application(NSApplication, willPresentError: any Error) -> any Error](./nsapplicationdelegate/application%28_,willpresenterror%29.md)
  Returns an error for the app to display to the user.
### Managing the Screen
- [func applicationDidChangeScreenParameters(Notification)](./nsapplicationdelegate/applicationdidchangescreenparameters%28_%29.md)
  Tells the delegate about changes to the configuration of any attached displays.
### Continuing User Activities
- [func application(NSApplication, willContinueUserActivityWithType: String) -> Bool](./nsapplicationdelegate/application%28_,willcontinueuseractivitywithtype%29.md)
  Returns a Boolean value that indicates if the app can continue the specified activity.
- [func application(NSApplication, continue: NSUserActivity, restorationHandler: ([any NSUserActivityRestoring]) -> Void) -> Bool](./nsapplicationdelegate/application%28_,continue,restorationhandler%29.md)
  Returns a Boolean value that indicates if the app successfully recreates the specified activity.
- [func application(NSApplication, didFailToContinueUserActivityWithType: String, error: any Error)](./nsapplicationdelegate/application%28_,didfailtocontinueuseractivitywithtype,error%29.md)
  Tells the delegate that the app couldn’t continue the specified activity.
- [func application(NSApplication, didUpdate: NSUserActivity)](./nsapplicationdelegate/application%28_,didupdate%29.md)
  Tells the delegate that there are changes to the specified activity.
### Handling Push Notifications
- [func application(NSApplication, didRegisterForRemoteNotificationsWithDeviceToken: Data)](./nsapplicationdelegate/application%28_,didregisterforremotenotificationswithdevicetoken%29.md)
  Tells the delegate that the app registered for Apple Push Services.
- [func application(NSApplication, didFailToRegisterForRemoteNotificationsWithError: any Error)](./nsapplicationdelegate/application%28_,didfailtoregisterforremotenotificationswitherror%29.md)
  Tells the delegate that the app was unable to register for Apple Push Services.
- [func application(NSApplication, didReceiveRemoteNotification: [String : Any])](./nsapplicationdelegate/application%28_,didreceiveremotenotification%29.md)
  Tells the delegate when the app receives a remote notification.
### Handling CloudKit Invitations
- [func application(NSApplication, userDidAcceptCloudKitShareWith: CKShareMetadata)](./nsapplicationdelegate/application%28_,userdidacceptcloudkitsharewith%29.md)
  Tells the delegate when the user accepts a CloudKit sharing invitation.
### Handling SiriKit Intents
- [func application(NSApplication, handlerFor: INIntent) -> Any?](./nsapplicationdelegate/application%28_,handlerfor%29.md)
  Returns an intent handler that’s capable of handling the specified intent.
### Opening Files
- [func application(NSApplication, open: [URL])](./nsapplicationdelegate/application%28_,open%29.md)
  Tells the delegate to open the resource at the specified URL.
- [func application(NSApplication, openFile: String) -> Bool](./nsapplicationdelegate/application%28_,openfile%29.md)
  Returns a Boolean value that indicates if the app opens the specified file.
- [func application(Any, openFileWithoutUI: String) -> Bool](./nsapplicationdelegate/application%28_,openfilewithoutui%29.md)
  Returns a Boolean value that indicates if the app opens the specified file without showing its user interface.
- [func application(NSApplication, openTempFile: String) -> Bool](./nsapplicationdelegate/application%28_,opentempfile%29.md)
  Returns a Boolean value that indicates if the app opens the specified temporary file.
- [func application(NSApplication, openFiles: [String])](./nsapplicationdelegate/application%28_,openfiles%29.md)
  Tells the delegate to open the specified files.
- [func applicationShouldOpenUntitledFile(NSApplication) -> Bool](./nsapplicationdelegate/applicationshouldopenuntitledfile%28_%29.md)
  Returns a Boolean value that indicates if the app can open an untitled file.
- [func applicationOpenUntitledFile(NSApplication) -> Bool](./nsapplicationdelegate/applicationopenuntitledfile%28_%29.md)
  Returns a Boolean value that indicates if the app opens an untitled file.
### Printing
- [func application(NSApplication, printFile: String) -> Bool](./nsapplicationdelegate/application%28_,printfile%29.md)
  Returns a Boolean value that indicates if the app prints the specified file in its entirety.
- [func application(NSApplication, printFiles: [String], withSettings: [NSPrintInfo.AttributeKey : Any], showPrintPanels: Bool) -> NSApplication.PrintReply](./nsapplicationdelegate/application%28_,printfiles,withsettings,showprintpanels%29.md)
  Returns a value that indicates if the app prints the specified files.
- [NSApplication.PrintReply](./nsapplication/printreply.md)
  Constants that indicate the outcome of a print request.
### Restoring Application State
- [func applicationSupportsSecureRestorableState(NSApplication) -> Bool](./nsapplicationdelegate/applicationsupportssecurerestorablestate%28_%29.md)
  Returns a Boolean value that indicates if the app supports secure state restoration.
- [func applicationProtectedDataDidBecomeAvailable(Notification)](./nsapplicationdelegate/applicationprotecteddatadidbecomeavailable%28_%29.md)
  Tells the delegate that protected data is now available.
- [func applicationProtectedDataWillBecomeUnavailable(Notification)](./nsapplicationdelegate/applicationprotecteddatawillbecomeunavailable%28_%29.md)
  Tells the delegate that protected data is about to become unavailable.
- [func application(NSApplication, willEncodeRestorableState: NSCoder)](./nsapplicationdelegate/application%28_,willencoderestorablestate%29.md)
  Tells the delegate that the app is about to encode its restorable state.
- [func application(NSApplication, didDecodeRestorableState: NSCoder)](./nsapplicationdelegate/application%28_,diddecoderestorablestate%29.md)
  Tells the delegate when the app finished decoding its restorable state.
### Handling Changes to the Occlusion State
- [func applicationDidChangeOcclusionState(Notification)](./nsapplicationdelegate/applicationdidchangeocclusionstate%28_%29.md)
  Tells the delegate about changes to the app’s occlusion state.
### Scripting Your App
- [func application(NSApplication, delegateHandlesKey: String) -> Bool](./nsapplicationdelegate/application%28_,delegatehandleskey%29.md)
  Returns a Boolean value that indicates if the app supports the specified scripting key.
### Type Methods
- [static func main()](./nsapplicationdelegate/main%28%29.md)
  Provides the top-level entry point for the app.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Life Cycle
- [class NSApplication](./nsapplication.md)
  An object that manages an app’s main event loop and resources used by all of that app’s objects.
- [class NSRunningApplication](./nsrunningapplication.md)
  An object that can manipulate and provide information for a single instance of an app.
- [func NSApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> Int32](./nsapplicationmain%28_,_%29.md)
  Called by the main function to create and run the application.
- [Managing ongoing background processes in your Mac](./managing-ongoing-background-processes-in-your-mac.md)
  Configure your app to help people understand when background processes may continue after they close your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate)*