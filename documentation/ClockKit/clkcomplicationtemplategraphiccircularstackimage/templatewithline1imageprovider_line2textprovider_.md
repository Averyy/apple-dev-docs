# templateWithLine1ImageProvider:line2TextProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a template that has an image and a small amount of text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithLine1ImageProvider:(CLKFullColorImageProvider *) line1ImageProvider line2TextProvider:(CLKTextProvider *) line2TextProvider;
```

## Parameters

- `line1ImageProvider`: A full-color image provider.
- `line2TextProvider`: The text provider for the text below the image. The template supports multicolored text from this text provider.

## See Also

### Creating the Template
- [init(line1ImageProvider: CLKFullColorImageProvider, line2TextProvider: CLKTextProvider)](./init%28line1imageprovider,line2textprovider%29.md)
  Creates a template that has an image and a small amount of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularstackimage/templatewithline1imageprovider:line2textprovider:)*