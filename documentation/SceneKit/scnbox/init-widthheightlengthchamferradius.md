# init(width:height:length:chamferRadius:)

**Framework**: SceneKit  
**Kind**: init

Creates a box geometry with the specified width, height, length, and chamfer radius.

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
convenience init(width: CGFloat, height: CGFloat, length: CGFloat, chamferRadius: CGFloat)
```

#### Return Value

A new box geometry.

#### Discussion

The box is centered in its local coordinate system. For example, if you create a box whose width, height and length are all `10.0`, it extends from `-5.0` to `5.0` along in each of the x-, y-, and z-axes.

## Parameters

- `width`: The width of the box along the x-axis of its local coordinate space.
- `height`: The height of the box along the y-axis of its local coordinate space.
- `length`: The length of the box along the z-axis of its local coordinate space.
- `chamferRadius`: The radius of curvature for the edges and corners of the box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbox/init(width:height:length:chamferradius:))*