# init(width:height:)

**Framework**: SceneKit  
**Kind**: init

Creates a plane geometry with the specified width and height.

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
convenience init(width: CGFloat, height: CGFloat)
```

#### Return Value

A new plane geometry.

#### Discussion

The plane is centered in its local coordinate system. For example, if you create a plane whose width and height are both `10.0`, it extends from `-5.0` to `5.0` along both the x- and y-axes, and the z-coordinate of all points in the plane is zero.

## Parameters

- `width`: The width of the plane along the x-axis of its local coordinate space.
- `height`: The height of the plane along the y-axis of its local coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnplane/init(width:height:))*