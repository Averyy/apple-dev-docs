# peripheral(_:didDiscoverDescriptorsFor:error:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the peripheral found descriptors for a characteristic.

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
optional func peripheral(_ peripheral: CBPeripheral, didDiscoverDescriptorsFor characteristic: CBCharacteristic, error: (any Error)?)
```

```objc
- (void) peripheral:(CBPeripheral *) peripheral didDiscoverDescriptorsForCharacteristic:(CBCharacteristic *) characteristic error:(NSError *) error;
```

## Discussion

Core Bluetooth invokes this method when your app calls the [`discoverDescriptors(for:)`](../cbperipheral/discoverdescriptors%28for%29.md) method. If the peripheral successfully discovers the descriptors of the specified characteristic, you can access them through the characteristic’s [`descriptors`](../cbcharacteristic/descriptors.md) property. If successful, the `error` parameter is `nil`. If unsuccessful, the `error` parameter returns the cause of the failure.

## Parameters

- `peripheral`: The peripheral providing this information.
- `characteristic`: The characteristic to which the characteristic descriptors belong.
- `error`: The reason the call failed, or `nil` if no error occurred.

## See Also

### Discovering Characteristics and their Descriptors
- [func peripheral(CBPeripheral, didDiscoverCharacteristicsFor: CBService, error: (any Error)?)](./peripheral%28_,diddiscovercharacteristicsfor,error%29.md)
  Tells the delegate that the peripheral found characteristics for a service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheral(_:diddiscoverdescriptorsfor:error:))*