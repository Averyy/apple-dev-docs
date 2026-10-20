# distortionHeight

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The height, in pixels, of the content region within the distortion texture to use as input.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.1+

## Declaration

```swift
var distortionHeight: Int { get set }
```

```objc
@property (nonatomic, readwrite) NSUInteger distortionHeight;
```

#### Discussion

When set to zero (the default), the frame interpolator uses [`contentHeight`](./contentheight.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/distortionheight)*