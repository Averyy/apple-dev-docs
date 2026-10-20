# ASDiscoveryDescriptor.Range

**Framework**: AccessorySetupKit  
**Kind**: enum  
**Role**: Enumeration

The Bluetooth range in which to discover accessories.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum Range
```

```c
enum ASDiscoveryDescriptorRange : NSInteger;
```

## Topics

### Creating an options instance
- [init?(rawValue: Int)](./range/init%28rawvalue%29.md)
### Bluetooth options
- [ASDiscoveryDescriptor.Range.default](./range/default.md)
  The default range in which to discover accessories.
- [ASDiscoveryDescriptor.Range.immediate](./range/immediate.md)
  A range in the immediate vicinity of the device performing accessory discovery.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying Bluetooth properties
- [var bluetoothCompanyIdentifier: ASBluetoothCompanyIdentifier](./bluetoothcompanyidentifier.md)
  The accessory’s 16-bit Bluetooth Company Identifier.
- [struct ASBluetoothCompanyIdentifier](../asbluetoothcompanyidentifier.md)
  The type used to identify a Bluetooth accessory provider.
- [struct ASBluetoothCompanyIdentifier](../asbluetoothcompanyidentifier.md)
  The type used to identify a Bluetooth accessory provider.
- [var bluetoothManufacturerDataBlob: Data?](./bluetoothmanufacturerdatablob.md)
  A byte buffer that matches the accessory’s Bluetooth manufacturer data.
- [var bluetoothManufacturerDataMask: Data?](./bluetoothmanufacturerdatamask.md)
  The accessory’s Bluetooth manufacturer data mask.
- [var bluetoothServiceDataBlob: Data?](./bluetoothservicedatablob.md)
  A byte buffer that matches the accessory’s Bluetooth service data.
- [var bluetoothServiceDataMask: Data?](./bluetoothservicedatamask.md)
  The accessory’s Bluetooth service data mask.
- [var bluetoothNameSubstring: String?](./bluetoothnamesubstring.md)
  The accessory’s over-the-air Bluetooth name substring.
- [var bluetoothNameSubstringCompareOptions: NSString.CompareOptions](./bluetoothnamesubstringcompareoptions.md)
  The accessory’s over-the-air Bluetooth name substring compare options.
- [var bluetoothServiceUUID: CBUUID?](./bluetoothserviceuuid.md)
  The accessory’s Bluetooth service UUID.
- [var bluetoothRange: ASDiscoveryDescriptor.Range](./bluetoothrange.md)
  A property that tells the session to discover accessories within a specific Bluetooth range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asdiscoverydescriptor/range)*