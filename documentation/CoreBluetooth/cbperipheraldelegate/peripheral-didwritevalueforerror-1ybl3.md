# peripheral(_:didWriteValueFor:error:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that the peripheral successfully set a value for the descriptor.

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
optional func peripheral(_ peripheral: CBPeripheral, didWriteValueFor descriptor: CBDescriptor, error: (any Error)?)
```

#### Discussion

Core Bluetooth invokes this method when your app calls the [`writeValue(_:for:)`](cbperipheral/writevalue(_:for:).md) method. If successful, the `error` parameter is `nil`. If unsuccessful, the `error` parameter returns the cause of the failure.

## Parameters

- `peripheral`: The peripheral providing this information.
- `descriptor`: The characteristic descriptor containing the value.
- `error`: The reason the call failed, or   if no error occurred.

## See Also

- [func peripheral(CBPeripheral, didWriteValueFor: CBCharacteristic, error: (any Error)?)](cbperipheraldelegate/peripheral(_:didwritevaluefor:error:)-4f5ea.md)
  Tells the delegate that the peripheral successfully set a value for the characteristic.
- [func peripheralIsReady(toSendWriteWithoutResponse: CBPeripheral)](cbperipheraldelegate/peripheralisready(tosendwritewithoutresponse:).md)
  Tells the delegate that a peripheral is again ready to send characteristic updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheral(_:didwritevaluefor:error:)-1ybl3)*