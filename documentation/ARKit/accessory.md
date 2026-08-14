# Accessory

**Framework**: ARKit  
**Kind**: struct

Represents an accessory to be tracked.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct Accessory
```

## Topics

### Structures
- [Accessory.LocationName](accessory/locationname.md)
  Location names to fetch transforms defined on accessories. Some pre-defined location names that are common to accessories conforming to the OpenXR spec are provided as a convenience. These are not required to exist on all accessories.
### Operators
- [static func == (Accessory, Accessory) -> Bool](accessory/==(_:_:).md)
  Returns a Boolean value indicating whether two accessories are equal.
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
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Preparing spatial accessories for tracking in your visionOS app](preparing-spatial-accessories-for-tracking-in-your-visionos-app.md)
  Prepare a spatial accessory for tracking by training a reference accessory file and integrating it into your visionOS app.
- [Working with generic spatial accessories](../visionos/working-with-generic-spatial-accessories.md)
  Let people place digital replicas of a generic spatial accessory by tracking the accessory with ARKit.
- [class AccessoryTrackingProvider](accessorytrackingprovider.md)
  Provides the real time position of accessories in the user’s environment.
- [struct AccessoryAnchor](accessoryanchor.md)
  Represents a tracked accessory.
- [Tracking accessories in volumetric windows](tracking-accessories-in-volumetric-windows.md)
  Translate the position and velocity of tracked handheld accessories to throw virtual balls at a stack of cans.
- [Tracking a handheld accessory as a virtual sculpting tool](tracking-a-handheld-accessory-as-a-virtual-sculpting-tool.md)
  Use a tracked accessory with Apple Vision Pro to create a virtual sculpture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/accessory)*