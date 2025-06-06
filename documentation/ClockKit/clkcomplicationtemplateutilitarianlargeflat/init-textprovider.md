# init(textProvider:)

**Framework**: ClockKit  
**Kind**: init

Creates a new template that has a long line of text.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(textProvider: CLKTextProvider)
```

## Parameters

- `textProvider`: The text provider for the template. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.

## See Also

- [init(textProvider: CLKTextProvider, imageProvider: CLKImageProvider?)](clkcomplicationtemplateutilitarianlargeflat/init(textprovider:imageprovider:).md)
  Creates a new template that has a single row with an image and a long line of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitarianlargeflat/init(textprovider:))*