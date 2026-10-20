# init(id:image:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

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
- `image`: The image data in one of the following formats:

  - [`kCVPixelFormatType_32BGRA`](../../CoreVideo/kcvpixelformattype_32bgra.md)

    - [`kCVPixelFormatType_32ARGB`](../../CoreVideo/kcvpixelformattype_32argb.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysample/init(id:image:))*