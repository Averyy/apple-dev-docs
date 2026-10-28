# applicationDidFinishLaunching(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app’s initialization is complete but it hasn’t received its first event.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationDidFinishLaunching(_ notification: Notification)
```

```objc
- (void) applicationDidFinishLaunching:(NSNotification *) notification;
```

## Discussion

Delegates can implement this method to perform further initialization. This method is called after the application’s main run loop has been started but before it has processed any events. If the application was launched by the user opening a file, the delegate’s  [`application(_:openFile:)`](./application%28_,openfile%29.md) method is called before this method. If you want to perform initialization before any files are opened, implement the [`applicationWillFinishLaunching(_:)`](./applicationwillfinishlaunching%28_%29.md) method in your delegate, which is called before [`application(_:openFile:)`](./application%28_,openfile%29.md).)

## Parameters

- `notification`: A notification named [`didFinishLaunchingNotification`](../nsapplication/didfinishlaunchingnotification.md). Calling the [`object`](../../Foundation/nsnotification/object.md) method of this notification returns the `NSApplication` object itself.

## See Also

### Related Documentation
- [func finishLaunching()](../nsapplication/finishlaunching%28%29.md)
  Activates the app, opens any files specified by the `NSOpen` user default, and unhighlights the app’s icon.
- [func application(NSApplication, openFile: String) -> Bool](./application%28_,openfile%29.md)
  Returns a Boolean value that indicates if the app opens the specified file.
- [func applicationDidBecomeActive(Notification)](./applicationdidbecomeactive%28_%29.md)
  Tells the delegate that the app is now active.
### Launching Applications
- [func applicationWillFinishLaunching(Notification)](./applicationwillfinishlaunching%28_%29.md)
  Tells the delegate that the app’s initialization is about to complete.
- [NSApplicationDidFinishLaunching User Info Keys](../nsapplicationdidfinishlaunching-user-info-keys.md)
  The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationdidfinishlaunching(_:))*