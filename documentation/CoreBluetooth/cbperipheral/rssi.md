# rssi

**Framework**: Core Bluetooth  
**Kind**: property

The Received Signal Strength Indicator (RSSI), in decibels, of the peripheral.

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
var rssi: NSNumber? { get }
```

#### Discussion

Returns a number, in decibels, that indicates the RSSI of the peripheral while connected to the central manager. You can use a connected peripheral’s RSSI property to determine the peripheral’s proximity. The default value of this property is `nil`; the first successful call to [`readRSSI()`](cbperipheral/readrssi().md) sets its value.

## See Also

- [func readRSSI()](cbperipheral/readrssi.md)
  Retrieves the current RSSI value for the peripheral while connected to the central manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/rssi)*