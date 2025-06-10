# setDepthBias(_:slopeScale:clamp:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setDepthBias(_ depthBias: Float, slopeScale: Float, clamp: Float)
```

## Parameters

- `depthBias`: A constant bias the render pipeline applies to all fragments.
- `slopeScale`: A bias coefficient that scales with the depth of the primitive relative to the camera.
- `clamp`: A value that limits the bias value the render pipeline can apply to a fragment.   Pass a positive or negative value to limit the largest magnitude of a positive   or negative bias, respectively. Set this value to   to disable bias clamping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setdepthbias(_:slopescale:clamp:))*