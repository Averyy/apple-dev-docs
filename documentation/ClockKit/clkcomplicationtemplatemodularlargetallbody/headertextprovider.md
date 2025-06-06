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

A tint color is applied to the header text to differentiate it from the other rows. In multicolor environments, the text provider or template provide the tint color. In monochrome environments, the clock face provides the tint color.

## See Also

- [var bodyTextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargetallbody/bodytextprovider.md)
  The text to display in the body line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargetallbody/headertextprovider)*