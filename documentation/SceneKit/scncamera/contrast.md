# contrast

**Framework**: SceneKit  
**Kind**: property

An adjustment factor to apply to the overall visual contrast of the rendered scene.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var contrast: CGFloat { get set }
```

#### Discussion

A value of 0.0 (the default) leaves the rendered scene unchanged. Positive values increase contrast between bright and dark areas, and negative values reduce contrast, shifting the rendered scene towards a uniform gray.

To enable this behavior, you must first enable the [`wantsHDR`](scncamera/wantshdr.md) setting.

## See Also

- [var saturation: CGFloat](scncamera/saturation.md)
  An adjustment factor to apply to the overall color saturation of the rendered scene.
- [var colorGrading: SCNMaterialProperty](scncamera/colorgrading.md)
  A texture for applying color grading effects to the entire rendered scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/contrast)*