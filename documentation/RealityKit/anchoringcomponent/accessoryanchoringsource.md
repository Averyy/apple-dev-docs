# AnchoringComponent.AccessoryAnchoringSource

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Defines the source of accessory anchoring target based on how it is created.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct AccessoryAnchoringSource
```

## Topics

### Creating an anchoring source
- [init(type: AnchoringComponent.AccessoryAnchoringSource.AccessoryType, location: String?)](./accessoryanchoringsource/init%28type,location%29.md)
  Creates an accessory anchoring source for a deferred accessory type.
### Specifying the accessory type
- [AnchoringComponent.AccessoryAnchoringSource.AccessoryType](./accessoryanchoringsource/accessorytype.md)
  Describes the type of accessory to track.
### Initializers
- [init(accessory: Accessory) throws](./accessoryanchoringsource/init%28accessory%29.md)
- [init(device: any GCDevice) async throws](./accessoryanchoringsource/init%28device%29.md)
  Creates the accessory anchoring source by the GCDevice asynchronously Returns an AccessoryAnchoringSource if the GCDevice supports spatial tracking, throwing an error otherwise
### Instance Properties
- [var accessoryLocations: [AnchoringComponent.AccessoryLocation]](./accessoryanchoringsource/accessorylocations.md)
  The list of anchor-able locations for this accessory.
- [var underlyingAccessory: Accessory?](./accessoryanchoringsource/underlyingaccessory.md)
  A reference to the root accessory object.
### Instance Methods
- [func locationName(named: String) -> AnchoringComponent.AccessoryLocation?](./accessoryanchoringsource/locationname%28named%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/accessoryanchoringsource)*