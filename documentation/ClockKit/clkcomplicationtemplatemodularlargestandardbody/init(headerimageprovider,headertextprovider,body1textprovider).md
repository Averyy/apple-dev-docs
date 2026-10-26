# init(headerImageProvider:headerTextProvider:body1TextProvider:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a new template that has a header row with an image and text, and a row of body text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```swift
init(headerImageProvider: CLKImageProvider?, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider)
```

```objc
- (instancetype) initWithHeaderImageProvider:(CLKImageProvider *) headerImageProvider headerTextProvider:(CLKTextProvider *) headerTextProvider body1TextProvider:(CLKTextProvider *) body1TextProvider;
```

## Parameters

- `headerImageProvider`: An image provider for the header. The system renders the image as a tinted template image, a bitmap image where only the opacity of the image matters. For more information, see [Providing images for different appearances](../../UIKit/providing-images-for-different-appearances.md).
- `headerTextProvider`: The text provider for the header. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `body1TextProvider`: The text provider for the row of body text. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.

## See Also

### Creating the Template
- [init(headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider)](./init%28headertextprovider,body1textprovider%29.md)
  Creates a new template that has a row of header text and a row of body text.
- [init(headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider?)](./init%28headertextprovider,body1textprovider,body2textprovider%29.md)
  Creates a new template that has a row of header text and two rows of body text.
- [init(headerImageProvider: CLKImageProvider?, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider?)](./init%28headerimageprovider,headertextprovider,body1textprovider,body2textprovider%29.md)
  Creates a new template that has a header row with an image and text, and two rows of body text.
- [+ templateWithHeaderTextProvider:body1TextProvider:](./templatewithheadertextprovider_body1textprovider_.md)
  Returns a new template that has a row of header text and a row of body text.
- [+ templateWithHeaderTextProvider:body1TextProvider:body2TextProvider:](./templatewithheadertextprovider_body1textprovider_body2textprovider_.md)
  Returns a new template that has a row of header text and two rows of body text.
- [+ templateWithHeaderImageProvider:headerTextProvider:body1TextProvider:](./templatewithheaderimageprovider_headertextprovider_body1textprovider_.md)
  Returns a new template that has a header row with an image and text, and a row of body text.
- [+ templateWithHeaderImageProvider:headerTextProvider:body1TextProvider:body2TextProvider:](./templatewithheaderimageprovider_headertextprovider_body1textprovider_body2textprovider_.md)
  Returns a new template that has a header row with an image and text, and two rows of body text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargestandardbody/init(headerimageprovider:headertextprovider:body1textprovider:))*