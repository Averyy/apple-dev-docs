# AnchoringComponent.AccessoryAnchoringSource.AccessoryType

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Describes the type of accessory to track.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
struct AccessoryType
```

## Topics

### Creating an accessory type
- [init(identifier: String, chirality: AnchoringComponent.Target.Chirality)](./accessorytype/init%28identifier,chirality%29.md)
  Creates a custom accessory type with a uniform type identifier and chirality.
### Accessing predefined types
- [static var eitherController: AnchoringComponent.AccessoryAnchoringSource.AccessoryType](./accessorytype/eithercontroller.md)
  Either left or right game controller.
- [static var leftController: AnchoringComponent.AccessoryAnchoringSource.AccessoryType](./accessorytype/leftcontroller.md)
  A left-handed game controller.
- [static var rightController: AnchoringComponent.AccessoryAnchoringSource.AccessoryType](./accessorytype/rightcontroller.md)
  A right-handed game controller.
- [static var stylus: AnchoringComponent.AccessoryAnchoringSource.AccessoryType](./accessorytype/stylus.md)
  A stylus device.
### Accessing chirality
- [let chirality: AnchoringComponent.Target.Chirality](./accessorytype/chirality.md)
  The chirality of the accessory, if applicable.
### Instance Properties
- [let identifier: String](./accessorytype/identifier.md)
  The uniform type identifier for the accessory.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/accessoryanchoringsource/accessorytype)*