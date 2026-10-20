# keyEquivalentFont

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The font used to draw the button’s key equivalent.

**Availability**:
- macOS 10.0+ - Deprecated in 10.15

> **Deprecated**: The keyEquivalentFont property is no longer used. It always returns the NSButtonCell's font, and setting it has no effect.

## Declaration

```swift
var keyEquivalentFont: NSFont? { get set }
```

```objc
@property (strong, nullable) NSFont * keyEquivalentFont;
```

#### Discussion

The value of this property is the font object that describes the font used to draw the button’s key equivalent. If the property value is `nil`, the button doesn’t have a key equivalent. Setting this property redraws the button if necessary. Setting this property on a button that has no key equivalent does nothing.

Note that the default font is the same as the font used to draw the title.

## See Also

### Related Documentation
- [var font: NSFont?](../nscell/font.md)
  The font that the cell uses to display text.
### Deprecated properties
- [var gradientType: NSButton.GradientType](./gradienttype.md)
  The gradient of the button’s border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/keyequivalentfont)*