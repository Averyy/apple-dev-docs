# minimumAngularLimit

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The minimum rotation angle between the two bodies, measured in radians relative to their initial orientations.

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
var minimumAngularLimit: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat minimumAngularLimit;
```

## Discussion

The default (and minimum) value of this property is `-M_PI`. With this value, the joint can spin clockwise (relative to the first body) with no limit.

Set both this property and the [`maximumAngularLimit`](./maximumangularlimit.md) property to the same value to prevent the bodies from rotating around their anchor points. (Set both properties to `0.0` to fix the bodies in their initial orientations.) Bodies whose orientation is fixed by a sliding joint may still slide, depending on the values of the [`minimumLinearLimit`](./minimumlinearlimit.md) and [`maximumLinearLimit`](./maximumlinearlimit.md) properties.

## See Also

### Limiting the Motion of a Slider Joint
- [var minimumLinearLimit: CGFloat](./minimumlinearlimit.md)
  The minimum distance between the anchor points of the two bodies, relative to their initial positions.
- [var maximumLinearLimit: CGFloat](./maximumlinearlimit.md)
  The maximum distance between the anchor points of the two bodies, relative to their initial positions.
- [var maximumAngularLimit: CGFloat](./maximumangularlimit.md)
  The maximum rotation angle between the two bodies, measured in radians relative to their initial orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/minimumangularlimit)*