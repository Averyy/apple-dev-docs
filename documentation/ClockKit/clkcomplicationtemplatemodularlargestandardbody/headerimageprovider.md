# headerImageProvider

**Framework**: ClockKit  
**Kind**: property

An optional image to display in the header.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var headerImageProvider: CLKImageProvider? { get set }
```

#### Discussion

A tint color is applied to the header image to differentiate it from the other rows. In multicolor environments, the image provider or template provide the tint color. In monochrome environments, the clock face provides the tint color.

## See Also

- [var headerTextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargestandardbody/headertextprovider.md)
  The text to display in the header line.
- [var body1TextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargestandardbody/body1textprovider.md)
  The top line of body text.
- [var body2TextProvider: CLKTextProvider?](clkcomplicationtemplatemodularlargestandardbody/body2textprovider.md)
  An optional second line of body text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargestandardbody/headerimageprovider)*