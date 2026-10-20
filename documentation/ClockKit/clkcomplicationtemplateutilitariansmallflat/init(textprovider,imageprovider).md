# init(textProvider:imageProvider:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a new template that has a single row with an image and a line of text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```swift
init(textProvider: CLKTextProvider, imageProvider: CLKImageProvider?)
```

```objc
- (instancetype) initWithTextProvider:(CLKTextProvider *) textProvider imageProvider:(CLKImageProvider *) imageProvider;
```

## Parameters

- `textProvider`: The text provider for the line of text. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `imageProvider`: The image provider for the leading image. The system renders the image as a tinted template image, a bitmap image where only the opacity of the image matters. For more information, see [Providing images for different appearances](../../UIKit/providing-images-for-different-appearances.md).

## See Also

### Creating the Template
- [init(textProvider: CLKTextProvider)](./init%28textprovider%29.md)
  Creates a new template that has a single line of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitariansmallflat/init(textprovider:imageprovider:))*