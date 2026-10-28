# characteristics

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

A list of characteristics discovered in this service.

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
var characteristics: [CBCharacteristic]? { get }
```

```objc
@property (retain, readonly, nullable) NSArray<CBCharacteristic *> * characteristics;
```

## Discussion

This array contains [`CBCharacteristic`](../cbcharacteristic.md) objects that represent a service’s characteristics. Characteristics provide further details about a peripheral’s service. For example, a heart rate service may contain one characteristic that describes the intended body location of the device’s heart rate sensor, while another characteristic transmits heart rate measurement data.

## See Also

### Accessing Service Data
- [var includedServices: [CBService]?](./includedservices.md)
  A list of included services discovered in this service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbservice/characteristics)*