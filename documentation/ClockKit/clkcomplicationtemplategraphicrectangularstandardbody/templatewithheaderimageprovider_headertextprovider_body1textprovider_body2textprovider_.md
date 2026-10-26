# templateWithHeaderImageProvider:headerTextProvider:body1TextProvider:body2TextProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a new template that has a header row with an image and text, and two rows of body text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithHeaderImageProvider:(CLKFullColorImageProvider *) headerImageProvider headerTextProvider:(CLKTextProvider *) headerTextProvider body1TextProvider:(CLKTextProvider *) body1TextProvider body2TextProvider:(CLKTextProvider *) body2TextProvider;
```

## Parameters

- `headerImageProvider`: A full-color image provider.
- `headerTextProvider`: The text provider for the header text. The template supports multicolored text from this text provider.
- `body1TextProvider`: The text provider for the first row of body text. The template supports multicolored text from this text provider.
- `body2TextProvider`: The text provider for the second row of body text. The template supports multicolored text from this text provider.

## See Also

### Creating the Template
- [init(headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider)](./init%28headertextprovider,body1textprovider%29.md)
  Creates a new template that has a row of header text and a row of body text.
- [init(headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider?)](./init%28headertextprovider,body1textprovider,body2textprovider%29.md)
  Creates a new template that has a row of header text and two rows of body text.
- [init(headerImageProvider: CLKFullColorImageProvider?, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider)](./init%28headerimageprovider,headertextprovider,body1textprovider%29.md)
  Creates a new template that has a header row with an image and text, and a row of body text.
- [init(headerImageProvider: CLKFullColorImageProvider?, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider?)](./init%28headerimageprovider,headertextprovider,body1textprovider,body2textprovider%29.md)
  Creates a new template that has a header row with an image and text, and two rows of body text.
- [+ templateWithHeaderTextProvider:body1TextProvider:](./templatewithheadertextprovider_body1textprovider_.md)
  Returns a new template that has a row of header text and a row of body text.
- [+ templateWithHeaderTextProvider:body1TextProvider:body2TextProvider:](./templatewithheadertextprovider_body1textprovider_body2textprovider_.md)
  Returns a new template that has a row of header text and two rows of body text.
- [+ templateWithHeaderImageProvider:headerTextProvider:body1TextProvider:](./templatewithheaderimageprovider_headertextprovider_body1textprovider_.md)
  Returns a new template that has a header row with an image and text, and a row of body text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangularstandardbody/templatewithheaderimageprovider:headertextprovider:body1textprovider:body2textprovider:)*