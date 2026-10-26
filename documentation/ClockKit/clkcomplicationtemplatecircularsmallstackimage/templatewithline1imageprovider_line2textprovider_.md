# templateWithLine1ImageProvider:line2TextProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a new template from the provided image and text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithLine1ImageProvider:(CLKImageProvider *) line1ImageProvider line2TextProvider:(CLKTextProvider *) line2TextProvider;
```

## Parameters

- `line1ImageProvider`: The image provider for the main image. The system renders the image as a tinted template image, a bitmap image where only the opacity of the image matters. For more information, see [Providing images for different appearances](../../UIKit/providing-images-for-different-appearances.md).
- `line2TextProvider`: A text provider for the text below the image. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.

## See Also

### Creating the Template
- [init(line1ImageProvider: CLKImageProvider, line2TextProvider: CLKTextProvider)](./init%28line1imageprovider,line2textprovider%29.md)
  Creates a new template from the provided image and text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallstackimage/templatewithline1imageprovider:line2textprovider:)*