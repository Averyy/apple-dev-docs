# bluetoothNameSubstringCompareOptions

**Framework**: AccessorySetupKit  
**Kind**: property  
**Role**: Instance Property

The accessory’s over-the-air Bluetooth name substring compare options.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
var bluetoothNameSubstringCompareOptions: NSString.CompareOptions { get set }
```

```objc
@property (nonatomic, assign, readwrite) NSStringCompareOptions bluetoothNameSubstringCompareOptions;
```

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
- [var bluetoothServiceUUID: CBUUID?](./bluetoothserviceuuid.md)
  The accessory’s Bluetooth service UUID.
- [var bluetoothRange: ASDiscoveryDescriptor.Range](./bluetoothrange.md)
  A property that tells the session to discover accessories within a specific Bluetooth range.
- [ASDiscoveryDescriptor.Range](./range.md)
  The Bluetooth range in which to discover accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asdiscoverydescriptor/bluetoothnamesubstringcompareoptions)*