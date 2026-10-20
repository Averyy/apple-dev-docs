# jitterOffsetY

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The vertical component of the subpixel sampling coordinate you use to generate the color texture input.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 27.1+

## Declaration

```swift
var jitterOffsetY: Float { get set }
```

```objc
@property (nonatomic) float jitterOffsetY;
```

#### Discussion

This property indicates the vertical pixel offset this interpolator samples to return to the frame’s reference frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/jitteroffsety)*