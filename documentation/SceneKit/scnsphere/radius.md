# radius

**Framework**: SceneKit  
**Kind**: property

The radius of the sphere. Animatable.

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
var radius: CGFloat { get set }
```

#### Discussion

The sphere is centered in its local coordinate system. For example, if you create a sphere whose radius is `5.0`, it extends from `-5.0` to `5.0` along each of the the x, y, and z-axes. A radius of zero or less creates an empty geometry.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnsphere/radius)*