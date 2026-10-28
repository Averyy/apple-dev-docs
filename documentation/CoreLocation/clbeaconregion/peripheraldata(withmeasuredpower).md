# peripheralData(withMeasuredPower:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Retrieves data that you can use to advertise the current device as a beacon.

**Availability**:
- iOS 7.0+ - Deprecated in 27.2
- iPadOS 7.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2

## Declaration

```swift
func peripheralData(withMeasuredPower measuredPower: NSNumber?) -> NSMutableDictionary
```

```objc
- (NSMutableDictionary<NSString *,id> *) peripheralDataWithMeasuredPower:(NSNumber *) measuredPower;
```

## Mentions

- [Turning an iOS device into an iBeacon device](../turning-an-ios-device-into-an-ibeacon-device.md)

## Return Value

A dictionary of data that you can use in conjunction with a [`CBPeripheralManager`](../../CoreBluetooth/cbperipheralmanager.md) to advertise the current device as a beacon.

## Discussion

The returned dictionary encodes the beacon’s identifying information, along with other information needed to advertise the beacon. You don’t need to access the dictionary contents directly. Pass the dictionary to the [`startAdvertising(_:)`](../../CoreBluetooth/cbperipheralmanager/startadvertising%28_%29.md) method of a [`CBPeripheralManager`](../../CoreBluetooth/cbperipheralmanager.md) to begin advertising the beacon.

## Parameters

- `measuredPower`: The received signal strength indicator (RSSI) value, measured in decibels, for the device. This value represents the measured strength of the beacon from one meter away that Core Location uses during ranging. Specify `nil` to use the default value for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/peripheraldata(withmeasuredpower:))*