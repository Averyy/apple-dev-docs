# makeFrameInterpolator(device:)

**Framework**: MetalFX  
**Kind**: method

Creates a frame interpolator instance for a Metal device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func makeFrameInterpolator(device: any MTLDevice) -> (any MTLFXFrameInterpolator)?
```

#### Return Value

 A new frame interpolator instance upon success, or `nil` otherwise.

## Parameters

- `device`: The Metal device that creates the frame interpolator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatordescriptor/makeframeinterpolator(device:))*