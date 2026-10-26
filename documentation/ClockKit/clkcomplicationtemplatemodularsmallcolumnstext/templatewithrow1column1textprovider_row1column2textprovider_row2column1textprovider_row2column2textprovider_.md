# templateWithRow1Column1TextProvider:row1Column2TextProvider:row2Column1TextProvider:row2Column2TextProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a new template that has two columns of text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithRow1Column1TextProvider:(CLKTextProvider *) row1Column1TextProvider row1Column2TextProvider:(CLKTextProvider *) row1Column2TextProvider row2Column1TextProvider:(CLKTextProvider *) row2Column1TextProvider row2Column2TextProvider:(CLKTextProvider *) row2Column2TextProvider;
```

## Parameters

- `row1Column1TextProvider`: A text provider for the top row of the first column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row1Column2TextProvider`: A text provider for the top row of the second column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row2Column1TextProvider`: A text provider for the bottom row of the first column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `row2Column2TextProvider`: A text provider for the bottom row of the second column. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.

## See Also

### Creating the Template
- [init(row1Column1TextProvider: CLKTextProvider, row1Column2TextProvider: CLKTextProvider, row2Column1TextProvider: CLKTextProvider, row2Column2TextProvider: CLKTextProvider)](./init%28row1column1textprovider,row1column2textprovider,row2column1textprovider,row2column2textprovider%29.md)
  Creates a new template that has two columns of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallcolumnstext/templatewithrow1column1textprovider:row1column2textprovider:row2column1textprovider:row2column2textprovider:)*