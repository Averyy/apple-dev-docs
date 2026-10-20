# isPrimary

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the type of service is primary or secondary.

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
var isPrimary: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isPrimary;
```

#### Discussion

A peripheral’s service is either primary or secondary. A primary service describes the primary function of a device. A secondary service describes a service that’s relevant only in the context of another service that references it. For example, the primary service of a heart rate monitor may be to expose heart rate data from the monitor’s heart rate sensor. In this example, a secondary service may be to expose the sensor’s battery data.

If the value of this property is [`true`](../../Swift/true.md), the type of service is primary. If the value of this property is [`false`](../../Swift/false.md), the type of service is secondary.

## See Also

### Identifying a Service
- [var peripheral: CBPeripheral?](./peripheral.md)
  The peripheral to which this service belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbservice/isprimary)*