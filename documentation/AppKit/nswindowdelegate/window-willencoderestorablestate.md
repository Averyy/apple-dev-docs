# window(_:willEncodeRestorableState:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate the window is about to add its restorable state to a given archiver.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func window(_ window: NSWindow, willEncodeRestorableState state: NSCoder)
```

#### Discussion

This method is called during the window’s [`encodeRestorableState(with:)`](nsresponder/encoderestorablestate(with:).md) method.

## Parameters

- `window`: The window adding its restorable state to an archive.
- `state`: The coder creating the archive.

## See Also

- [func window(NSWindow, didDecodeRestorableState: NSCoder)](nswindowdelegate/window(_:diddecoderestorablestate:).md)
  Tells the delegate the window is has extracted its restorable state from a given archiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/window(_:willencoderestorablestate:))*