# AnchoringComponent.Target

**Framework**: RealityKit  
**Kind**: enum

Defines the kinds of real world objects to which an anchor entity can be tethered.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
enum Target
```

## Topics

### Basic anchor targets
- [AnchoringComponent.Target.world(transform:)](anchoringcomponent/target-swift.enum/world(transform:).md)
  An anchor point attached to a fixed position in the scene.
- [case plane(AnchoringComponent.Target.Alignment, classification: AnchoringComponent.Target.Classification, minimumBounds: SIMD2<Float>)](anchoringcomponent/target-swift.enum/plane(_:classification:minimumbounds:).md)
  An anchor point attached to a real world surface.
- [AnchoringComponent.Target.camera](anchoringcomponent/target-swift.enum/camera.md)
  An anchor point attached to the device’s camera.
- [AnchoringComponent.Target.anchor(identifier:)](anchoringcomponent/target-swift.enum/anchor(identifier:).md)
  An anchor point attached to the AR anchor with a given identifier.
### Human anchor targets
- [AnchoringComponent.Target.face](anchoringcomponent/target-swift.enum/face.md)
  An anchor point attached to the user’s face.
- [AnchoringComponent.Target.body](anchoringcomponent/target-swift.enum/body.md)
  An anchor point attached to a human body in motion within the scene.
- [case hand(AnchoringComponent.Target.Chirality, location: AnchoringComponent.Target.HandLocation)](anchoringcomponent/target-swift.enum/hand(_:location:).md)
  An anchor point attached to a specific location on the user’s hand.
- [AnchoringComponent.Target.head](anchoringcomponent/target-swift.enum/head.md)
  An anchor point attached to the user’s head.
### Image and object anchor targets
- [AnchoringComponent.Target.image(group:name:)](anchoringcomponent/target-swift.enum/image(group:name:).md)
  An anchor point attached to the image specified by a group and a name in AR Resources.
- [AnchoringComponent.Target.object(group:name:)](anchoringcomponent/target-swift.enum/object(group:name:).md)
  An anchor point attached to the object specified by a group and a name in AR Resources.
### Comparing targets
- [static func == (AnchoringComponent.Target, AnchoringComponent.Target) -> Bool](anchoringcomponent/target-swift.enum/==(_:_:).md)
  Indicates whether two targets are equal.
- [func hash(into: inout Hasher)](anchoringcomponent/target-swift.enum/hash(into:).md)
  Hashes the essential components of the target by feeding them into the given hash function.
### Structures
- [AnchoringComponent.Target.Alignment](anchoringcomponent/target-swift.enum/alignment.md)
  Defines the alignment of real-world surfaces to seek as targets.
- [AnchoringComponent.Target.Classification](anchoringcomponent/target-swift.enum/classification.md)
  Defines types of real-world surfaces to seek as targets.
- [AnchoringComponent.Target.HandLocation](anchoringcomponent/target-swift.enum/handlocation.md)
  Defines the locations of tracked hands to look for.
### Enumeration Cases
- [case accessory(from: AnchoringComponent.AccessoryAnchoringSource, location: AnchoringComponent.AccessoryLocationName)](anchoringcomponent/target-swift.enum/accessory(from:location:).md)
- [case referenceImage(from: AnchoringComponent.ImageAnchoringSource)](anchoringcomponent/target-swift.enum/referenceimage(from:)-52x3p.md)
  An anchor point attached to the image specified by an image anchoring source.
- [case referenceImage(from: AnchoringComponent.ImageAnchoringSource)](anchoringcomponent/target-swift.enum/referenceimage(from:)-7ubtj.md)
  An anchor point attached to the image specified by an image anchoring source.
- [case referenceObject(from: AnchoringComponent.ObjectAnchoringSource)](anchoringcomponent/target-swift.enum/referenceobject(from:)-7yzer.md)
  An anchor point attached to an object that matches the reference of an object anchor.
- [case referenceObject(from: AnchoringComponent.ObjectAnchoringSource)](anchoringcomponent/target-swift.enum/referenceobject(from:)-k3em.md)
  An anchor point attached to an object that matches the reference of an object anchor.
### Enumerations
- [AnchoringComponent.Target.Chirality](anchoringcomponent/target-swift.enum/chirality.md)
  Defines the chirality of tracked hands to look for.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct AnchoringComponent](anchoringcomponent.md)
  A component that anchors virtual content to a real world target.
- [struct ARKitAnchorComponent](arkitanchorcomponent.md)
- [class AnchorEntity](anchorentity.md)
  An anchor that tethers entities to a scene.
- [protocol HasAnchoring](hasanchoring.md)
  An interface that enables anchoring of virtual content to a real-world object in an AR scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/target-swift.enum)*