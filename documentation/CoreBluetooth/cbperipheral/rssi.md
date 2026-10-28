# rssi

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

The Received Signal Strength Indicator (RSSI), in decibels, of the peripheral.

**Availability**:
- iOS 5.0+ - Deprecated in 8.0
- iPadOS 5.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.13
- tvOS 9.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: On iOS and tvOS, when you call the [`readRSSI()`](./readrssi%28%29.md) method, the system returns the RSSI as a parameter in a call to the delegate’s [`peripheral(_:didReadRSSI:error:)`](../cbperipheraldelegate/peripheral%28_,didreadrssi,error%29.md) method. Use that value instead.

## Declaration

```swift
var rssi: NSNumber? { get }
```

```objc
@property (retain, readonly, nullable) NSNumber * RSSI;
```

## Discussion

Returns a number, in decibels, that indicates the RSSI of the peripheral while connected to the central manager. You can use a connected peripheral’s RSSI property to determine the peripheral’s proximity. The default value of this property is `nil`; the first successful call to [`readRSSI()`](./readrssi%28%29.md) sets its value.

## See Also

### Accessing a Peripheral’s Signal Strength
- [func readRSSI()](./readrssi%28%29.md)
  Retrieves the current RSSI value for the peripheral while connected to the central manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/rssi)*