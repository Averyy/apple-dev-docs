# includedServices

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (retain, readonly, nullable) NSArray<CBService *> * includedServices;
```

## Discussion

This array contains [`CBService`](../cbservice.md) objects that represent the included services of a service. A service of a peripheral may contain a reference to other services that are available on the peripheral. These other services are the included services of the service. You discover included services using the [`discoverIncludedServices(_:for:)`](../cbperipheral/discoverincludedservices%28_,for%29.md) method of the [`CBPeripheral`](../cbperipheral.md) class.

## See Also

### Accessing Service Data
- [var characteristics: [CBCharacteristic]?](./characteristics.md)
  A list of characteristics discovered in this service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbservice/includedservices)*