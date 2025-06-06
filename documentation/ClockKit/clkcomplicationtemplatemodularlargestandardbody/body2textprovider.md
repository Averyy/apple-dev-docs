# body2TextProvider

**Framework**: ClockKit  
**Kind**: property

An optional second line of body text.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var body2TextProvider: CLKTextProvider? { get set }
```

#### Discussion

If you don’t specify a value for this property, the text in the [`body1TextProvider`](clkcomplicationtemplatemodularlargestandardbody/body1textprovider.md) property wraps and is displayed on the second line.

## See Also

- [var headerImageProvider: CLKImageProvider?](clkcomplicationtemplatemodularlargestandardbody/headerimageprovider.md)
  An optional image to display in the header.
- [var headerTextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargestandardbody/headertextprovider.md)
  The text to display in the header line.
- [var body1TextProvider: CLKTextProvider](clkcomplicationtemplatemodularlargestandardbody/body1textprovider.md)
  The top line of body text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargestandardbody/body2textprovider)*