# lifetime

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The lifetime of the cell, in seconds. Animatable.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var lifetime: Float { get set }
```

```objc
@property float lifetime;
```

## Discussion

The lifetime of the cell will vary by a random amount with the range specified by [`lifetimeRange`](./lifetimerange.md).

The default value of this property is `0.0`.

## See Also

### Setting Emitter Cell Temporal Attributes
- [var lifetimeRange: Float](./lifetimerange.md)
  The mean value by which the [`lifetime`](./lifetime.md) of the cell can vary. Animatable.
- [var birthRate: Float](./birthrate.md)
  The number of emitted objects created every second. Animatable.
- [var scaleSpeed: CGFloat](./scalespeed.md)
  The speed at which the scale changes over the lifetime of the cell. Animatable.
- [var velocity: CGFloat](./velocity.md)
  The initial velocity of the cell. Animatable.
- [var velocityRange: CGFloat](./velocityrange.md)
  The amount by which the velocity of the cell can vary. Animatable.
- [var xAcceleration: CGFloat](./xacceleration.md)
  The x component of an acceleration vector applied to cell.
- [var yAcceleration: CGFloat](./yacceleration.md)
  The y component of an acceleration vector applied to cell.
- [var zAcceleration: CGFloat](./zacceleration.md)
  The z component of an acceleration vector applied to cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemittercell/lifetime)*