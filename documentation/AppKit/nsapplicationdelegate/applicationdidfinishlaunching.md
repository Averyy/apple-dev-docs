# applicationDidFinishLaunching(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the app’s initialization is complete but it hasn’t received its first event.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationDidFinishLaunching(_ notification: Notification)
```

#### Discussion

Delegates can implement this method to perform further initialization. This method is called after the application’s main run loop has been started but before it has processed any events. If the application was launched by the user opening a file, the delegate’s  [`application(_:openFile:)`](nsapplicationdelegate/application(_:openfile:).md) method is called before this method. If you want to perform initialization before any files are opened, implement the [`applicationWillFinishLaunching(_:)`](nsapplicationdelegate/applicationwillfinishlaunching(_:).md) method in your delegate, which is called before [`application(_:openFile:)`](nsapplicationdelegate/application(_:openfile:).md).)

## Parameters

- `notification`: A notification named  . Calling the   method of this notification returns the   object itself.

## See Also

- [func finishLaunching()](nsapplication/finishlaunching.md)
  Activates the app, opens any files specified by the `NSOpen` user default, and unhighlights the app’s icon.
- [func application(NSApplication, openFile: String) -> Bool](nsapplicationdelegate/application(_:openfile:).md)
  Returns a Boolean value that indicates if the app opens the specified file.
- [func applicationDidBecomeActive(Notification)](nsapplicationdelegate/applicationdidbecomeactive(_:).md)
  Tells the delegate that the app is now active.
- [func applicationWillFinishLaunching(Notification)](nsapplicationdelegate/applicationwillfinishlaunching(_:).md)
  Tells the delegate that the app’s initialization is about to complete.
- [NSApplicationDidFinishLaunching User Info Keys](nsapplicationdidfinishlaunching-user-info-keys.md)
  The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationdidfinishlaunching(_:))*