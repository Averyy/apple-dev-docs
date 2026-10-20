# automaticallyAdjustsZRange

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the camera automatically adjusts its [`zNear`](./znear.md) and [`zFar`](./zfar.md) depth limits.

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
var automaticallyAdjustsZRange: Bool { get set }
```

```objc
@property (nonatomic) BOOL automaticallyAdjustsZRange;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md), specifying that the camera’s [`zNear`](./znear.md) and [`zFar`](./zfar.md) properties control its depth limits. If you change this property’s value to [`true`](../../Swift/true.md), SceneKit automatically adjusts the depth limits at render time to fit the bounding box of the scene. Changing the values of the [`zNear`](./znear.md) and [`zFar`](./zfar.md) properties automatically resets this property’s value to [`false`](../../Swift/false.md).

## See Also

### Adjusting Camera Perspective
- [var zNear: Double](./znear.md)
  The camera’s near depth limit. Animatable.
- [var zFar: Double](./zfar.md)
  The camera’s far depth limit. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/automaticallyadjustszrange)*