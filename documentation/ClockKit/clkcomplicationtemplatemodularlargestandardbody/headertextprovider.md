# headerTextProvider

**Framework**: ClockKit  
**Kind**: property

The text to display in the header line.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var headerTextProvider: CLKTextProvider { get set }
```

#### Discussion

The width of the header image determines how much space is available for displaying text. A tint color is applied to the header text to differentiate it from the body text rows. In multicolor environments, the text provider or template provide the tint color. In monochrome environments, the clock face provides the tint color.

## See Also

- [var headerImageProvider: CLKImageProvider?](clkcomplicationtemplatemodularlargestandardbody/headerimageprovider.md)
  An optional image to display in the header.
- [var body1TextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargestandardbody/body1textprovider.md)
  The top line of body text.
- [var body2TextProvider: CLKTextProvider?](clkcomplicationtemplatemodularlargestandardbody/body2textprovider.md)
  An optional second line of body text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargestandardbody/headertextprovider)*