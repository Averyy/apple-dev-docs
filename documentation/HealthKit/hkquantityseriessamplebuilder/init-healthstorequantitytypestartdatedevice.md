# init(healthStore:quantityType:startDate:device:)

**Framework**: HealthKit  
**Kind**: init

Creates a new quantity series builder.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
init(healthStore: HKHealthStore, quantityType: HKQuantityType, startDate: Date, device: HKDevice?)
```

## Parameters

- `healthStore`: The HealthKit store.
- `quantityType`: The sample’s quantity type.
- `startDate`: The sample’s start date.
- `device`: An object representing the device that provided the data. Pass   if the app is generating its own data.

## See Also

- [var quantityType: HKQuantityType](hkquantityseriessamplebuilder/quantitytype.md)
  The quantity type for the series.
- [var startDate: Date](hkquantityseriessamplebuilder/startdate.md)
  The starting date and time for the sample.
- [var device: HKDevice?](hkquantityseriessamplebuilder/device.md)
  The device providing the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplebuilder/init(healthstore:quantitytype:startdate:device:))*