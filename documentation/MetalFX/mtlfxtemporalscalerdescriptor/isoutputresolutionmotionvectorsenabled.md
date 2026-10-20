# isOutputResolutionMotionVectorsEnabled

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the scaler expects motion vectors at output resolution.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.1+

## Declaration

```swift
var isOutputResolutionMotionVectorsEnabled: Bool { get set }
```

```objc
@property (nonatomic, readwrite, getter=isOutputResolutionMotionVectorsEnabled) BOOL outputResolutionMotionVectorsEnabled;
```

#### Discussion

Set this property to [`true`](../../Swift/true.md) when your app provides motion vectors at the output resolution rather than the input resolution.

When you enable this property, the scaler interprets the [`motionTexture`](../mtlfxtemporalscalerbase/motiontexture.md) dimensions to match [`outputWidth`](./outputwidth.md) and [`outputHeight`](./outputheight.md) instead of [`inputWidth`](./inputwidth.md) and [`inputHeight`](./inputheight.md).

This property’s default value is [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerdescriptor/isoutputresolutionmotionvectorsenabled)*