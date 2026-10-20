# ASAccessory.SupportOptions

**Framework**: AccessorySetupKit  
**Kind**: struct  
**Role**: Structure

Options of discoverable accessories.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct SupportOptions
```

```c
enum ASAccessorySupportOptions : NSUInteger;
```

## Topics

### Creating an options instance
- [init(rawValue: UInt)](./supportoptions/init%28rawvalue%29.md)
### Bluetooth options
- [static var bluetoothPairingLE: ASAccessory.SupportOptions](./supportoptions/bluetoothpairingle.md)
  The accessory supports Bluetooth Low Energy pairing.
- [static var bluetoothTransportBridging: ASAccessory.SupportOptions](./supportoptions/bluetoothtransportbridging.md)
  The accessory supports bridging to Bluetooth classic transport.
- [static var bluetoothHID: ASAccessory.SupportOptions](./supportoptions/bluetoothhid.md)
  The accessory supports Bluetooth Low Energy HID service.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Specifying options
- [var supportedOptions: ASAccessory.SupportOptions](../asdiscoverydescriptor/supportedoptions.md)
  Options supported by an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessory/supportoptions)*