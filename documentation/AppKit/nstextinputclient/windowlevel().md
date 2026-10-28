# windowLevel()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the window level of the receiver.

**Availability**:
- macOS

## Declaration

```swift
optional func windowLevel() -> Int
```

```objc
- (NSInteger) windowLevel;
```

## Return Value

The window level of the receiver.

## Discussion

Implementation of this method is optional. A class adopting `NSTextInputClient` can implement this interface to specify its window level if it is higher than `NSFloatingWindowLevel`.

## See Also

### Placing content
- [var documentVisibleRect: NSRect](./documentvisiblerect.md)
- [var unionRectInVisibleSelectedRange: NSRect](./unionrectinvisibleselectedrange.md)
- [func preferredTextAccessoryPlacement() -> NSTextCursorAccessoryPlacement](./preferredtextaccessoryplacement%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/windowlevel())*