# init(textProvider:imageProvider:)

**Framework**: ClockKit  
**Kind**: init

Creates a new template that has a single row with an image and a line of text.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(textProvider: CLKTextProvider, imageProvider: CLKImageProvider?)
```

## Parameters

- `textProvider`: The text provider for the line of text. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `imageProvider`: The image provider for the leading image. The system renders the image as a tinted template image, a bitmap image where only the opacity of the image matters. For more information, see  .

## See Also

- [init(textProvider: CLKTextProvider)](clkcomplicationtemplateutilitariansmallflat/init(textprovider:).md)
  Creates a new template that has a single line of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitariansmallflat/init(textprovider:imageprovider:))*