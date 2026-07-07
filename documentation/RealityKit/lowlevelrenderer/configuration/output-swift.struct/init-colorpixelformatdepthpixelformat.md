# init(colorPixelFormat:depthPixelFormat:)

**Framework**: RealityKit  
**Kind**: init

Creates an output configuration with the given color and depth pixel formats.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(colorPixelFormat: MTLPixelFormat?, depthPixelFormat: MTLPixelFormat? = nil)
```

## Parameters

- `colorPixelFormat`: The pixel format of the color attachment, or `nil` for depth-only passes.
- `depthPixelFormat`: The pixel format of the depth attachment, or `nil` to omit depth. Defaults to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/configuration/output-swift.struct/init(colorpixelformat:depthpixelformat:))*