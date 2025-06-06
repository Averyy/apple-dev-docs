# PHASEObject

**Framework**: PHASE  
**Kind**: class

An object in the scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEObject
```

## Mentions

- [Playing sound from a location in a 3D scene](playing-sound-from-a-location-in-a-3d-scene.md)

#### Overview

This class models a member of your app’s scene by defining a 3D position and orientation.

The following subclasses derive from this class:

The [`children`](phaseobject/children.md) array holds instances of this class to position and orient them relatively.

## Topics

### Creating an Object
- [init(engine: PHASEEngine)](phaseobject/init(engine:).md)
  Creates an object in the scene.
### Managing the Hierarchy
- [var children: [PHASEObject]](phaseobject/children.md)
  Objects that position and orient in the scene relative to the given object.
- [var parent: PHASEObject?](phaseobject/parent.md)
  The object that this instance positions and orients relative to in the scene.
- [func addChild(PHASEObject) throws](phaseobject/addchild(_:).md)
  Adds the given object as a child.
- [func removeChild(PHASEObject)](phaseobject/removechild(_:).md)
  Removes the given object as a child.
- [func removeChildren()](phaseobject/removechildren.md)
  Removes all child objects from the given object.
### Defining a Pose
- [var transform: simd_float4x4](phaseobject/transform.md)
  A matrix, in local coordinates, that determines the object’s pose in the scene.
- [var worldTransform: simd_float4x4](phaseobject/worldtransform.md)
  A matrix, in scene coordinates, that determines the object’s pose in the scene.
### Inspecting the Orientation
- [class var forward: simd_float3](phaseobject/forward.md)
  A vector that points forward in the local coordinate space.
- [class var right: simd_float3](phaseobject/right.md)
  A vector that points right in the local coordinate space.
- [class var up: simd_float3](phaseobject/up.md)
  A vector that points up in the local coordinate space.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [PHASEListener](phaselistener.md)
- [PHASEOccluder](phaseoccluder.md)
- [PHASESource](phasesource.md)
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
- [class PHASEShape](phaseshape.md)
  A collection of points that connect to form a 3D volume.
- [PHASEShape.Element](phaseshape/element.md)
  An object that describes the characteristics of a physical surface.
- [class PHASEMaterial](phasematerial.md)
  Surface characteristics that determine the acoustic properties of an object.
- [enum PHASEMaterialPreset](phasematerialpreset.md)
  A collection of physical surfaces that each add a unique acoustic quality to your app’s audio.
- [class PHASEMixerParameters](phasemixerparameters.md)
  An object that specifies a mixer for sound events and orients them in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseobject)*