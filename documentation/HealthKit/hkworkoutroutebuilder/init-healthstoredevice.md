# init(healthStore:device:)

**Framework**: HealthKit  
**Kind**: init

Creates and returns a new workout route builder.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(healthStore: HKHealthStore, device: HKDevice?)
```

#### Return Value

A newly initialized workout route builder.

##### Discussion

Use of this initializer is discouraged. Use [`seriesBuilder(for:)`](hkworkoutbuilder/seriesbuilder(for:).md) instead.

## Parameters

- `healthStore`: The HealthKit store.
- `device`: An object representing the device that provided the location data. Pass   if the app is generating its own location data (for example, using  ).

## See Also

- [func seriesBuilder(for: HKSeriesType) -> HKSeriesBuilder?](hkworkoutbuilder/seriesbuilder(for:).md)
  Returns the series builder for the specified type, creating a new builder, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroutebuilder/init(healthstore:device:))*