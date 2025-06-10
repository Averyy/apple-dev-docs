# Accessory

**Framework**: ARKit  
**Kind**: struct

Represents an accessory to be tracked.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Accessory
```

## Topics

### Structures
- [Accessory.LocationName](accessory/locationname.md)
  Location names to fetch transforms defined on accessories. Some pre-defined location names that are common to accessories conforming to the OpenXR spec are provided as a convenience. These are not required to exist on all accessories.
### Initializers
- [init(device: any GCDevice) async throws](accessory/init(device:).md)
  Initializes an accessory from a GCDevice.
### Instance Properties
- [var description: String](accessory/description.md)
  A textual representation of this accessory.
- [var id: UUID](accessory/id.md)
  The unique identifier of this accessory.
- [var inherentChirality: Accessory.Chirality](accessory/inherentchirality.md)
  The hand that this accessory is designed to be held in.
- [var locations: [Accessory.LocationName]](accessory/locations.md)
  A list of locations on this accessory for which coordinate transforms are provided.
- [var name: String](accessory/name.md)
  The name of the accessory.
- [var source: Accessory.Source](accessory/source-swift.property.md)
  The input source used to create this accessory.
- [var usdzFile: URL?](accessory/usdzfile.md)
  USDZ file representing this accessory, if present.
### Enumerations
- [Accessory.Chirality](accessory/chirality.md)
  The hand which an accessory corresponds to.
- [Accessory.Source](accessory/source-swift.enum.md)
  Type of source an Accessory was loaded from.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/accessory)*