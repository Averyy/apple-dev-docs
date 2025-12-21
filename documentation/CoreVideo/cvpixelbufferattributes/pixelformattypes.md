# pixelFormatTypes

**Framework**: Core Video  
**Kind**: property

Allow multiple pixel formats to be specified in attributes

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var pixelFormatTypes: [CVPixelFormatType]? { get set }
```

#### Discussion

Setting this property will override the single format value set by [`pixelFormatType`](cvpixelbuffercreationattributes/pixelformattype.md) and vice-versa. When accessing [`pixelFormatType`](cvpixelbuffercreationattributes/pixelformattype.md), only the first value is used if multiple format values are set. Do not set this value to an empty array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferattributes/pixelformattypes)*