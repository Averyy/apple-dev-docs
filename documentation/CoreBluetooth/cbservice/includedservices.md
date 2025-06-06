# includedServices

**Framework**: Core Bluetooth  
**Kind**: property

A list of included services discovered in this service.

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
var includedServices: [CBService]? { get }
```

#### Discussion

This array contains [`CBService`](cbservice.md) objects that represent the included services of a service. A service of a peripheral may contain a reference to other services that are available on the peripheral. These other services are the included services of the service. You discover included services using the [`discoverIncludedServices(_:for:)`](cbperipheral/discoverincludedservices(_:for:).md) method of the [`CBPeripheral`](cbperipheral.md) class.

## See Also

- [var characteristics: [CBCharacteristic]?](cbservice/characteristics.md)
  A list of characteristics discovered in this service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbservice/includedservices)*