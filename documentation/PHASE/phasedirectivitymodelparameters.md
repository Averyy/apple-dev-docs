# PHASEDirectivityModelParameters

**Framework**: PHASE  
**Kind**: class

A base class for objects that direct sound.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEDirectivityModelParameters
```

#### Overview

Several classes derive from this class that implement a unique strategy to direct sound. Rather than create an instance of this class, instantiate a subclass, such as [`PHASECardioidDirectivityModelParameters`](phasecardioiddirectivitymodelparameters.md) or [`PHASEConeDirectivityModelParameters`](phaseconedirectivitymodelparameters.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [PHASECardioidDirectivityModelParameters](phasecardioiddirectivitymodelparameters.md)
- [PHASEConeDirectivityModelParameters](phaseconedirectivitymodelparameters.md)
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
- [class PHASEConeDirectivityModelSubbandParameters](phaseconedirectivitymodelsubbandparameters.md)
  A data set that projects sound of a certain frequency outward in the shape of a cone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasedirectivitymodelparameters)*