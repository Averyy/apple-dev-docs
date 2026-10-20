# spin

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The rotational velocity, measured in radians per second, to apply to the cell. Animatable.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var spin: CGFloat { get set }
```

```objc
@property CGFloat spin;
```

#### Discussion

The spin of the cell will vary by a random amount with the range specified by [`spinRange`](./spinrange.md).

The default value of this property is `0.0`.

## See Also

### Setting Emitter Cell Motion Attributes
- [var spinRange: CGFloat](./spinrange.md)
  The amount by which the spin of the cell can vary over its lifetime. Animatable.
- [var emissionLatitude: CGFloat](./emissionlatitude.md)
  The latitudinal orientation of the emission angle. Animatable.
- [var emissionLongitude: CGFloat](./emissionlongitude.md)
  The longitudinal orientation of the emission angle. Animatable.
- [var emissionRange: CGFloat](./emissionrange.md)
  The angle, in radians, defining a cone around the emission angle. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemittercell/spin)*