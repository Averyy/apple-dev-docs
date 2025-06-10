# minimumAngularLimit

**Framework**: SceneKit  
**Kind**: property

The minimum rotation angle between the two bodies, measured in radians relative to their initial orientations.

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
var minimumAngularLimit: CGFloat { get set }
```

#### Discussion

The default (and minimum) value of this property is `-M_PI`. With this value, the joint can spin clockwise (relative to the first body) with no limit.

Set both this property and the [`maximumAngularLimit`](scnphysicssliderjoint/maximumangularlimit.md) property to the same value to prevent the bodies from rotating around their anchor points. (Set both properties to `0.0` to fix the bodies in their initial orientations.) Bodies whose orientation is fixed by a sliding joint may still slide, depending on the values of the [`minimumLinearLimit`](scnphysicssliderjoint/minimumlinearlimit.md) and [`maximumLinearLimit`](scnphysicssliderjoint/maximumlinearlimit.md) properties.

## See Also

- [var minimumLinearLimit: CGFloat](scnphysicssliderjoint/minimumlinearlimit.md)
  The minimum distance between the anchor points of the two bodies, relative to their initial positions.
- [var maximumLinearLimit: CGFloat](scnphysicssliderjoint/maximumlinearlimit.md)
  The maximum distance between the anchor points of the two bodies, relative to their initial positions.
- [var maximumAngularLimit: CGFloat](scnphysicssliderjoint/maximumangularlimit.md)
  The maximum rotation angle between the two bodies, measured in radians relative to their initial orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/minimumangularlimit)*