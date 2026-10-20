# preferredTextFieldWidth()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The preferred width of the form’s cells when using Auto Layout.

**Availability**:
- macOS 10.8+ - Deprecated in 10.10

## Declaration

```swift
func preferredTextFieldWidth() -> CGFloat
```

```objc
- (CGFloat) preferredTextFieldWidth;
```

#### Return Value

The field’s width.

#### Discussion

If the width is negative, the [`cellSize`](../nscell/cellsize.md) matches the historic behavior, which is that it is large enough to accommodate the title, bezel, and the current text.

The default is -1.

## See Also

### Auto Layout Sizing
- [func setPreferredTextFieldWidth(CGFloat)](./setpreferredtextfieldwidth%28_%29.md)
  Sets the preferred text field width used by Auto Layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/preferredtextfieldwidth())*