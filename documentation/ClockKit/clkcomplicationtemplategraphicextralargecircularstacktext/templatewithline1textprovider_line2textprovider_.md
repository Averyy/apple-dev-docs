# templateWithLine1TextProvider:line2TextProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a new template with two rows of text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithLine1TextProvider:(CLKTextProvider *) line1TextProvider line2TextProvider:(CLKTextProvider *) line2TextProvider;
```

## Parameters

- `line1TextProvider`: The text provider for the top row of text. The template supports multicolored text from this text provider.
- `line2TextProvider`: The text provider for the bottom row of text. The template supports multicolored text from this text provider.

## See Also

### Creating the Template
- [init(line1TextProvider: CLKTextProvider, line2TextProvider: CLKTextProvider)](./init%28line1textprovider,line2textprovider%29.md)
  Creates a new template with two rows of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularstacktext/templatewithline1textprovider:line2textprovider:)*