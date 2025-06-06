# PHASECardioidDirectivityModelSubbandParameters

**Framework**: PHASE  
**Kind**: class

A data set that projects sound of a certain frequency outward in the shape of a heart.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASECardioidDirectivityModelSubbandParameters
```

#### Overview

This class defines one subband in the [`PHASECardioidDirectivityModelParameters`](phasecardioiddirectivitymodelparameters.md) class’s `subbands`. Depending on the specific shape you define with [`pattern`](phasecardioiddirectivitymodelsubbandparameters/pattern.md) and [`sharpness`](phasecardioiddirectivitymodelsubbandparameters/sharpness.md), you can attenuate sound focused at [`frequency`](phasecardioiddirectivitymodelsubbandparameters/frequency.md) to the sides of the listener, while leaving the sound in front of or behind the listener unchanged.

## Topics

### Creating Cardioid Directivity Subband Parameters
- [init()](phasecardioiddirectivitymodelsubbandparameters/init.md)
  Creates a data set that projects sound of a certain frequency outward in the shape of a heart.
### Sizing the Subband
- [var frequency: Double](phasecardioiddirectivitymodelsubbandparameters/frequency.md)
  A frequency in the audio spectrum where the pattern and sharpness resonate most.
### Shaping Directivity
- [var pattern: Double](phasecardioiddirectivitymodelsubbandparameters/pattern.md)
  A shape that determines the direction of sound.
- [var sharpness: Double](phasecardioiddirectivitymodelsubbandparameters/sharpness.md)
  The amount that the shape overlaps with bordering subbands.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASECardioidDirectivityModelParameters](phasecardioiddirectivitymodelparameters.md)
  An object that directs sound in a heart-shaped curve surrounding a sound source.
- [class PHASEConeDirectivityModelParameters](phaseconedirectivitymodelparameters.md)
  An object that directs sound in a cone-shaped curve that extends from a sound source.
- [class PHASEConeDirectivityModelSubbandParameters](phaseconedirectivitymodelsubbandparameters.md)
  A data set that projects sound of a certain frequency outward in the shape of a cone.
- [class PHASEDirectivityModelParameters](phasedirectivitymodelparameters.md)
  A base class for objects that direct sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecardioiddirectivitymodelsubbandparameters)*