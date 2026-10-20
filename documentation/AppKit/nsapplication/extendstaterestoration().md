# extendStateRestoration()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows an app to extend its state restoration period.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func extendStateRestoration()
```

```objc
- (void) extendStateRestoration;
```

#### Discussion

This method allows an app to extend the state restoration period beyond the usual. For example, the app crashes before state restoration is complete, then it may offer to discard restorable state on the next launch.

If a window has some state that may take a long time to restore, such as a web page, you may use this method and methods to [`completeStateRestoration()`](./completestaterestoration%28%29.md) to extend the period of this crash protection beyond the default.

You call `extendStateRestoration` within your implementation of [`restoreWindow(withIdentifier:state:completionHandler:)`](./restorewindow%28withidentifier,state,completionhandler%29.md).  You would then call [`completeStateRestoration()`](./completestaterestoration%28%29.md) some time after the window is fully restored.  If the app crashes in the interim, then it may offer to discard restorable state on the next launch.

The `extendStateRestoration` and [`completeStateRestoration()`](./completestaterestoration%28%29.md) methods act as a counter. Each call to `extendStateRestoration` increments the counter, and must be matched with a corresponding call to [`completeStateRestoration()`](./completestaterestoration%28%29.md) which decrements it.  When the counter reaches zero, the app is considered to have been fully restored, and any further calls are silently ignored.

This method is thread safe.

## See Also

### Restoring App Windows at Launch
- [var isProtectedDataAvailable: Bool](./isprotecteddataavailable.md)
- [func completeStateRestoration()](./completestaterestoration%28%29.md)
  Completes the extended state restoration.
- [func restoreWindow(withIdentifier: NSUserInterfaceItemIdentifier, state: NSCoder, completionHandler: (NSWindow?, (any Error)?) -> Void) -> Bool](./restorewindow%28withidentifier,state,completionhandler%29.md)
  Invoked to request that a window be restored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/extendstaterestoration())*