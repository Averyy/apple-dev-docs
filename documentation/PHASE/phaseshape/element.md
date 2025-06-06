# PHASEShape.Element

**Framework**: PHASE  
**Kind**: class

An object that describes the characteristics of a physical surface.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class Element
```

#### Overview

This class defines the material that makes up a [`PHASEShape`](phaseshape.md) object.

You don’t instantiate instances of this class yourself; the framework creates an instance of this class for every material you pass into the [`init(engine:mesh:materials:)`](phaseshape/init(engine:mesh:materials:).md) initializer. The shape’s [`elements`](phaseshape/elements.md) array provides read-only access to the instances.

## Topics

### Specifying a Meterial
- [var material: PHASEMaterial?](phaseshape/element/material.md)
  A surface characteristic that determines the acoustic properties of an object.

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

- [class PHASESource](phasesource.md)
  An object that plays audio from a 3D location and orientation in a scene.
- [class PHASEListener](phaselistener.md)
  A central point of reference that defines the location within the scene that’s most audible to the user.
- [class PHASEOccluder](phaseoccluder.md)
  An object with a shape and position that blocks audio from reaching the listener.
- [class PHASEObject](phaseobject.md)
  An object in the scene.
- [class PHASEShape](phaseshape.md)
  A collection of points that connect to form a 3D volume.
- [class PHASEMaterial](phasematerial.md)
  Surface characteristics that determine the acoustic properties of an object.
- [enum PHASEMaterialPreset](phasematerialpreset.md)
  A collection of physical surfaces that each add a unique acoustic quality to your app’s audio.
- [class PHASEMixerParameters](phasemixerparameters.md)
  An object that specifies a mixer for sound events and orients them in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseshape/element)*