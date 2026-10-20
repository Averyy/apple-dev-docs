# radius

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The radius of the cylinder’s circular cross section. Animatable.

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
var radius: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat radius;
```

#### Discussion

The cylinder is centered in its local coordinate system. For example, a cylinder of radius `5.0` extends from `-5.0` to `5.0` along the x- and z-axes. The default radius is `0.5`. A radius of zero or less creates an empty geometry.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Related Documentation
- [class SCNCylinder](../scncylinder.md)
  A right circular cylinder geometry.
### Adjusting a Cylinder’s Dimensions
- [var height: CGFloat](./height.md)
  The extent of the cylinder along its y-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncylinder/radius)*