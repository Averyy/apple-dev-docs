# GCSpatialAccessory

**Framework**: Game Controller  
**Kind**: class  
**Role**: Class

**Availability**:
- visionOS 27.0+

## Declaration

```swift
class GCSpatialAccessory
```

```objc
@interface GCSpatialAccessory : NSObject
```

## Topics

### Structures
- [GCSpatialAccessory.DidConnectMessage](./gcspatialaccessory/didconnectmessage.md)
  A message that posts after a spatial accessory connects to the device.
- [GCSpatialAccessory.DidDisconnectMessage](./gcspatialaccessory/diddisconnectmessage.md)
  A message that posts after a spatial accessory disconnects from the device.
### Instance Properties
- [var haptics: GCDeviceHaptics?](./gcspatialaccessory/haptics.md)
  Gets the haptics for the device, if supported.
- [var input: (any GCDevicePhysicalInput)?](./gcspatialaccessory/input.md)
  Gets the input profile for the device.
### Instance Methods
- [func conforms(to: GCDeviceType) -> Bool](./gcspatialaccessory/conforms%28to%29.md)
  Tests the conformance of the receiver to the provided device type.
### Type Properties
- [class var spatialAccessories: [GCSpatialAccessory]](./gcspatialaccessory/spatialaccessories.md)
  Get the collection of spatial accessories currently connected to the system.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [GCDevice](./gcdevice.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcspatialaccessory)*