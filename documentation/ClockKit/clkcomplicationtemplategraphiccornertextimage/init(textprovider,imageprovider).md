# init(textProvider:imageProvider:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a template with a line of text and an image.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```swift
init(textProvider: CLKTextProvider, imageProvider: CLKFullColorImageProvider)
```

```objc
- (instancetype) initWithTextProvider:(CLKTextProvider *) textProvider imageProvider:(CLKFullColorImageProvider *) imageProvider;
```

## Parameters

- `textProvider`: The text provider for the text. The template supports multicolored text from this text provider.
- `imageProvider`: A full-color image provider.

## See Also

### Creating the Template
- [+ templateWithTextProvider:imageProvider:](./templatewithtextprovider_imageprovider_.md)
  Creates a template with a line of text and an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornertextimage/init(textprovider:imageprovider:))*