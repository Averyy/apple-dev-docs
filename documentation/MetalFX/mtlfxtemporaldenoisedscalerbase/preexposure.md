# preExposure

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

A pre-exposure value for this scaler to evaluate.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var preExposure: Float { get set }
```

#### Discussion

If the input color texture you assign to [`colorTexture`](mtlfxtemporaldenoisedscalerbase/colortexture.md) is pre-multiplied by fixed value, set this property to that same fixed value so MetalFX divides input color by it. This is not a common situation and you typically don’t need to assign a value to this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase/preexposure)*