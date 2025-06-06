# init(headerTextProvider:body1TextProvider:body2TextProvider:)

**Framework**: ClockKit  
**Kind**: init

Creates a new template that has a row of header text and two rows of body text.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider?)
```

## Parameters

- `headerTextProvider`: The text provider for the header. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `body1TextProvider`: The text provider for the first row of body text. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `body2TextProvider`: The text provider for the second row of body text. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.

## See Also

- [init(headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider)](clkcomplicationtemplatemodularlargestandardbody/init(headertextprovider:body1textprovider:).md)
  Creates a new template that has a row of header text and a row of body text.
- [init(headerImageProvider: CLKImageProvider?, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider)](clkcomplicationtemplatemodularlargestandardbody/init(headerimageprovider:headertextprovider:body1textprovider:).md)
  Creates a new template that has a header row with an image and text, and a row of body text.
- [init(headerImageProvider: CLKImageProvider?, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider?)](clkcomplicationtemplatemodularlargestandardbody/init(headerimageprovider:headertextprovider:body1textprovider:body2textprovider:).md)
  Creates a new template that has a header row with an image and text, and two rows of body text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargestandardbody/init(headertextprovider:body1textprovider:body2textprovider:))*