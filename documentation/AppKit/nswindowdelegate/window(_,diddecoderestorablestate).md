# window(_:didDecodeRestorableState:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the window is has extracted its restorable state from a given archiver.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func window(_ window: NSWindow, didDecodeRestorableState state: NSCoder)
```

```objc
- (void) window:(NSWindow *) window didDecodeRestorableState:(NSCoder *) state;
```

## Discussion

This method is called during the window’s [`restoreState(with:)`](../nsresponder/restorestate%28with%29.md) method.

## Parameters

- `window`: The window extracting its restorable state from an archive.
- `state`: The coder extracting the archive.

## See Also

### Managing Restorable State
- [func window(NSWindow, willEncodeRestorableState: NSCoder)](./window%28_,willencoderestorablestate%29.md)
  Tells the delegate the window is about to add its restorable state to a given archiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/window(_:diddecoderestorablestate:))*