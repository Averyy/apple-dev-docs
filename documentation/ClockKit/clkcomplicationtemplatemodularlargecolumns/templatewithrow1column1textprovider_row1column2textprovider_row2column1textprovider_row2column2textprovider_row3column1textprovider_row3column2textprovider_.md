# templateWithRow1Column1TextProvider:row1Column2TextProvider:row2Column1TextProvider:row2Column2TextProvider:row3Column1TextProvider:row3Column2TextProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a template that has two columns of text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithRow1Column1TextProvider:(CLKTextProvider *) row1Column1TextProvider row1Column2TextProvider:(CLKTextProvider *) row1Column2TextProvider row2Column1TextProvider:(CLKTextProvider *) row2Column1TextProvider row2Column2TextProvider:(CLKTextProvider *) row2Column2TextProvider row3Column1TextProvider:(CLKTextProvider *) row3Column1TextProvider row3Column2TextProvider:(CLKTextProvider *) row3Column2TextProvider;
```

## Parameters

- `row1Column1TextProvider`: The text provider for the first row in the first column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row1Column2TextProvider`: The text provider for the first row in the second column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row2Column1TextProvider`: The text provider for the second row in the first column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row2Column2TextProvider`: The text provider for the second row in the second column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row3Column1TextProvider`: The text provider for the third row in the first column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row3Column2TextProvider`: The text provider for the third row in the second column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.

## See Also

### Creating the Template
- [init(row1Column1TextProvider: CLKTextProvider, row1Column2TextProvider: CLKTextProvider, row2Column1TextProvider: CLKTextProvider, row2Column2TextProvider: CLKTextProvider, row3Column1TextProvider: CLKTextProvider, row3Column2TextProvider: CLKTextProvider)](./init%28row1column1textprovider,row1column2textprovider,row2column1textprovider,row2column2textprovider,row3column1textprovider,row3column2textprovider%29.md)
  Creates a template that has two columns of text.
- [init(row1ImageProvider: CLKImageProvider?, row1Column1TextProvider: CLKTextProvider, row1Column2TextProvider: CLKTextProvider, row2ImageProvider: CLKImageProvider?, row2Column1TextProvider: CLKTextProvider, row2Column2TextProvider: CLKTextProvider, row3ImageProvider: CLKImageProvider?, row3Column1TextProvider: CLKTextProvider, row3Column2TextProvider: CLKTextProvider)](./init%28row1imageprovider,row1column1textprovider,row1column2textprovider,row2imageprovider,row2column1textprovider,row2column2textprovider,row3imageprovider,row3column1textprovider,row3column2textprovider%29.md)
  Creates a template that has a column of images and two columns of text.
- [+ templateWithRow1ImageProvider:row1Column1TextProvider:row1Column2TextProvider:row2ImageProvider:row2Column1TextProvider:row2Column2TextProvider:row3ImageProvider:row3Column1TextProvider:row3Column2TextProvider:](./templatewithrow1imageprovider_row1column1textprovider_row1column2textprovider_row2imageprovider_row2column1textprovider_row2column2textprovider_row3imageprovider_row3column1textprovider_row3column2textprovider_.md)
  Returns a template that has a column of images and two columns of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargecolumns/templatewithrow1column1textprovider:row1column2textprovider:row2column1textprovider:row2column2textprovider:row3column1textprovider:row3column2textprovider:)*