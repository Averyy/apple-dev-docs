# maximumWriteValueLength(for:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSUInteger) maximumWriteValueLengthForType:(CBCharacteristicWriteType) type;
```

## Parameters

- `type`: The characteristic write type to inspect.

## See Also

### Writing Characteristic and Descriptor Values
- [func writeValue(Data, for: CBCharacteristic, type: CBCharacteristicWriteType)](./writevalue%28_,for,type%29.md)
  Writes the value of a characteristic.
- [func writeValue(Data, for: CBDescriptor)](./writevalue%28_,for%29.md)
  Writes the value of a characteristic descriptor.
- [enum CBCharacteristicWriteType](../cbcharacteristicwritetype.md)
  Values representing the possible write types to a characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/maximumwritevaluelength(for:))*