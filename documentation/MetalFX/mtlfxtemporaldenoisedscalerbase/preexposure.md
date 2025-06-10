# preExposure

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

A pre-exposure value for this scaler to evaluate.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var preExposure: Float { get set }
```

#### Discussion

If the input color texture you assign to [`colorTexture`](mtlfxtemporaldenoisedscalerbase/colortexture.md) is pre-multiplied by fixed value, set this property to that same fixed value so MetalFX divides input color by it. This is not a common situation and you typically don’t need to assign a value to this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase/preexposure)*