# discoverServices(_:)

**Framework**: Core Bluetooth  
**Kind**: method

Discovers the specified services of the peripheral.

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
func discoverServices(_ serviceUUIDs: [CBUUID]?)
```

#### Discussion

You can provide an array of [`CBUUID`](cbuuid.md) objects—representing service UUIDs—in the `serviceUUIDs` parameter. When you do, the peripheral returns only the services of the peripheral that match the provided UUIDs.

> **Note**:  If the `servicesUUIDs` parameter is `nil`, this method returns all of the peripheral’s available services. This is much slower than providing an array of service UUIDs to search for.

 If the `servicesUUIDs` parameter is `nil`, this method returns all of the peripheral’s available services. This is much slower than providing an array of service UUIDs to search for.

When the peripheral discovers one or more services, it calls the [`peripheral(_:didDiscoverServices:)`](cbperipheraldelegate/peripheral(_:diddiscoverservices:).md): method of its delegate object. After a peripheral discovers services, you can access them through the peripheral’s [`services`](cbperipheral/services.md) property.

## Parameters

- `serviceUUIDs`: An array of   objects that you are interested in. Each   object represents a UUID that identifies the type of service you want to discover.

## See Also

- [func discoverIncludedServices([CBUUID]?, for: CBService)](cbperipheral/discoverincludedservices(_:for:).md)
  Discovers the specified included services of a previously-discovered service.
- [var services: [CBService]?](cbperipheral/services.md)
  A list of a peripheral’s discovered services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/discoverservices(_:))*