# newFrameInterpolator(with:compiler:)

**Framework**: MetalFX  
**Kind**: method

Creates a frame interpolator instance for a Metal device.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
func newFrameInterpolator(with device: any MTLDevice, compiler: any MTL4Compiler) -> (any MTL4FXFrameInterpolator)?
```

#### Return Value

 A new frame interpolator instance upon success, or `nil` otherwise.

## Parameters

- `device`: The Metal device that creates the frame interpolator.
- `compiler`: A compiler instance this method can use to build pipeline state objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatordescriptor/newframeinterpolator(with:compiler:))*