# peripheral(_:didDiscoverCharacteristicsFor:error:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that the peripheral found characteristics for a service.

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
optional func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error: (any Error)?)
```

#### Discussion

Core Bluetooth invokes this method when your app calls the [`discoverCharacteristics(_:for:)`](cbperipheral/discovercharacteristics(_:for:).md) method. If the peripheral successfully discovers the characteristics of the specified service, you can access them through the service’s [`characteristics`](cbservice/characteristics.md) property. If successful, the `error` parameter is `nil`. If unsuccessful, the `error` parameter returns the cause of the failure.

## Parameters

- `peripheral`: The peripheral providing this information.
- `service`: The service to which the characteristics belong.
- `error`: The reason the call failed, or   if no error occurred.

## See Also

- [func peripheral(CBPeripheral, didDiscoverDescriptorsFor: CBCharacteristic, error: (any Error)?)](cbperipheraldelegate/peripheral(_:diddiscoverdescriptorsfor:error:).md)
  Tells the delegate that the peripheral found descriptors for a characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheral(_:diddiscovercharacteristicsfor:error:))*