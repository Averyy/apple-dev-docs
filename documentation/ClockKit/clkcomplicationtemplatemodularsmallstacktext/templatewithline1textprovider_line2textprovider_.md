# templateWithLine1TextProvider:line2TextProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a new template that has two lines of text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithLine1TextProvider:(CLKTextProvider *) line1TextProvider line2TextProvider:(CLKTextProvider *) line2TextProvider;
```

## Parameters

- `line1TextProvider`: A text provider for the top line of text. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `line2TextProvider`: A text provider for the bottom line of text. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.

## See Also

### Creating the Template
- [init(line1TextProvider: CLKTextProvider, line2TextProvider: CLKTextProvider)](./init%28line1textprovider,line2textprovider%29.md)
  Creates a new template that has two lines of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallstacktext/templatewithline1textprovider:line2textprovider:)*