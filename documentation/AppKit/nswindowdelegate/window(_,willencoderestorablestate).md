# window(_:willEncodeRestorableState:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the window is about to add its restorable state to a given archiver.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func window(_ window: NSWindow, willEncodeRestorableState state: NSCoder)
```

```objc
- (void) window:(NSWindow *) window willEncodeRestorableState:(NSCoder *) state;
```

#### Discussion

This method is called during the window’s [`encodeRestorableState(with:)`](../nsresponder/encoderestorablestate%28with%29.md) method.

## Parameters

- `window`: The window adding its restorable state to an archive.
- `state`: The coder creating the archive.

## See Also

### Managing Restorable State
- [func window(NSWindow, didDecodeRestorableState: NSCoder)](./window%28_,diddecoderestorablestate%29.md)
  Tells the delegate the window is has extracted its restorable state from a given archiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/window(_:willencoderestorablestate:))*