# central

**Framework**: Core Bluetooth  
**Kind**: property

The remote central device that originated the request.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var central: CBCentral { get }
```

#### Overview

For more information, see [`Core Bluetooth Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257).

## See Also

- [var characteristic: CBCharacteristic](cbattrequest/characteristic.md)
  The characteristic to read or write the value of.
- [var value: Data?](cbattrequest/value.md)
  The data that the central reads from or writes to the peripheral.
- [var offset: Int](cbattrequest/offset.md)
  The zero-based index of the first byte for the read or write request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbattrequest/central)*