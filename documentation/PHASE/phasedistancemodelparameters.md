# PHASEDistanceModelParameters

**Framework**: PHASE  
**Kind**: class

A base class for a sound’s rate of change over distance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEDistanceModelParameters
```

#### Overview

When your app outputs sound with a 3D position and orientation, designate a subclass of this class to indicate the manner in which PHASE changes sound with distance. Assign an instance of either [`PHASEGeometricSpreadingDistanceModelParameters`](phasegeometricspreadingdistancemodelparameters.md) or [`PHASEEnvelopeDistanceModelParameters`](phaseenvelopedistancemodelparameters.md), depending on your app’s needs, to the [`PHASESpatialMixerDefinition`](phasespatialmixerdefinition.md) class’s [`distanceModelParameters`](phasespatialmixerdefinition/distancemodelparameters.md) property.

## Topics

### Fading the Sound
- [var fadeOutParameters: PHASEDistanceModelFadeOutParameters?](phasedistancemodelparameters/fadeoutparameters.md)
  A distance over which the framework fades out the mixer’s sound.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [PHASEEnvelopeDistanceModelParameters](phaseenvelopedistancemodelparameters.md)
- [PHASEGeometricSpreadingDistanceModelParameters](phasegeometricspreadingdistancemodelparameters.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASEGeometricSpreadingDistanceModelParameters](phasegeometricspreadingdistancemodelparameters.md)
  An object that dissipates sound frequencies over distance.
- [class PHASEEnvelopeDistanceModelParameters](phaseenvelopedistancemodelparameters.md)
  A graph of points and curves that shapes the volume of a sound over distance.
- [class PHASEDistanceModelFadeOutParameters](phasedistancemodelfadeoutparameters.md)
  A distance over which the framework fades out sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasedistancemodelparameters)*