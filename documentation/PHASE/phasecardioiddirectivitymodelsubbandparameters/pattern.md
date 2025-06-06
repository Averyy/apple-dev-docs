# pattern

**Framework**: PHASE  
**Kind**: property

A shape that determines the direction of sound.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var pattern: Double { get set }
```

#### Discussion

The framework clamps the value to the range `[0.0, 1.0]`. The default value is `0.0`, which creates an omnidirectional shape. The value `0.5` creates a cardioid shape. The value `1.0` creates a dipole shape.

## See Also

- [var sharpness: Double](phasecardioiddirectivitymodelsubbandparameters/sharpness.md)
  The amount that the shape overlaps with bordering subbands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecardioiddirectivitymodelsubbandparameters/pattern)*