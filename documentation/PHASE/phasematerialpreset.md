# PHASEMaterialPreset

**Framework**: PHASE  
**Kind**: enum

A collection of physical surfaces that each add a unique acoustic quality to your app’s audio.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum PHASEMaterialPreset
```

## Mentions

- [Playing sound from a location in a 3D scene](playing-sound-from-a-location-in-a-3d-scene.md)

#### Overview

This enumeration defines the types of surface texture that you choose for your scene’s objects. To assign a preset to a material, define the `preset` argument for the material’s [`init(engine:preset:)`](phasematerial/init(engine:preset:).md) initializer.

## Topics

### Presets
- [PHASEMaterialPreset.brick](phasematerialpreset/brick.md)
  A surface characteristic that produces the acoustic quality of brick.
- [PHASEMaterialPreset.cardboard](phasematerialpreset/cardboard.md)
  A surface characteristic that produces the acoustic quality of cardboard.
- [PHASEMaterialPreset.concrete](phasematerialpreset/concrete.md)
  A surface characteristic that produces the acoustic quality of concrete.
- [PHASEMaterialPreset.drywall](phasematerialpreset/drywall.md)
  A surface characteristic that produces the acoustic quality of drywall.
- [PHASEMaterialPreset.glass](phasematerialpreset/glass.md)
  A surface characteristic that produces the acoustic quality of glass.
- [PHASEMaterialPreset.wood](phasematerialpreset/wood.md)
  A surface characteristic that produces the acoustic quality of wood.
### Initializers
- [init?(rawValue: Int)](phasematerialpreset/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [PHASEShape.Element](phaseshape/element.md)
  An object that describes the characteristics of a physical surface.
- [class PHASEMaterial](phasematerial.md)
  Surface characteristics that determine the acoustic properties of an object.
- [class PHASEMixerParameters](phasemixerparameters.md)
  An object that specifies a mixer for sound events and orients them in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasematerialpreset)*