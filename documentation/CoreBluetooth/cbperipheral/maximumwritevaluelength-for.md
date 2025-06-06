# maximumWriteValueLength(for:)

**Framework**: Core Bluetooth  
**Kind**: method

The maximum amount of data, in bytes, you can send to a characteristic in a single write type.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func maximumWriteValueLength(for type: CBCharacteristicWriteType) -> Int
```

## Parameters

- `type`: The characteristic write type to inspect.

## See Also

- [func writeValue(Data, for: CBCharacteristic, type: CBCharacteristicWriteType)](cbperipheral/writevalue(_:for:type:).md)
  Writes the value of a characteristic.
- [func writeValue(Data, for: CBDescriptor)](cbperipheral/writevalue(_:for:).md)
  Writes the value of a characteristic descriptor.
- [enum CBCharacteristicWriteType](cbcharacteristicwritetype.md)
  Values representing the possible write types to a characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/maximumwritevaluelength(for:))*