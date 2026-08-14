# init(id:image:)

**Framework**: RealityKit  
**Kind**: init

Creates a new sample.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
init(id: Int, image: CVPixelBuffer)
```

## Parameters

- `id`: A unique identifier for the sample.  This `id` *must* be in the domain [0, 2147483647].
- `image`: The image data in one of the following formats: - [`kCVPixelFormatType_32BGRA`](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_32bgra) - [`kCVPixelFormatType_32ARGB`](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_32argb)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysample/init(id:image:))*