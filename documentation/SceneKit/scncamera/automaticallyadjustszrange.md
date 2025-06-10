# automaticallyAdjustsZRange

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether the camera automatically adjusts its [`zNear`](scncamera/znear.md) and [`zFar`](scncamera/zfar.md) depth limits.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var automaticallyAdjustsZRange: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false), specifying that the camera’s [`zNear`](scncamera/znear.md) and [`zFar`](scncamera/zfar.md) properties control its depth limits. If you change this property’s value to [`true`](https://developer.apple.com/documentation/swift/true), SceneKit automatically adjusts the depth limits at render time to fit the bounding box of the scene. Changing the values of the [`zNear`](scncamera/znear.md) and [`zFar`](scncamera/zfar.md) properties automatically resets this property’s value to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var zNear: Double](scncamera/znear.md)
  The camera’s near depth limit. Animatable.
- [var zFar: Double](scncamera/zfar.md)
  The camera’s far depth limit. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/automaticallyadjustszrange)*