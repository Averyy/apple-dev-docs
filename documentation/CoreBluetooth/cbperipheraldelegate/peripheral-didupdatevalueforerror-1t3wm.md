# peripheral(_:didUpdateValueFor:error:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that retrieving a specified characteristic descriptor’s value succeeded.

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
optional func peripheral(_ peripheral: CBPeripheral, didUpdateValueFor descriptor: CBDescriptor, error: (any Error)?)
```

#### Discussion

Core Bluetooth invokes this method when your app calls the [`readValue(for:)`](cbperipheral/readvalue(for:)-91hhp.md) method. If successful, the `error` parameter is `nil`. If unsuccessful, the `error` parameter returns the cause of the failure.

## Parameters

- `peripheral`: The peripheral providing this information.
- `descriptor`: The characteristic descriptor containing the value.
- `error`: The reason the call failed, or   if no error occurred.

## See Also

- [func peripheral(CBPeripheral, didUpdateValueFor: CBCharacteristic, error: (any Error)?)](cbperipheraldelegate/peripheral(_:didupdatevaluefor:error:)-1xyna.md)
  Tells the delegate that retrieving the specified characteristic’s value succeeded, or that the characteristic’s value changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheral(_:didupdatevaluefor:error:)-1t3wm)*