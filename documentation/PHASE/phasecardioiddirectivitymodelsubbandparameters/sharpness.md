# sharpness

**Framework**: PHASE  
**Kind**: property

The amount that the shape overlaps with bordering subbands.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var sharpness: Double { get set }
```

#### Discussion

This property condenses the shape of the [`pattern`](phasecardioiddirectivitymodelsubbandparameters/pattern.md) such that higher values extend the shape frontwards. Increasing sharpness for dipole (a [`pattern`](phasecardioiddirectivitymodelsubbandparameters/pattern.md) value of `1.0`), extends the shape frontwards and backwards.

The default value is `1.0`. Values greater than `1.0` increase sharpness. The framework clamps the value to the range `[1.0,` [`greatestFiniteMagnitude`](https://developer.apple.com/documentation/Swift/Double/greatestFiniteMagnitude)`]`.

## See Also

- [var pattern: Double](phasecardioiddirectivitymodelsubbandparameters/pattern.md)
  A shape that determines the direction of sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecardioiddirectivitymodelsubbandparameters/sharpness)*