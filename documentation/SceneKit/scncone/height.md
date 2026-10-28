# height

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The extent of the cylinder along its y-axis. Animatable.

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
var height: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat height;
```

## Discussion

The cone is centered in its local coordinate system. For example, if a cone has a height of `10.0`, its base lies in the plane whose y-coordinate is `-5.0` and its top has a y-coordinate of `5.0`. The default height is `1.0`. A height of zero or less creates an empty geometry.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Adjusting a Cone’s Dimensions
- [var topRadius: CGFloat](./topradius.md)
  The radius of the cone’s circular top. Animatable.
- [var bottomRadius: CGFloat](./bottomradius.md)
  The radius of the cone’s circular base. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncone/height)*