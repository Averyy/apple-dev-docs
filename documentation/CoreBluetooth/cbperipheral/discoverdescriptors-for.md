# discoverDescriptors(for:)

**Framework**: Core Bluetooth  
**Kind**: method

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

#### Discussion

When the peripheral discovers one or more descriptors of the specified characteristic, it calls the [`peripheral(_:didDiscoverDescriptorsFor:error:)`](cbperipheraldelegate/peripheral(_:diddiscoverdescriptorsfor:error:).md) method of its delegate object. After the peripheral discovers the descriptors of the characteristic, you can access them through the characteristic’s [`descriptors`](cbcharacteristic/descriptors.md) property.

## Parameters

- `characteristic`: The characteristic whose descriptors you want to discover.

## See Also

- [func discoverCharacteristics([CBUUID]?, for: CBService)](cbperipheral/discovercharacteristics(_:for:).md)
  Discovers the specified characteristics of a service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/discoverdescriptors(for:))*