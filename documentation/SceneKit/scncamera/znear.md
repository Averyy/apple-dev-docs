# zNear

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The camera’s near depth limit. Animatable.

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
var zNear: Double { get set }
```

```objc
@property (nonatomic) double zNear;
```

#### Discussion

The near value determines the minimal distance between the camera and a visible surface. If a surface is closer to the camera than this  distance, the surface is clipped and does not appear. The near value must not be zero. The default near value is `1.0`.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Adjusting Camera Perspective
- [var zFar: Double](./zfar.md)
  The camera’s far depth limit. Animatable.
- [var automaticallyAdjustsZRange: Bool](./automaticallyadjustszrange.md)
  A Boolean value that determines whether the camera automatically adjusts its [`zNear`](./znear.md) and [`zFar`](./zfar.md) depth limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/znear)*