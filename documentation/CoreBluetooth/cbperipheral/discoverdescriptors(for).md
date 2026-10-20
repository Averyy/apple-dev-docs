# discoverDescriptors(for:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

Discovers the descriptors of a characteristic.

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
func discoverDescriptors(for characteristic: CBCharacteristic)
```

```objc
- (void) discoverDescriptorsForCharacteristic:(CBCharacteristic *) characteristic;
```

#### Discussion

When the peripheral discovers one or more descriptors of the specified characteristic, it calls the [`peripheral(_:didDiscoverDescriptorsFor:error:)`](../cbperipheraldelegate/peripheral%28_,diddiscoverdescriptorsfor,error%29.md) method of its delegate object. After the peripheral discovers the descriptors of the characteristic, you can access them through the characteristic’s [`descriptors`](../cbcharacteristic/descriptors.md) property.

## Parameters

- `characteristic`: The characteristic whose descriptors you want to discover.

## See Also

### Discovering Characteristics and Descriptors
- [func discoverCharacteristics([CBUUID]?, for: CBService)](./discovercharacteristics%28_,for%29.md)
  Discovers the specified characteristics of a service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/discoverdescriptors(for:))*