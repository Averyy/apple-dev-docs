# readRSSI()

**Framework**: Core Bluetooth  
**Kind**: method

Retrieves the current RSSI value for the peripheral while connected to the central manager.

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
func readRSSI()
```

#### Discussion

On macOS, when you call this method to retrieve the Received Signal Strength Indicator (RSSI) of the peripheral while connected to the central manager, the peripheral calls the [`peripheralDidUpdateRSSI(_:error:)`](cbperipheraldelegate/peripheraldidupdaterssi(_:error:).md) method of its delegate object. If retrieving the RSSI value of the peripheral succeeds, you can access it through the peripheral’s [`rssi`](cbperipheral/rssi.md) property.

On iOS and tvOS, when you call this method to retrieve the RSSI of the peripheral while connected to the central manager, the peripheral calls the [`peripheral(_:didReadRSSI:error:)`](cbperipheraldelegate/peripheral(_:didreadrssi:error:).md) method of its delegate object, which includes the RSSI value as a parameter.

## See Also

- [var rssi: NSNumber?](cbperipheral/rssi.md)
  The Received Signal Strength Indicator (RSSI), in decibels, of the peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/readrssi())*