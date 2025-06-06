# PHASEConeDirectivityModelSubbandParameters

**Framework**: PHASE  
**Kind**: class

A data set that projects sound of a certain frequency outward in the shape of a cone.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEConeDirectivityModelSubbandParameters
```

#### Overview

This class defines one subband in the [`PHASEConeDirectivityModelParameters`](phaseconedirectivitymodelparameters.md) class’s `subbands`. The inner and outer angles you define with [`setAngles(innerAngle:outerAngle:)`](phaseconedirectivitymodelsubbandparameters/setangles(innerangle:outerangle:).md) describe a cone that directs sound of a given [`frequency`](phasecardioiddirectivitymodelsubbandparameters/frequency.md) toward the listener. The cone’s point rests at the 3D position of the sound source. The framework adjusts the volume of the sound according to location of the listener in the 3D scene:

- If the listener positions in an area outside of the subband’s [`outerAngle`](phaseconedirectivitymodelsubbandparameters/outerangle.md), the sound emanates from the source at the volume defined by [`outerGain`](phaseconedirectivitymodelsubbandparameters/outergain.md).
- If the listener positions inside the area defined by [`innerAngle`](phaseconedirectivitymodelsubbandparameters/innerangle.md), the sound emanates from the source at maximum volume.
- If the listener positions in between the outer and inner angles, the framework blends the volume to a value between [`outerGain`](phaseconedirectivitymodelsubbandparameters/outergain.md) and the maximum.

## Topics

### Creating Cone Directivity Subband Parameters
- [init()](phaseconedirectivitymodelsubbandparameters/init.md)
  Creates a data set that projects sound of a certain frequency outward in the shape of a cone.
### Sizing the Subband
- [var frequency: Double](phaseconedirectivitymodelsubbandparameters/frequency.md)
  A frequency in the audio spectrum where the subband resonates most.
### Shaping Directivity
- [var innerAngle: Double](phaseconedirectivitymodelsubbandparameters/innerangle.md)
  An angle, in degrees, that determines the size of the audio emitting area inside the cone.
- [var outerAngle: Double](phaseconedirectivitymodelsubbandparameters/outerangle.md)
  An angle, in degrees, that determines the size of the audio emitting area outside the cone.
- [var outerGain: Double](phaseconedirectivitymodelsubbandparameters/outergain.md)
  The loudness of the audio the outside area of the cone emits.
- [func setAngles(innerAngle: Double, outerAngle: Double)](phaseconedirectivitymodelsubbandparameters/setangles(innerangle:outerangle:).md)
  Configures a focus area for cone-based sound directivity.

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
- [class PHASECardioidDirectivityModelSubbandParameters](phasecardioiddirectivitymodelsubbandparameters.md)
  A data set that projects sound of a certain frequency outward in the shape of a heart.
- [class PHASEConeDirectivityModelParameters](phaseconedirectivitymodelparameters.md)
  An object that directs sound in a cone-shaped curve that extends from a sound source.
- [class PHASEDirectivityModelParameters](phasedirectivitymodelparameters.md)
  A base class for objects that direct sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseconedirectivitymodelsubbandparameters)*