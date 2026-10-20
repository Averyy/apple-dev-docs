# bluetoothRange

**Framework**: AccessorySetupKit  
**Kind**: property  
**Role**: Instance Property

A property that tells the session to discover accessories within a specific Bluetooth range.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var bluetoothRange: ASDiscoveryDescriptor.Range { get set }
```

```objc
@property (nonatomic, assign, readwrite) ASDiscoveryDescriptorRange bluetoothRange;
```

## Mentions

- [Discovering and configuring accessories](../discovering-and-configuring-accessories.md)

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
- [ASDiscoveryDescriptor.Range](./range.md)
  The Bluetooth range in which to discover accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asdiscoverydescriptor/bluetoothrange)*