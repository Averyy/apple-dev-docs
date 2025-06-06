# peripheral(_:didWriteValueFor:error:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that the peripheral successfully set a value for the characteristic.

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
optional func peripheral(_ peripheral: CBPeripheral, didWriteValueFor characteristic: CBCharacteristic, error: (any Error)?)
```

#### Discussion

Core Bluetooth invokes this method only when your app calls the [`writeValue(_:for:type:)`](cbperipheral/writevalue(_:for:type:).md) method with the [`CBCharacteristicWriteType.withResponse`](cbcharacteristicwritetype/withresponse.md) constant specified as the write type. If successful, the `error` parameter is `nil`. If unsuccessful, the `error` parameter returns the cause of the failure.

## Parameters

- `peripheral`: The peripheral providing this information.
- `characteristic`: The characteristic containing the value.
- `error`: The reason the call failed, or   if no error occurred.

## See Also

- [func peripheral(CBPeripheral, didWriteValueFor: CBDescriptor, error: (any Error)?)](cbperipheraldelegate/peripheral(_:didwritevaluefor:error:)-1ybl3.md)
  Tells the delegate that the peripheral successfully set a value for the descriptor.
- [func peripheralIsReady(toSendWriteWithoutResponse: CBPeripheral)](cbperipheraldelegate/peripheralisready(tosendwritewithoutresponse:).md)
  Tells the delegate that a peripheral is again ready to send characteristic updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheral(_:didwritevaluefor:error:)-4f5ea)*