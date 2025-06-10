# height

**Framework**: SceneKit  
**Kind**: property

The extent of the tube along its y-axis. Animatable.

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
var height: CGFloat { get set }
```

#### Discussion

The tube is centered in its local coordinate system. For example, if a tube has a height of `10.0`, its base lies in the plane whose y-coordinate is `-5.0` and its top is in the plane whose y-coordinate is `5.0`. The default height is `1.0`. A height of zero or less creates an empty geometry.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var outerRadius: CGFloat](scntube/outerradius.md)
  The radius of the tube’s outer circular cross section. Animatable.
- [var innerRadius: CGFloat](scntube/innerradius.md)
  The radius of the circular hole through the tube. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntube/height)*