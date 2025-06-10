# init(width:height:length:)

**Framework**: SceneKit  
**Kind**: init

Creates a pyramid geometry with the specified width, height, and length.

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
convenience init(width: CGFloat, height: CGFloat, length: CGFloat)
```

#### Return Value

A new pyramid geometry.

#### Discussion

The pyramid’s base is centered in its local coordinate system. For example, if you create a pyramid whose width, height and length are all `10.0`, its apex is at the point `{0, 10.0, 0}`, and its base lies in the plane whose y-coordinate is `0.0`, extending from `-5.0` to `5.0` along both the x- and z-axes.

## Parameters

- `width`: The width of the pyramid along the x-axis of its local coordinate space.
- `height`: The height of the pyramid along the y-axis of its local coordinate space.
- `length`: The length of the pyramid along the z-axis of its local coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnpyramid/init(width:height:length:))*