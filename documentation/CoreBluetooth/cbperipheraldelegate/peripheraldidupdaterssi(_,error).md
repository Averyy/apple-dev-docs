# peripheralDidUpdateRSSI(_:error:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that retrieving the value of the peripheral’s current Received Signal Strength Indicator (RSSI) succeeded.

**Availability**:
- iOS 5.0+ - Deprecated in 8.0
- iPadOS 5.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.13
- tvOS 9.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: in iOS and tvOS, use the [`peripheral(_:didReadRSSI:error:)`](./peripheral%28_,didreadrssi,error%29.md) method instead.

## Declaration

```swift
optional func peripheralDidUpdateRSSI(_ peripheral: CBPeripheral, error: (any Error)?)
```

```objc
- (void) peripheralDidUpdateRSSI:(CBPeripheral *) peripheral error:(NSError *) error;
```

#### Discussion

Core Bluetooth invokes this method when your app calls the [`readRSSI()`](../cbperipheral/readrssi%28%29.md) method, while the peripheral is connected to the central manager. If successful, the `error` parameter is `nil`. If unsuccessful, the `error` parameter returns the cause of the failure.

## Parameters

- `peripheral`: The peripheral providing this information.
- `error`: The reason the call failed, or `nil` if no error occurred.

## See Also

### Retrieving a Peripheral’s RSSI Data
- [func peripheral(CBPeripheral, didReadRSSI: NSNumber, error: (any Error)?)](./peripheral%28_,didreadrssi,error%29.md)
  Tells the delegate that retrieving the value of the peripheral’s current Received Signal Strength Indicator (RSSI) succeeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheraldidupdaterssi(_:error:))*