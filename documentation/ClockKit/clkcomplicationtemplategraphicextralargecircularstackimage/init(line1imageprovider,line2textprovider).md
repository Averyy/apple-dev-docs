# init(line1ImageProvider:line2TextProvider:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a template with an image and a small amount of text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
init(line1ImageProvider: CLKFullColorImageProvider, line2TextProvider: CLKTextProvider)
```

```objc
- (instancetype) initWithLine1ImageProvider:(CLKFullColorImageProvider *) line1ImageProvider line2TextProvider:(CLKTextProvider *) line2TextProvider;
```

## Parameters

- `line1ImageProvider`: A full-color image provider.
- `line2TextProvider`: The text provider for the text below the image. The template supports multicolored text from this text provider.

## See Also

### Creating the Template
- [+ templateWithLine1ImageProvider:line2TextProvider:](./templatewithline1imageprovider_line2textprovider_.md)
  Creates a template with an image and a small amount of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularstackimage/init(line1imageprovider:line2textprovider:))*