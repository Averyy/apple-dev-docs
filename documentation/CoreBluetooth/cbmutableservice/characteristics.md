# characteristics

**Framework**: Core Bluetooth  
**Kind**: property

A list of characteristics of a service.

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
var characteristics: [CBCharacteristic]? { get set }
```

#### Discussion

An array containing [`CBCharacteristic`](cbcharacteristic.md) objects that represent a service’s characteristics. Characteristics provide further details about a peripheral’s service. For example, a heart rate service may contain one characteristic that describes the intended body location of the device’s heart rate sensor, while another characteristic transmits heart rate measurement data.

## See Also

- [var includedServices: [CBService]?](cbmutableservice/includedservices.md)
  A list of included services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmutableservice/characteristics)*