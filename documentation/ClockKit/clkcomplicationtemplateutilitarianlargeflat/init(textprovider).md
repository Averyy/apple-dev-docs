# init(textProvider:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a new template that has a long line of text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```swift
init(textProvider: CLKTextProvider)
```

```objc
- (instancetype) initWithTextProvider:(CLKTextProvider *) textProvider;
```

## Parameters

- `textProvider`: The text provider for the template. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.

## See Also

### Creating the Template
- [init(textProvider: CLKTextProvider, imageProvider: CLKImageProvider?)](./init%28textprovider,imageprovider%29.md)
  Creates a new template that has a single row with an image and a long line of text.
- [+ templateWithTextProvider:](./templatewithtextprovider_.md)
  Returns a new template that has a long line of text.
- [+ templateWithTextProvider:imageProvider:](./templatewithtextprovider_imageprovider_.md)
  Returns a new template that has a single row with an image and a long line of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitarianlargeflat/init(textprovider:))*