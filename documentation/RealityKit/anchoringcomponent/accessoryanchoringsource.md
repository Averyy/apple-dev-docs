# AnchoringComponent.AccessoryAnchoringSource

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct AccessoryAnchoringSource
```

## Topics

### Creating an anchoring source
- [init(type: AnchoringComponent.AccessoryAnchoringSource.AccessoryType, location: String?)](anchoringcomponent/accessoryanchoringsource/init(type:location:).md)
  Creates an accessory anchoring source for a deferred accessory type.
### Specifying the accessory type
- [AnchoringComponent.AccessoryAnchoringSource.AccessoryType](anchoringcomponent/accessoryanchoringsource/accessorytype.md)
  Describes the type of accessory to track.
### Initializers
- [init(accessory: Accessory) throws](anchoringcomponent/accessoryanchoringsource/init(accessory:).md)
- [init(device: any GCDevice) async throws](anchoringcomponent/accessoryanchoringsource/init(device:).md)
  Creates the accessory anchoring source by the GCDevice asynchronously Returns an AccessoryAnchoringSource if the GCDevice supports spatial tracking, throwing an error otherwise
### Instance Properties
- [var accessoryLocations: [AnchoringComponent.AccessoryLocation]](anchoringcomponent/accessoryanchoringsource/accessorylocations.md)
  The list of anchor-able locations for this accessory.
- [var underlyingAccessory: Accessory?](anchoringcomponent/accessoryanchoringsource/underlyingaccessory.md)
  A reference to the root accessory object.
### Instance Methods
- [func locationName(named: String) -> AnchoringComponent.AccessoryLocation?](anchoringcomponent/accessoryanchoringsource/locationname(named:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/accessoryanchoringsource)*