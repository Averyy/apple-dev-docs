# isOutputResolutionMotionVectorsEnabled

**Framework**: MetalFX  
**Kind**: property

A Boolean value that indicates whether the scaler expects motion vectors at output resolution.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var isOutputResolutionMotionVectorsEnabled: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/Swift/true) when your app provides motion vectors at the output resolution rather than the input resolution.

When you enable this property, the scaler interprets the [`motionTexture`](mtlfxtemporalscalerbase/motiontexture.md) dimensions to match [`outputWidth`](mtlfxtemporalscalerdescriptor/outputwidth.md) and [`outputHeight`](mtlfxtemporalscalerdescriptor/outputheight.md) instead of [`inputWidth`](mtlfxtemporalscalerdescriptor/inputwidth.md) and [`inputHeight`](mtlfxtemporalscalerdescriptor/inputheight.md).

This property’s default value is [`false`](https://developer.apple.com/documentation/Swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerdescriptor/isoutputresolutionmotionvectorsenabled)*