# init(radius:)

**Framework**: SceneKit  
**Kind**: init

Creates a sphere geometry with the specified radius.

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
convenience init(radius: CGFloat)
```

#### Return Value

A new sphere geometry.

#### Discussion

The sphere is centered in its local coordinate system. For example, if you create a sphere whose radius is `5.0`, it extends from `-5.0` to `5.0` along each of the the x, y, and z-axes.

## Parameters

- `radius`: The radius of the sphere in its local coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnsphere/init(radius:))*