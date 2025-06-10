# init(radius:height:)

**Framework**: SceneKit  
**Kind**: init

Creates a cylinder geometry with the specified radius and height.

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
convenience init(radius: CGFloat, height: CGFloat)
```

#### Return Value

A new cylinder geometry.

#### Discussion

The cylinder is centered in its local coordinate system. For example, if you create a cylinder whose radius is `5.0` and height is `10.0`, its circular cross section extends from `-5.0` to `5.0` along the x- and z-axes, and the y-coordinates of its base and top are `-5.0` and `5.0`, respectively.

## Parameters

- `radius`: The radius of the cylinder’s circular cross section in the x- and z-axis dimensions of its local coordinate space.
- `height`: The height of the cylinder along the y-axis of its local coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncylinder/init(radius:height:))*