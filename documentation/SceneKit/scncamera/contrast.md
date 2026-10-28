# contrast

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An adjustment factor to apply to the overall visual contrast of the rendered scene.

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
var contrast: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat contrast;
```

## Discussion

A value of 0.0 (the default) leaves the rendered scene unchanged. Positive values increase contrast between bright and dark areas, and negative values reduce contrast, shifting the rendered scene towards a uniform gray.

To enable this behavior, you must first enable the [`wantsHDR`](./wantshdr.md) setting.

## See Also

### Adjusting Rendered Colors
- [var saturation: CGFloat](./saturation.md)
  An adjustment factor to apply to the overall color saturation of the rendered scene.
- [var colorGrading: SCNMaterialProperty](./colorgrading.md)
  A texture for applying color grading effects to the entire rendered scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/contrast)*