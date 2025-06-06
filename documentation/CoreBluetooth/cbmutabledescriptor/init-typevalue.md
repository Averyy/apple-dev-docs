# init(type:value:)

**Framework**: Core Bluetooth  
**Kind**: init

Creates a mutable descriptor with a specified value.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+

## Declaration

```swift
init(type UUID: CBUUID, value: Any?)
```

#### Return Value

A newly initialized mutable descriptor.

#### Discussion

The value type of `value` depends on the type of descriptor:

- The value type of [`CBUUIDCharacteristicUserDescriptionString`](cbuuidcharacteristicuserdescriptionstring.md) is a string you use to provide a human-readable description of the characteristic’s value.
- The value type of a [`CBUUIDCharacteristicFormatString`](cbuuidcharacteristicformatstring.md) is an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object that you use to specify how to format the characteristic’s value for presentation purposes.

If you want to create a local characteristic format descriptor, the descriptor’s value must conform to the attribute value of the characteristic format descriptor as defined in the Bluetooth 4.0 specification, Volume 3, Part G, Section 3.3.3.5.

For more information, see [`Core Bluetooth Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257).

## Parameters

- `UUID`: A 128-bit UUID that identifies the characteristic. You must use only one of the two currently supported descriptor types:   or  . For more details about these descriptor types, see  .
- `value`: The descriptor value to cache. You must provide a non-  value. Once published, you can’t update the value dynamically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmutabledescriptor/init(type:value:))*