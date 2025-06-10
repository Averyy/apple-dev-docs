# spotOuterAngle

**Framework**: SceneKit  
**Kind**: property

The angle, in degrees, of the area partially lit by a spotlight. Animatable.

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
var spotOuterAngle: CGFloat { get set }
```

#### Discussion

You define the cone-shaped illuminated area of a spotlight with a position and direction (from the node containing the light) and with an angle specifying the cone’s width. Additionally, the illuminated area can smoothly transition from full illumination to no illumination. This property determines the width of the transition area.

The default value is `45.0`.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var spotInnerAngle: CGFloat](scnlight/spotinnerangle.md)
  The angle, in degrees, of the area fully lit by a spotlight. Animatable.
- [var gobo: SCNMaterialProperty?](scnlight/gobo.md)
  An image or other visual content affecting the shape and color of a light’s illuminated area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/spotouterangle)*