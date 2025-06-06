# scaleSpeed

**Framework**: Core Animation  
**Kind**: property

The speed at which the scale changes over the lifetime of the cell. Animatable.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var scaleSpeed: CGFloat { get set }
```

#### Discussion

The speed change is defined as the rate of change per second.

The default value of this property is `0.0`.

## See Also

- [var lifetime: Float](caemittercell/lifetime.md)
  The lifetime of the cell, in seconds. Animatable.
- [var lifetimeRange: Float](caemittercell/lifetimerange.md)
  The mean value by which the [`lifetime`](caemittercell/lifetime.md) of the cell can vary. Animatable.
- [var birthRate: Float](caemittercell/birthrate.md)
  The number of emitted objects created every second. Animatable.
- [var velocity: CGFloat](caemittercell/velocity.md)
  The initial velocity of the cell. Animatable.
- [var velocityRange: CGFloat](caemittercell/velocityrange.md)
  The amount by which the velocity of the cell can vary. Animatable.
- [var xAcceleration: CGFloat](caemittercell/xacceleration.md)
  The x component of an acceleration vector applied to cell.
- [var yAcceleration: CGFloat](caemittercell/yacceleration.md)
  The y component of an acceleration vector applied to cell.
- [var zAcceleration: CGFloat](caemittercell/zacceleration.md)
  The z component of an acceleration vector applied to cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemittercell/scalespeed)*