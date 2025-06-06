# discoverCharacteristics(_:for:)

**Framework**: Corebluetooth  
**Kind**: method

Discovers the specified characteristics of a service.

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
func discoverCharacteristics(_ characteristicUUIDs: [CBUUID]?, for service: CBService)
```

#### Discussion

You can provide an array of [`CBUUID`](cbuuid.md) objects—representing characteristic UUIDs— in the `characteristicUUIDs` parameter. When you do, the peripheral returns only the characteristics of the service that match the provided UUIDs. If the `characteristicUUIDs` parameter is `nil`, this method returns all characteristics of the service.

> **Note**:  If the `characteristicUUIDs` parameter is `nil`, this method returns all of the service’s characteristics. This is much slower than providing an array of characteristic UUIDs to search for.

When the peripheral discovers one or more characteristics of the specified service, it calls the [`peripheral(_:didDiscoverCharacteristicsFor:error:)`](cbperipheraldelegate/peripheral(_:diddiscovercharacteristicsfor:error:).md) method of its delegate object. After the peripheral discovers the service’s characteristics, you can access them through the service’s [`characteristics`](cbservice/characteristics.md) property.

## Parameters

- `characteristicUUIDs`: An array of   objects that you are interested in. Each   object represents a UUID that identifies the type of a characteristic you want to discover.
- `service`: The service whose characteristics you want to discover.

## See Also

- [func discoverDescriptors(for: CBCharacteristic)](cbperipheral/discoverdescriptors(for:).md)
  Discovers the descriptors of a characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/discovercharacteristics(_:for:))*