# minimumLinearLimit

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The minimum distance between the anchor points of the two bodies, relative to their initial positions.

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
var minimumLinearLimit: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat minimumLinearLimit;
```

#### Discussion

The default value of this property is `-INFINITY`. With this value, the joint can slide forever in the direction opposite the slider axis.

Set both this property and the [`maximumLinearLimit`](./maximumlinearlimit.md) property to the same value to pin the bodies together at their anchor points. (Set both properties to `0.0` to pin the bodies together at their initial positions.) Bodies pinned together by a sliding joint may still rotate, depending on the values of the [`minimumAngularLimit`](./minimumangularlimit.md) and [`maximumAngularLimit`](./maximumangularlimit.md) properties.

## See Also

### Limiting the Motion of a Slider Joint
- [var maximumLinearLimit: CGFloat](./maximumlinearlimit.md)
  The maximum distance between the anchor points of the two bodies, relative to their initial positions.
- [var minimumAngularLimit: CGFloat](./minimumangularlimit.md)
  The minimum rotation angle between the two bodies, measured in radians relative to their initial orientations.
- [var maximumAngularLimit: CGFloat](./maximumangularlimit.md)
  The maximum rotation angle between the two bodies, measured in radians relative to their initial orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/minimumlinearlimit)*