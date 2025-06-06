# init(capRadius:height:)

**Framework**: SceneKit  
**Kind**: init

Creates a capsule geometry with the specified radius and height.

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
convenience init(capRadius: CGFloat, height: CGFloat)
```

#### Return Value

A new capsule geometry.

#### Discussion

The capsule is centered in its local coordinate system. For example, if you create a capsule whose cap radius is `5.0` and height is `20.0`, it extends from `-10.0` to `10.0` in the y-axis, and the circular cross section at the center of its body extends from `-5.0` to `5.0` along the x- and z-axes.

## Parameters

- `capRadius`: The radius both of the capsule’s cylindrical body and of its hemispherical ends.
- `height`: The height of the capsule along the y-axis of its local coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncapsule/init(capradius:height:))*