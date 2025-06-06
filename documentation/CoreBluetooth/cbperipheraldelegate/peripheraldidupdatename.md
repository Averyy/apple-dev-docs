# peripheralDidUpdateName(_:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that a peripheral’s name changed.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func peripheralDidUpdateName(_ peripheral: CBPeripheral)
```

#### Discussion

Core Bluetooth invokes this method whenever the peripheral’s Generic Access Profile (GAP) device name changes. Since a peripheral device can change its GAP device name, you can implement this method if your app needs to display the current name of the peripheral device.

## Parameters

- `peripheral`: The peripheral providing this information.

## See Also

- [func peripheral(CBPeripheral, didModifyServices: [CBService])](cbperipheraldelegate/peripheral(_:didmodifyservices:).md)
  Tells the delegate that a peripheral’s services changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheraldidupdatename(_:))*