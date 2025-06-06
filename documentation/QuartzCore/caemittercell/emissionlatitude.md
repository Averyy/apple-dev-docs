# emissionLatitude

**Framework**: Core Animation  
**Kind**: property

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

#### Discussion

The emission latitude is the orientation of the emission angle from the z-axis. It is also referred to as the colatitude.

The default value of this property is `0.0`.

## See Also

- [var spin: CGFloat](caemittercell/spin.md)
  The rotational velocity, measured in radians per second, to apply to the cell. Animatable.
- [var spinRange: CGFloat](caemittercell/spinrange.md)
  The amount by which the spin of the cell can vary over its lifetime. Animatable.
- [var emissionLongitude: CGFloat](caemittercell/emissionlongitude.md)
  The longitudinal orientation of the emission angle. Animatable.
- [var emissionRange: CGFloat](caemittercell/emissionrange.md)
  The angle, in radians, defining a cone around the emission angle. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemittercell/emissionlatitude)*