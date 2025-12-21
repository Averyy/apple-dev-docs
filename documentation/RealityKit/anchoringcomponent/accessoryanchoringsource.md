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

### Initializers
- [init(accessory: Accessory) throws](anchoringcomponent/accessoryanchoringsource/init(accessory:).md)
- [init(device: any GCDevice) async throws](anchoringcomponent/accessoryanchoringsource/init(device:).md)
  Creates the accessory anchoring source by the GCDevice asynchronously Returns an AccessoryAnchoringSource if the GCDevice supports spatial tracking, throwing an error otherwise
### Instance Properties
- [var accessoryLocations: [AnchoringComponent.AccessoryLocation]](anchoringcomponent/accessoryanchoringsource/accessorylocations.md)
  The list of anchor-able locations for an AccessoryAnchoringSource Returns an array of Strings
- [var underlyingAccessory: Accessory?](anchoringcomponent/accessoryanchoringsource/underlyingaccessory.md)
### Instance Methods
- [func locationName(named: String) -> AnchoringComponent.AccessoryLocation?](anchoringcomponent/accessoryanchoringsource/locationname(named:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/accessoryanchoringsource)*