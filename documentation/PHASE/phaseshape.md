# PHASEShape

**Framework**: PHASE  
**Kind**: class

A collection of points that connect to form a 3D volume.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEShape
```

## Mentions

- [Playing sound from a location in a 3D scene](playing-sound-from-a-location-in-a-3d-scene.md)

#### Overview

To define your scene’s important 3D volumes, create one or more of the following surfaces and add them to your scene’s [`shapes`](phasesource/shapes.md) array:

- The audio-emitting surface of a volumetric [`PHASESource`](phasesource.md)
- The audio-deflecting surface and texture of a [`PHASEOccluder`](phaseoccluder.md)

## Topics

### Creating a Shape
- [init(engine: PHASEEngine, mesh: MDLMesh)](phaseshape/init(engine:mesh:).md)
  Creates an object that the given geometric data shapes.
- [convenience init(engine: PHASEEngine, mesh: MDLMesh, materials: [PHASEMaterial])](phaseshape/init(engine:mesh:materials:).md)
  Creates an object of a specific material that the given geometric data shapes.
### Describing Surface Characteristics
- [var elements: [PHASEShape.Element]](phaseshape/elements.md)
  An array of objects that collectively describe the physical characteristics of a surface.
- [PHASEShape.Element](phaseshape/element.md)
  An object that describes the characteristics of a physical surface.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
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
- [PHASEShape.Element](phaseshape/element.md)
  An object that describes the characteristics of a physical surface.
- [class PHASEMaterial](phasematerial.md)
  Surface characteristics that determine the acoustic properties of an object.
- [enum PHASEMaterialPreset](phasematerialpreset.md)
  A collection of physical surfaces that each add a unique acoustic quality to your app’s audio.
- [class PHASEMixerParameters](phasemixerparameters.md)
  An object that specifies a mixer for sound events and orients them in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseshape)*