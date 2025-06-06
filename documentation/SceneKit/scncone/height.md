# height

**Framework**: SceneKit  
**Kind**: property

The extent of the cylinder along its y-axis. Animatable.

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
var height: CGFloat { get set }
```

#### Discussion

The cone is centered in its local coordinate system. For example, if a cone has a height of `10.0`, its base lies in the plane whose y-coordinate is `-5.0` and its top has a y-coordinate of `5.0`. The default height is `1.0`. A height of zero or less creates an empty geometry.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var topRadius: CGFloat](scncone/topradius.md)
  The radius of the cone’s circular top. Animatable.
- [var bottomRadius: CGFloat](scncone/bottomradius.md)
  The radius of the cone’s circular base. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncone/height)*