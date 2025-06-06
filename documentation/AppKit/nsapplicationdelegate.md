# NSApplicationDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of methods that manage your app’s life cycle and its interaction with common system services.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSApplicationDelegate : NSObjectProtocol
```

## Topics

### Launching Applications
- [func applicationWillFinishLaunching(Notification)](nsapplicationdelegate/applicationwillfinishlaunching(_:).md)
  Tells the delegate that the app’s initialization is about to complete.
- [func applicationDidFinishLaunching(Notification)](nsapplicationdelegate/applicationdidfinishlaunching(_:).md)
  Tells the delegate that the app’s initialization is complete but it hasn’t received its first event.
- [NSApplicationDidFinishLaunching User Info Keys](nsapplicationdidfinishlaunching-user-info-keys.md)
  The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.
### Managing Active Status
- [func applicationWillBecomeActive(Notification)](nsapplicationdelegate/applicationwillbecomeactive(_:).md)
  Tells the delegate that the app is about to become active.
- [func applicationDidBecomeActive(Notification)](nsapplicationdelegate/applicationdidbecomeactive(_:).md)
  Tells the delegate that the app is now active.
- [func applicationWillResignActive(Notification)](nsapplicationdelegate/applicationwillresignactive(_:).md)
  Tells the delegate that the app is about to become inactive and will lose focus.
- [func applicationDidResignActive(Notification)](nsapplicationdelegate/applicationdidresignactive(_:).md)
  Tells the delegate that the app is no longer active and doesn’t have focus.
### Terminating Applications
- [func applicationShouldTerminate(NSApplication) -> NSApplication.TerminateReply](nsapplicationdelegate/applicationshouldterminate(_:).md)
  Returns a value that indicates if the app should terminate.
- [NSApplication.TerminateReply](nsapplication/terminatereply.md)
  Constants that determine whether an app should terminate.
- [func applicationShouldTerminateAfterLastWindowClosed(NSApplication) -> Bool](nsapplicationdelegate/applicationshouldterminateafterlastwindowclosed(_:).md)
  Returns a Boolean value that indicates if the app terminates once the last window closes.
- [func applicationWillTerminate(Notification)](nsapplicationdelegate/applicationwillterminate(_:).md)
  Tells the delegate that the app is about to terminate.
### Hiding Applications
- [func applicationWillHide(Notification)](nsapplicationdelegate/applicationwillhide(_:).md)
  Tells the delegate that the app is about to be hidden.
- [func applicationDidHide(Notification)](nsapplicationdelegate/applicationdidhide(_:).md)
  Tells the delegate that the app is now hidden.
- [func applicationWillUnhide(Notification)](nsapplicationdelegate/applicationwillunhide(_:).md)
  Tells the delegate that the app is about to become visible.
- [func applicationDidUnhide(Notification)](nsapplicationdelegate/applicationdidunhide(_:).md)
  Tells the delegate that the app is now visible.
### Managing Windows
- [func applicationWillUpdate(Notification)](nsapplicationdelegate/applicationwillupdate(_:).md)
  Tells the delegate that the app is about to update its windows.
- [func applicationDidUpdate(Notification)](nsapplicationdelegate/applicationdidupdate(_:).md)
  Tells the delegate that the app’s windows did update.
- [func applicationShouldHandleReopen(NSApplication, hasVisibleWindows: Bool) -> Bool](nsapplicationdelegate/applicationshouldhandlereopen(_:hasvisiblewindows:).md)
  Returns a Boolean value that indicates if the app responds to reopen AppleEvents.
### Managing the Dock Menu
- [func applicationDockMenu(NSApplication) -> NSMenu?](nsapplicationdelegate/applicationdockmenu(_:).md)
  Returns the app’s dock menu.
### Localizing Keyboard Shortcuts
- [func applicationShouldAutomaticallyLocalizeKeyEquivalents(NSApplication) -> Bool](nsapplicationdelegate/applicationshouldautomaticallylocalizekeyequivalents(_:).md)
  Returns a Boolean value that tells the system whether to remap menu shortcuts to support localized keyboards.
### Displaying Errors
- [func application(NSApplication, willPresentError: any Error) -> any Error](nsapplicationdelegate/application(_:willpresenterror:).md)
  Returns an error for the app to display to the user.
### Managing the Screen
- [func applicationDidChangeScreenParameters(Notification)](nsapplicationdelegate/applicationdidchangescreenparameters(_:).md)
  Tells the delegate about changes to the configuration of any attached displays.
### Continuing User Activities
- [func application(NSApplication, willContinueUserActivityWithType: String) -> Bool](nsapplicationdelegate/application(_:willcontinueuseractivitywithtype:).md)
  Returns a Boolean value that indicates if the app can continue the specified activity.
- [func application(NSApplication, continue: NSUserActivity, restorationHandler: ([any NSUserActivityRestoring]) -> Void) -> Bool](nsapplicationdelegate/application(_:continue:restorationhandler:).md)
  Returns a Boolean value that indicates if the app successfully recreates the specified activity.
- [func application(NSApplication, didFailToContinueUserActivityWithType: String, error: any Error)](nsapplicationdelegate/application(_:didfailtocontinueuseractivitywithtype:error:).md)
  Tells the delegate that the app couldn’t continue the specified activity.
- [func application(NSApplication, didUpdate: NSUserActivity)](nsapplicationdelegate/application(_:didupdate:).md)
  Tells the delegate that there are changes to the specified activity.
### Handling Push Notifications
- [func application(NSApplication, didRegisterForRemoteNotificationsWithDeviceToken: Data)](nsapplicationdelegate/application(_:didregisterforremotenotificationswithdevicetoken:).md)
  Tells the delegate that the app registered for Apple Push Services.
- [func application(NSApplication, didFailToRegisterForRemoteNotificationsWithError: any Error)](nsapplicationdelegate/application(_:didfailtoregisterforremotenotificationswitherror:).md)
  Tells the delegate that the app was unable to register for Apple Push Services.
- [func application(NSApplication, didReceiveRemoteNotification: [String : Any])](nsapplicationdelegate/application(_:didreceiveremotenotification:).md)
  Tells the delegate when the app receives a remote notification.
### Handling CloudKit Invitations
- [func application(NSApplication, userDidAcceptCloudKitShareWith: CKShareMetadata)](nsapplicationdelegate/application(_:userdidacceptcloudkitsharewith:).md)
  Tells the delegate when the user accepts a CloudKit sharing invitation.
### Handling SiriKit Intents
- [func application(NSApplication, handlerFor: INIntent) -> Any?](nsapplicationdelegate/application(_:handlerfor:).md)
  Returns an intent handler that’s capable of handling the specified intent.
### Opening Files
- [func application(NSApplication, open: [URL])](nsapplicationdelegate/application(_:open:).md)
  Tells the delegate to open the resource at the specified URL.
- [func application(NSApplication, openFile: String) -> Bool](nsapplicationdelegate/application(_:openfile:).md)
  Returns a Boolean value that indicates if the app opens the specified file.
- [func application(Any, openFileWithoutUI: String) -> Bool](nsapplicationdelegate/application(_:openfilewithoutui:).md)
  Returns a Boolean value that indicates if the app opens the specified file without showing its user interface.
- [func application(NSApplication, openTempFile: String) -> Bool](nsapplicationdelegate/application(_:opentempfile:).md)
  Returns a Boolean value that indicates if the app opens the specified temporary file.
- [func application(NSApplication, openFiles: [String])](nsapplicationdelegate/application(_:openfiles:).md)
  Tells the delegate to open the specified files.
- [func applicationShouldOpenUntitledFile(NSApplication) -> Bool](nsapplicationdelegate/applicationshouldopenuntitledfile(_:).md)
  Returns a Boolean value that indicates if the app can open an untitled file.
- [func applicationOpenUntitledFile(NSApplication) -> Bool](nsapplicationdelegate/applicationopenuntitledfile(_:).md)
  Returns a Boolean value that indicates if the app opens an untitled file.
### Printing
- [func application(NSApplication, printFile: String) -> Bool](nsapplicationdelegate/application(_:printfile:).md)
  Returns a Boolean value that indicates if the app prints the specified file in its entirety.
- [func application(NSApplication, printFiles: [String], withSettings: [NSPrintInfo.AttributeKey : Any], showPrintPanels: Bool) -> NSApplication.PrintReply](nsapplicationdelegate/application(_:printfiles:withsettings:showprintpanels:).md)
  Returns a value that indicates if the app prints the specified files.
- [NSApplication.PrintReply](nsapplication/printreply.md)
  Constants that indicate the outcome of a print request.
### Restoring Application State
- [func applicationSupportsSecureRestorableState(NSApplication) -> Bool](nsapplicationdelegate/applicationsupportssecurerestorablestate(_:).md)
  Returns a Boolean value that indicates if the app supports secure state restoration.
- [func applicationProtectedDataDidBecomeAvailable(Notification)](nsapplicationdelegate/applicationprotecteddatadidbecomeavailable(_:).md)
  Tells the delegate that protected data is now available.
- [func applicationProtectedDataWillBecomeUnavailable(Notification)](nsapplicationdelegate/applicationprotecteddatawillbecomeunavailable(_:).md)
  Tells the delegate that protected data is about to become unavailable.
- [func application(NSApplication, willEncodeRestorableState: NSCoder)](nsapplicationdelegate/application(_:willencoderestorablestate:).md)
  Tells the delegate that the app is about to encode its restorable state.
- [func application(NSApplication, didDecodeRestorableState: NSCoder)](nsapplicationdelegate/application(_:diddecoderestorablestate:).md)
  Tells the delegate when the app finished decoding its restorable state.
### Handling Changes to the Occlusion State
- [func applicationDidChangeOcclusionState(Notification)](nsapplicationdelegate/applicationdidchangeocclusionstate(_:).md)
  Tells the delegate about changes to the app’s occlusion state.
### Scripting Your App
- [func application(NSApplication, delegateHandlesKey: String) -> Bool](nsapplicationdelegate/application(_:delegatehandleskey:).md)
  Returns a Boolean value that indicates if the app supports the specified scripting key.
### Type Methods
- [static func main()](nsapplicationdelegate/main.md)
  Provides the top-level entry point for the app.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSApplication](nsapplication.md)
  An object that manages an app’s main event loop and resources used by all of that app’s objects.
- [class NSRunningApplication](nsrunningapplication.md)
  An object that can manipulate and provide information for a single instance of an app.
- [func NSApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> Int32](nsapplicationmain(_:_:).md)
  Called by the main function to create and run the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate)*