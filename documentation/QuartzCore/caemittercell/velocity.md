# velocity

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The initial velocity of the cell. Animatable.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var velocity: CGFloat { get set }
```

```objc
@property CGFloat velocity;
```

#### Discussion

The velocity of the cell will vary by a random amount within the range specified by [`velocityRange`](./velocityrange.md).

## See Also

### Setting Emitter Cell Temporal Attributes
- [var lifetime: Float](./lifetime.md)
  The lifetime of the cell, in seconds. Animatable.
- [var lifetimeRange: Float](./lifetimerange.md)
  The mean value by which the [`lifetime`](./lifetime.md) of the cell can vary. Animatable.
- [var birthRate: Float](./birthrate.md)
  The number of emitted objects created every second. Animatable.
- [var scaleSpeed: CGFloat](./scalespeed.md)
  The speed at which the scale changes over the lifetime of the cell. Animatable.
- [var velocityRange: CGFloat](./velocityrange.md)
  The amount by which the velocity of the cell can vary. Animatable.
- [var xAcceleration: CGFloat](./xacceleration.md)
  The x component of an acceleration vector applied to cell.
- [var yAcceleration: CGFloat](./yacceleration.md)
  The y component of an acceleration vector applied to cell.
- [var zAcceleration: CGFloat](./zacceleration.md)
  The z component of an acceleration vector applied to cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemittercell/velocity)*