# isProtectedDataAvailable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 12.0+

## Declaration

```swift
var isProtectedDataAvailable: Bool { get }
```

```objc
@property (readonly, getter=isProtectedDataAvailable) BOOL protectedDataAvailable;
```

## See Also

### Restoring App Windows at Launch
- [func extendStateRestoration()](./extendstaterestoration%28%29.md)
  Allows an app to extend its state restoration period.
- [func completeStateRestoration()](./completestaterestoration%28%29.md)
  Completes the extended state restoration.
- [func restoreWindow(withIdentifier: NSUserInterfaceItemIdentifier, state: NSCoder, completionHandler: (NSWindow?, (any Error)?) -> Void) -> Bool](./restorewindow%28withidentifier,state,completionhandler%29.md)
  Invoked to request that a window be restored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/isprotecteddataavailable)*