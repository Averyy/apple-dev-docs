# windowLevel()

**Framework**: AppKit  
**Kind**: method

Returns the window level of the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func windowLevel() -> Int
```

#### Return Value

The window level of the receiver.

#### Discussion

Implementation of this method is optional. A class adopting `NSTextInputClient` can implement this interface to specify its window level if it is higher than `NSFloatingWindowLevel`.

## See Also

- [var documentVisibleRect: NSRect](nstextinputclient/documentvisiblerect.md)
- [var unionRectInVisibleSelectedRange: NSRect](nstextinputclient/unionrectinvisibleselectedrange.md)
- [func preferredTextAccessoryPlacement() -> NSTextCursorAccessoryPlacement](nstextinputclient/preferredtextaccessoryplacement.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/windowlevel())*