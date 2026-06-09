# AnchoringComponent.AccessoryAnchoringSource.AccessoryType

**Framework**: RealityKit  
**Kind**: struct

Describes the type of accessory to track.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct AccessoryType
```

## Topics

### Creating an accessory type
- [init(identifier: String, chirality: AnchoringComponent.Target.Chirality)](anchoringcomponent/accessoryanchoringsource/accessorytype/init(identifier:chirality:).md)
  Creates a custom accessory type with a uniform type identifier and chirality.
### Accessing predefined types
- [static var eitherController: AnchoringComponent.AccessoryAnchoringSource.AccessoryType](anchoringcomponent/accessoryanchoringsource/accessorytype/eithercontroller.md)
  Either left or right game controller.
- [static var leftController: AnchoringComponent.AccessoryAnchoringSource.AccessoryType](anchoringcomponent/accessoryanchoringsource/accessorytype/leftcontroller.md)
  A left-handed game controller.
- [static var rightController: AnchoringComponent.AccessoryAnchoringSource.AccessoryType](anchoringcomponent/accessoryanchoringsource/accessorytype/rightcontroller.md)
  A right-handed game controller.
- [static var stylus: AnchoringComponent.AccessoryAnchoringSource.AccessoryType](anchoringcomponent/accessoryanchoringsource/accessorytype/stylus.md)
  A stylus device.
### Accessing chirality
- [let chirality: AnchoringComponent.Target.Chirality](anchoringcomponent/accessoryanchoringsource/accessorytype/chirality.md)
  The chirality of the accessory, if applicable.
### Instance Properties
- [let identifier: String](anchoringcomponent/accessoryanchoringsource/accessorytype/identifier.md)
  The uniform type identifier for the accessory.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/accessoryanchoringsource/accessorytype)*