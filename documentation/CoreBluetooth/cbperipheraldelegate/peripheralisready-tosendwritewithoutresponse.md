# peripheralIsReady(toSendWriteWithoutResponse:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that a peripheral is again ready to send characteristic updates.

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
optional func peripheralIsReady(toSendWriteWithoutResponse peripheral: CBPeripheral)
```

#### Discussion

The peripheral calls this delegate method after a failed call to [`writeValue(_:for:type:)`](cbperipheral/writevalue(_:for:type:).md), once `peripheral` is ready to send characteristic value updates.

## Parameters

- `peripheral`: The peripheral providing this update.

## See Also

- [func peripheral(CBPeripheral, didWriteValueFor: CBCharacteristic, error: (any Error)?)](cbperipheraldelegate/peripheral(_:didwritevaluefor:error:)-4f5ea.md)
  Tells the delegate that the peripheral successfully set a value for the characteristic.
- [func peripheral(CBPeripheral, didWriteValueFor: CBDescriptor, error: (any Error)?)](cbperipheraldelegate/peripheral(_:didwritevaluefor:error:)-1ybl3.md)
  Tells the delegate that the peripheral successfully set a value for the descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheralisready(tosendwritewithoutresponse:))*