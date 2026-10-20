# services

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (retain, readonly, nullable) NSArray<CBService *> * services;
```

#### Discussion

Returns an array of services (represented by [`CBService`](../cbservice.md) objects) that successful call to the [`discoverServices(_:)`](./discoverservices%28_%29.md) method discovered. If you haven’t yet called the [`discoverServices(_:)`](./discoverservices%28_%29.md) method to discover the services of the peripheral, or if there was an error in doing so, the value of this property is `nil`.

## See Also

### Discovering Services
- [func discoverServices([CBUUID]?)](./discoverservices%28_%29.md)
  Discovers the specified services of the peripheral.
- [func discoverIncludedServices([CBUUID]?, for: CBService)](./discoverincludedservices%28_,for%29.md)
  Discovers the specified included services of a previously-discovered service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/services)*