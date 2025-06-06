# preferredTextFieldWidth()

**Framework**: AppKit  
**Kind**: method

The preferred width of the form’s cells when using Auto Layout.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
func preferredTextFieldWidth() -> CGFloat
```

#### Return Value

The field’s width.

#### Discussion

If the width is negative, the [`cellSize`](nscell/cellsize.md) matches the historic behavior, which is that it is large enough to accommodate the title, bezel, and the current text.

The default is -1.

## See Also

- [func setPreferredTextFieldWidth(CGFloat)](nsform/setpreferredtextfieldwidth(_:).md)
  Sets the preferred text field width used by Auto Layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/preferredtextfieldwidth())*