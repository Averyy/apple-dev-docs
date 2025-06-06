# peripheral(_:didUpdateNotificationStateFor:error:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that the peripheral received a request to start or stop providing notifications for a specified characteristic’s value.

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
optional func peripheral(_ peripheral: CBPeripheral, didUpdateNotificationStateFor characteristic: CBCharacteristic, error: (any Error)?)
```

#### Discussion

Core Bluetooth invokes this method when your app calls the [`setNotifyValue(_:for:)`](cbperipheral/setnotifyvalue(_:for:).md) method. If successful, the `error` parameter is `nil`. If unsuccessful, the `error` parameter returns the cause of the failure.

## Parameters

- `peripheral`: The peripheral providing this information.
- `characteristic`: The characteristic for which to configure value notifications.
- `error`: The reason the call failed, or   if no error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheral(_:didupdatenotificationstatefor:error:))*