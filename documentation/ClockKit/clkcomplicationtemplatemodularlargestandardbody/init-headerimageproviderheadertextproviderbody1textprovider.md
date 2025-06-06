# init(headerImageProvider:headerTextProvider:body1TextProvider:)

**Framework**: ClockKit  
**Kind**: init

Creates a new template that has a header row with an image and text, and a row of body text.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(headerImageProvider: CLKImageProvider?, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider)
```

## Parameters

- `headerImageProvider`: An image provider for the header. The system renders the image as a tinted template image, a bitmap image where only the opacity of the image matters. For more information, see  .
- `headerTextProvider`: The text provider for the header. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `body1TextProvider`: The text provider for the row of body text. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.

## See Also

- [init(headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider)](clkcomplicationtemplatemodularlargestandardbody/init(headertextprovider:body1textprovider:).md)
  Creates a new template that has a row of header text and a row of body text.
- [init(headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider?)](clkcomplicationtemplatemodularlargestandardbody/init(headertextprovider:body1textprovider:body2textprovider:).md)
  Creates a new template that has a row of header text and two rows of body text.
- [init(headerImageProvider: CLKImageProvider?, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider?)](clkcomplicationtemplatemodularlargestandardbody/init(headerimageprovider:headertextprovider:body1textprovider:body2textprovider:).md)
  Creates a new template that has a header row with an image and text, and two rows of body text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargestandardbody/init(headerimageprovider:headertextprovider:body1textprovider:))*