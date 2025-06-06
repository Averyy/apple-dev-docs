# value

**Framework**: Core Bluetooth  
**Kind**: property

The value of the descriptor.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var value: Any? { get }
```

#### Discussion

The documentation for [`CBUUID`](cbuuid.md) details the value types for the various descriptor types.

You can read the value of a descriptor by calling the [`readValue(for:)`](cbperipheral/readvalue(for:)-91hhp.md) method of the [`CBPeripheral`](cbperipheral.md) class. You can write the value of a descriptor by calling the [`writeValue(_:for:)`](cbperipheral/writevalue(_:for:).md) method of the [`CBPeripheral`](cbperipheral.md) class. You can’t, however, use the [`writeValue(_:for:)`](cbperipheral/writevalue(_:for:).md) method to write the value of a client configuration descriptor ([`CBUUIDClientCharacteristicConfigurationString`](cbuuidclientcharacteristicconfigurationstring.md)). Instead, you use the [`setNotifyValue(_:for:)`](cbperipheral/setnotifyvalue(_:for:).md) method of the [`CBPeripheral`](cbperipheral.md) class to configure client indications or notifications of a characteristic’s value on a server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbdescriptor/value)*