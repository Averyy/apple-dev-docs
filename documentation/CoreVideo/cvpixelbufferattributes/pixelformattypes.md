# pixelFormatTypes

**Framework**: Core Video  
**Kind**: property

Allow multiple pixel formats to be specified in attributes

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var pixelFormatTypes: [CVPixelFormatType]? { get set }
```

#### Discussion

Setting this property will override the single format value set by [`pixelFormatType`](cvpixelbuffercreationattributes/pixelformattype.md) and vice-versa. When accessing [`pixelFormatType`](cvpixelbuffercreationattributes/pixelformattype.md), only the first value is used if multiple format values are set. Do not set this value to an empty array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferattributes/pixelformattypes)*