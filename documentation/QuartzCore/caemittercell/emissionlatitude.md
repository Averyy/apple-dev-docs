# emissionLatitude

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The latitudinal orientation of the emission angle. Animatable.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var emissionLatitude: CGFloat { get set }
```

```objc
@property CGFloat emissionLatitude;
```

## Discussion

The emission latitude is the orientation of the emission angle from the z-axis. It is also referred to as the colatitude.

The default value of this property is `0.0`.

## See Also

### Setting Emitter Cell Motion Attributes
- [var spin: CGFloat](./spin.md)
  The rotational velocity, measured in radians per second, to apply to the cell. Animatable.
- [var spinRange: CGFloat](./spinrange.md)
  The amount by which the spin of the cell can vary over its lifetime. Animatable.
- [var emissionLongitude: CGFloat](./emissionlongitude.md)
  The longitudinal orientation of the emission angle. Animatable.
- [var emissionRange: CGFloat](./emissionrange.md)
  The angle, in radians, defining a cone around the emission angle. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemittercell/emissionlatitude)*