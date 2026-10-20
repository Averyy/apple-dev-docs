# includedServices

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

A list of included services.

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
var includedServices: [CBService]? { get set }
```

```objc
@property (retain, readwrite, nullable) NSArray<CBService *> * includedServices;
```

#### Discussion

A service of a peripheral may contain a reference to other services that are available on the peripheral. These other services are the included services of the service.

## See Also

### Managing a Mutable Service
- [var characteristics: [CBCharacteristic]?](./characteristics.md)
  A list of characteristics of a service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmutableservice/includedservices)*