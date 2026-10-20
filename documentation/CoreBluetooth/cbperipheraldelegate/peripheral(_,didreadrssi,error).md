# peripheral(_:didReadRSSI:error:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that retrieving the value of the peripheral’s current Received Signal Strength Indicator (RSSI) succeeded.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func peripheral(_ peripheral: CBPeripheral, didReadRSSI RSSI: NSNumber, error: (any Error)?)
```

```objc
- (void) peripheral:(CBPeripheral *) peripheral didReadRSSI:(NSNumber *) RSSI error:(NSError *) error;
```

#### Discussion

Core Bluetooth invokes this method when your app calls the [`readRSSI()`](../cbperipheral/readrssi%28%29.md) method, while the peripheral is connected to the central manager. If successful, the `error` parameter is `nil` and the parameter `RSSI` reports the peripheral’s signal strength, in decibels. If unsuccessful, the `error` parameter returns the cause of the failure.

## Parameters

- `peripheral`: The peripheral providing this information.
- `RSSI`: The RSSI, in decibels, of the peripheral.
- `error`: The reason the call failed, or `nil` if no error occurred.

## See Also

### Retrieving a Peripheral’s RSSI Data
- [func peripheralDidUpdateRSSI(CBPeripheral, error: (any Error)?)](./peripheraldidupdaterssi%28_,error%29.md)
  Tells the delegate that retrieving the value of the peripheral’s current Received Signal Strength Indicator (RSSI) succeeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheral(_:didreadrssi:error:))*