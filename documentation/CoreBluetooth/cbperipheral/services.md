# services

**Framework**: Core Bluetooth  
**Kind**: property

A list of a peripheral’s discovered services.

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
var services: [CBService]? { get }
```

#### Discussion

Returns an array of services (represented by [`CBService`](cbservice.md) objects) that successful call to the [`discoverServices(_:)`](cbperipheral/discoverservices(_:).md) method discovered. If you haven’t yet called the [`discoverServices(_:)`](cbperipheral/discoverservices(_:).md) method to discover the services of the peripheral, or if there was an error in doing so, the value of this property is `nil`.

## See Also

- [func discoverServices([CBUUID]?)](cbperipheral/discoverservices(_:).md)
  Discovers the specified services of the peripheral.
- [func discoverIncludedServices([CBUUID]?, for: CBService)](cbperipheral/discoverincludedservices(_:for:).md)
  Discovers the specified included services of a previously-discovered service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/services)*