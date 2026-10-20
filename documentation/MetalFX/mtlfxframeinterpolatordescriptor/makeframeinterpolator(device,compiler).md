# makeFrameInterpolator(device:compiler:)

**Framework**: MetalFX  
**Kind**: method  
**Role**: Instance Method

Creates a frame interpolator instance for a Metal device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 27.1+

## Declaration

```swift
func makeFrameInterpolator(device: any MTLDevice, compiler: any MTL4Compiler) -> (any MTL4FXFrameInterpolator)?
```

```objc
- (id<MTL4FXFrameInterpolator>) newFrameInterpolatorWithDevice:(id<MTLDevice>) device compiler:(id<MTL4Compiler>) compiler;
```

#### Return Value

 A new frame interpolator instance upon success, or `nil` otherwise.

## Parameters

- `device`: The Metal device that creates the frame interpolator.
- `compiler`: A compiler instance this method can use to build pipeline state objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatordescriptor/makeframeinterpolator(device:compiler:))*