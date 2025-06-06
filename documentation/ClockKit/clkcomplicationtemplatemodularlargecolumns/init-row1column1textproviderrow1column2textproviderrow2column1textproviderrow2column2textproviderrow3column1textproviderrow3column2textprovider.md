# init(row1Column1TextProvider:row1Column2TextProvider:row2Column1TextProvider:row2Column2TextProvider:row3Column1TextProvider:row3Column2TextProvider:)

**Framework**: ClockKit  
**Kind**: init

Creates a template that has two columns of text.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(row1Column1TextProvider: CLKTextProvider, row1Column2TextProvider: CLKTextProvider, row2Column1TextProvider: CLKTextProvider, row2Column2TextProvider: CLKTextProvider, row3Column1TextProvider: CLKTextProvider, row3Column2TextProvider: CLKTextProvider)
```

## Parameters

- `row1Column1TextProvider`: The text provider for the first row in the first column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row1Column2TextProvider`: The text provider for the first row in the second column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row2Column1TextProvider`: The text provider for the second row in the first column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row2Column2TextProvider`: The text provider for the second row in the second column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row3Column1TextProvider`: The text provider for the third row in the first column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row3Column2TextProvider`: The text provider for the third row in the second column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.

## See Also

- [init(row1ImageProvider: CLKImageProvider?, row1Column1TextProvider: CLKTextProvider, row1Column2TextProvider: CLKTextProvider, row2ImageProvider: CLKImageProvider?, row2Column1TextProvider: CLKTextProvider, row2Column2TextProvider: CLKTextProvider, row3ImageProvider: CLKImageProvider?, row3Column1TextProvider: CLKTextProvider, row3Column2TextProvider: CLKTextProvider)](clkcomplicationtemplatemodularlargecolumns/init(row1imageprovider:row1column1textprovider:row1column2textprovider:row2imageprovider:row2column1textprovider:row2column2textprovider:row3imageprovider:row3column1textprovider:row3column2textprovider:).md)
  Creates a template that has a column of images and two columns of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargecolumns/init(row1column1textprovider:row1column2textprovider:row2column1textprovider:row2column2textprovider:row3column1textprovider:row3column2textprovider:))*