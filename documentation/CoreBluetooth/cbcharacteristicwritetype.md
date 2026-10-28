# CBCharacteristicWriteType

**Framework**: Core Bluetooth  
**Kind**: enum  
**Role**: Enumeration

Values representing the possible write types to a characteristic’s value.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum CBCharacteristicWriteType
```

```c
enum CBCharacteristicWriteType : NSInteger;
```

## Overview

Characteristic write types have corresponding restrictions on the length of the data that you can write to a characteristic’s value. For the [`CBCharacteristicWriteType.withResponse`](./cbcharacteristicwritetype/withresponse.md) write type’s restrictions, see the Bluetooth 4.0 specification, Volume 3, Part G, Sections 4.9.3–4. For the [`CBCharacteristicWriteType.withoutResponse`](./cbcharacteristicwritetype/withoutresponse.md) write type restrictions, see the Bluetooth 4.0 specification, Volume 3, Part G, Sections 4.9.1–2.

> 💡 **Tip**:  When you write with a response, you can write a characteristic value that’s longer than permitted when you write without a response.

## Topics

### Write Types
- [CBCharacteristicWriteType.withResponse](./cbcharacteristicwritetype/withresponse.md)
  Write a characteristic value, with a response from the peripheral to indicate whether the write was successful.
- [CBCharacteristicWriteType.withoutResponse](./cbcharacteristicwritetype/withoutresponse.md)
  Write a characteristic value, without any response from the peripheral to indicate whether the write was successful.
### Initializers
- [init?(rawValue: Int)](./cbcharacteristicwritetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Writing Characteristic and Descriptor Values
- [func writeValue(Data, for: CBCharacteristic, type: CBCharacteristicWriteType)](./cbperipheral/writevalue%28_,for,type%29.md)
  Writes the value of a characteristic.
- [func writeValue(Data, for: CBDescriptor)](./cbperipheral/writevalue%28_,for%29.md)
  Writes the value of a characteristic descriptor.
- [func maximumWriteValueLength(for: CBCharacteristicWriteType) -> Int](./cbperipheral/maximumwritevaluelength%28for%29.md)
  The maximum amount of data, in bytes, you can send to a characteristic in a single write type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcharacteristicwritetype)*