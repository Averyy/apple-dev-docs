# minimumLinearLimit

**Framework**: SceneKit  
**Kind**: property

The minimum distance between the anchor points of the two bodies, relative to their initial positions.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var minimumLinearLimit: CGFloat { get set }
```

#### Discussion

The default value of this property is `-INFINITY`. With this value, the joint can slide forever in the direction opposite the slider axis.

Set both this property and the [`maximumLinearLimit`](scnphysicssliderjoint/maximumlinearlimit.md) property to the same value to pin the bodies together at their anchor points. (Set both properties to `0.0` to pin the bodies together at their initial positions.) Bodies pinned together by a sliding joint may still rotate, depending on the values of the [`minimumAngularLimit`](scnphysicssliderjoint/minimumangularlimit.md) and [`maximumAngularLimit`](scnphysicssliderjoint/maximumangularlimit.md) properties.

## See Also

- [var maximumLinearLimit: CGFloat](scnphysicssliderjoint/maximumlinearlimit.md)
  The maximum distance between the anchor points of the two bodies, relative to their initial positions.
- [var minimumAngularLimit: CGFloat](scnphysicssliderjoint/minimumangularlimit.md)
  The minimum rotation angle between the two bodies, measured in radians relative to their initial orientations.
- [var maximumAngularLimit: CGFloat](scnphysicssliderjoint/maximumangularlimit.md)
  The maximum rotation angle between the two bodies, measured in radians relative to their initial orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/minimumlinearlimit)*