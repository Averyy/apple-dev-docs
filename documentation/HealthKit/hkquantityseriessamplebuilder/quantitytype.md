# quantityType

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The quantity type for the series.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@NSCopying
var quantityType: HKQuantityType { get }
```

```objc
@property (copy, readonly) HKQuantityType * quantityType;
```

## See Also

### Creating a Quantity Series Builder
- [init(healthStore: HKHealthStore, quantityType: HKQuantityType, startDate: Date, device: HKDevice?)](./init%28healthstore,quantitytype,startdate,device%29.md)
  Creates a new quantity series builder.
- [var startDate: Date](./startdate.md)
  The starting date and time for the sample.
- [var device: HKDevice?](./device.md)
  The device providing the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplebuilder/quantitytype)*