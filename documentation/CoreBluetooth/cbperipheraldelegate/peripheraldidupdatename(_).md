# peripheralDidUpdateName(_:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) peripheralDidUpdateName:(CBPeripheral *) peripheral;
```

## Discussion

Core Bluetooth invokes this method whenever the peripheral’s Generic Access Profile (GAP) device name changes. Since a peripheral device can change its GAP device name, you can implement this method if your app needs to display the current name of the peripheral device.

## Parameters

- `peripheral`: The peripheral providing this information.

## See Also

### Monitoring Changes to a Peripheral’s Name or Services
- [func peripheral(CBPeripheral, didModifyServices: [CBService])](./peripheral%28_,didmodifyservices%29.md)
  Tells the delegate that a peripheral’s services changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheraldidupdatename(_:))*