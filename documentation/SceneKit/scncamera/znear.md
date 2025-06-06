# zNear

**Framework**: SceneKit  
**Kind**: property

The camera’s near depth limit. Animatable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var zNear: Double { get set }
```

#### Discussion

The near value determines the minimal distance between the camera and a visible surface. If a surface is closer to the camera than this  distance, the surface is clipped and does not appear. The near value must not be zero. The default near value is `1.0`.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var zFar: Double](scncamera/zfar.md)
  The camera’s far depth limit. Animatable.
- [var automaticallyAdjustsZRange: Bool](scncamera/automaticallyadjustszrange.md)
  A Boolean value that determines whether the camera automatically adjusts its [`zNear`](scncamera/znear.md) and [`zFar`](scncamera/zfar.md) depth limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/znear)*