# keyEquivalentFont

**Framework**: AppKit  
**Kind**: property

The font used to draw the button’s key equivalent.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var keyEquivalentFont: NSFont? { get set }
```

#### Discussion

The value of this property is the font object that describes the font used to draw the button’s key equivalent. If the property value is `nil`, the button doesn’t have a key equivalent. Setting this property redraws the button if necessary. Setting this property on a button that has no key equivalent does nothing.

Note that the default font is the same as the font used to draw the title.

## See Also

- [var font: NSFont?](nscell/font.md)
  The font that the cell uses to display text.
- [var gradientType: NSButton.GradientType](nsbuttoncell/gradienttype.md)
  The gradient of the button’s border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/keyequivalentfont)*