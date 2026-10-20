# peripheral

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

The peripheral to which this service belongs.

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
weak var peripheral: CBPeripheral? { get }
```

```objc
@property (nonatomic, weak, readonly) CBPeripheral * peripheral;
```

## See Also

### Identifying a Service
- [var isPrimary: Bool](./isprimary.md)
  A Boolean value that indicates whether the type of service is primary or secondary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbservice/peripheral)*