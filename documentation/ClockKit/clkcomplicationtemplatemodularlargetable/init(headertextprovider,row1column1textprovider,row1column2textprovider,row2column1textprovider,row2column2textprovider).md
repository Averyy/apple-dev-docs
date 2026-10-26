# init(headerTextProvider:row1Column1TextProvider:row1Column2TextProvider:row2Column1TextProvider:row2Column2TextProvider:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a template that has a header and two columns of text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```swift
init(headerTextProvider: CLKTextProvider, row1Column1TextProvider: CLKTextProvider, row1Column2TextProvider: CLKTextProvider, row2Column1TextProvider: CLKTextProvider, row2Column2TextProvider: CLKTextProvider)
```

```objc
- (instancetype) initWithHeaderTextProvider:(CLKTextProvider *) headerTextProvider row1Column1TextProvider:(CLKTextProvider *) row1Column1TextProvider row1Column2TextProvider:(CLKTextProvider *) row1Column2TextProvider row2Column1TextProvider:(CLKTextProvider *) row2Column1TextProvider row2Column2TextProvider:(CLKTextProvider *) row2Column2TextProvider;
```

## Parameters

- `headerTextProvider`: The text provider for the header. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row1Column1TextProvider`: The text provider for the first row of the first column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row1Column2TextProvider`: The text provider for the first row of the second column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row2Column1TextProvider`: The text provider for the second row of the first column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row2Column2TextProvider`: The text provider for the second row of the second column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.

## See Also

### Creating the Template
- [init(headerImageProvider: CLKImageProvider?, headerTextProvider: CLKTextProvider, row1Column1TextProvider: CLKTextProvider, row1Column2TextProvider: CLKTextProvider, row2Column1TextProvider: CLKTextProvider, row2Column2TextProvider: CLKTextProvider)](./init%28headerimageprovider,headertextprovider,row1column1textprovider,row1column2textprovider,row2column1textprovider,row2column2textprovider%29.md)
  Creates a template that has a header row with an image and text, and two columns of text.
- [+ templateWithHeaderTextProvider:row1Column1TextProvider:row1Column2TextProvider:row2Column1TextProvider:row2Column2TextProvider:](./templatewithheadertextprovider_row1column1textprovider_row1column2textprovider_row2column1textprovider_row2column2textprovider_.md)
  Returns a template that has a header and two columns of text.
- [+ templateWithHeaderImageProvider:headerTextProvider:row1Column1TextProvider:row1Column2TextProvider:row2Column1TextProvider:row2Column2TextProvider:](./templatewithheaderimageprovider_headertextprovider_row1column1textprovider_row1column2textprovider_row2column1textprovider_row2column2textprovider_.md)
  Returns a template that has a header row with an image and text, and two columns of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargetable/init(headertextprovider:row1column1textprovider:row1column2textprovider:row2column1textprovider:row2column2textprovider:))*