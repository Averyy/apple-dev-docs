# device

**Framework**: HealthKit  
**Kind**: property

The device providing the data.

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
var device: HKDevice? { get }
```

## See Also

- [init(healthStore: HKHealthStore, quantityType: HKQuantityType, startDate: Date, device: HKDevice?)](hkquantityseriessamplebuilder/init(healthstore:quantitytype:startdate:device:).md)
  Creates a new quantity series builder.
- [var quantityType: HKQuantityType](hkquantityseriessamplebuilder/quantitytype.md)
  The quantity type for the series.
- [var startDate: Date](hkquantityseriessamplebuilder/startdate.md)
  The starting date and time for the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplebuilder/device)*