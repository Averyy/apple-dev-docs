# templateWithImageProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a new template that has a square image.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithImageProvider:(CLKImageProvider *) imageProvider;
```

## Parameters

- `imageProvider`: The image provider for an image that fills the template. The system renders the image as a tinted template image, a bitmap image where only the opacity of the image matters. For more information, see [Providing images for different appearances](../../UIKit/providing-images-for-different-appearances.md).

## See Also

### Creating the Template
- [init(imageProvider: CLKImageProvider)](./init%28imageprovider%29.md)
  Creates a new template that has a square image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitariansmallsquare/templatewithimageprovider:)*