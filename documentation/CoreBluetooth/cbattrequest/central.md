# central

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) CBCentral * central;
```

#### Overview

For more information, see [Core Bluetooth Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257).

## See Also

### Requesting to Read and Write Characteristic Values
- [var characteristic: CBCharacteristic](./characteristic.md)
  The characteristic to read or write the value of.
- [var value: Data?](./value.md)
  The data that the central reads from or writes to the peripheral.
- [var offset: Int](./offset.md)
  The zero-based index of the first byte for the read or write request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbattrequest/central)*