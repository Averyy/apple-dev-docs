# init(line1ImageProvider:line2TextProvider:)

**Framework**: ClockKit  
**Kind**: init

Creates a new template from the provided image and text.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(line1ImageProvider: CLKImageProvider, line2TextProvider: CLKTextProvider)
```

## Parameters

- `line1ImageProvider`: The image provider for the main image. The system renders the image as a tinted template image, a bitmap image where only the opacity of the image matters. For more information, see  .
- `line2TextProvider`: A text provider for the text below the image. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallstackimage/init(line1imageprovider:line2textprovider:))*