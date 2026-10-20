# saturation

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An adjustment factor to apply to the overall color saturation of the rendered scene.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var saturation: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat saturation;
```

#### Discussion

A value of `1.0` (the default) leaves scene colors unchanged. Greater values result in oversaturated colors, and a value of `0.0` makes the rendered scene entirely grayscale.

To enable this behavior, you must first enable the [`wantsHDR`](./wantshdr.md) setting.

## See Also

### Adjusting Rendered Colors
- [var contrast: CGFloat](./contrast.md)
  An adjustment factor to apply to the overall visual contrast of the rendered scene.
- [var colorGrading: SCNMaterialProperty](./colorgrading.md)
  A texture for applying color grading effects to the entire rendered scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/saturation)*