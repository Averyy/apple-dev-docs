# gradientType

**Framework**: AppKit  
**Kind**: property

The gradient of the button’s border.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var gradientType: NSButton.GradientType { get set }
```

#### Discussion

The value of this property is a constant that specifies the gradient used for the button’s border. See [`NSButton.GradientType`](nsbutton/gradienttype.md) for a list of possible values.

If the button has no border, setting this property has no effect on the button’s appearance. A concave gradient is darkest in the top-left corner; a convex gradient is darkest in the bottom-right corner. Weak versus strong is how much contrast exists between the colors used in opposite corners.

> **Note**:  This property is currently unused by AppKit and has no effect.

## See Also

- [var keyEquivalentFont: NSFont?](nsbuttoncell/keyequivalentfont.md)
  The font used to draw the button’s key equivalent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/gradienttype)*