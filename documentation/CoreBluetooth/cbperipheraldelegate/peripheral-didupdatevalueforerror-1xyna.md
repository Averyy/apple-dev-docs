# peripheral(_:didUpdateValueFor:error:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that retrieving the specified characteristic’s value succeeded, or that the characteristic’s value changed.

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
optional func peripheral(_ peripheral: CBPeripheral, didUpdateValueFor characteristic: CBCharacteristic, error: (any Error)?)
```

#### Discussion

Core Bluetooth invokes this method when your app calls the [`readValue(for:)`](cbperipheral/readvalue(for:)-6u2kr.md) method. A peripheral also invokes this method to notify your app of a change to the value of the characteristic for which the app previously enabled notifications by calling [`setNotifyValue(_:for:)`](cbperipheral/setnotifyvalue(_:for:).md). If successful, the `error` parameter is `nil`. If unsuccessful, the `error` parameter returns the cause of the failure.

## Parameters

- `peripheral`: The peripheral providing this information.
- `characteristic`: The characteristic containing the value.
- `error`: The reason the call failed, or   if no error occurred.

## See Also

- [func peripheral(CBPeripheral, didUpdateValueFor: CBDescriptor, error: (any Error)?)](cbperipheraldelegate/peripheral(_:didupdatevaluefor:error:)-1t3wm.md)
  Tells the delegate that retrieving a specified characteristic descriptor’s value succeeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheral(_:didupdatevaluefor:error:)-1xyna)*