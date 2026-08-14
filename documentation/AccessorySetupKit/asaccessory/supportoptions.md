# ASAccessory.SupportOptions

**Framework**: AccessorySetupKit  
**Kind**: struct

Options of discoverable accessories.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct SupportOptions
```

## Topics

### Creating an options instance
- [init(rawValue: UInt)](asaccessory/supportoptions/init(rawvalue:).md)
### Bluetooth options
- [static var bluetoothPairingLE: ASAccessory.SupportOptions](asaccessory/supportoptions/bluetoothpairingle.md)
  The accessory supports Bluetooth Low Energy pairing.
- [static var bluetoothTransportBridging: ASAccessory.SupportOptions](asaccessory/supportoptions/bluetoothtransportbridging.md)
  The accessory supports bridging to Bluetooth classic transport.
- [static var bluetoothHID: ASAccessory.SupportOptions](asaccessory/supportoptions/bluetoothhid.md)
  The accessory supports Bluetooth Low Energy HID service.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [var supportedOptions: ASAccessory.SupportOptions](asdiscoverydescriptor/supportedoptions.md)
  Options supported by an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessory/supportoptions)*