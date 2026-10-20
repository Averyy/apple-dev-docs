# spotOuterAngle

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The angle, in degrees, of the area partially lit by a spotlight. Animatable.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var spotOuterAngle: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat spotOuterAngle;
```

#### Discussion

You define the cone-shaped illuminated area of a spotlight with a position and direction (from the node containing the light) and with an angle specifying the cone’s width. Additionally, the illuminated area can smoothly transition from full illumination to no illumination. This property determines the width of the transition area.

The default value is `45.0`.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Managing Spotlight Extent
- [var spotInnerAngle: CGFloat](./spotinnerangle.md)
  The angle, in degrees, of the area fully lit by a spotlight. Animatable.
- [var gobo: SCNMaterialProperty?](./gobo.md)
  An image or other visual content affecting the shape and color of a light’s illuminated area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/spotouterangle)*