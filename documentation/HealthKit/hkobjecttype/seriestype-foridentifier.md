# seriesType(forIdentifier:)

**Framework**: HealthKit  
**Kind**: method

Returns the shared series type for the provided identifier.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func seriesType(forIdentifier identifier: String) -> HKSeriesType?
```

#### Return Value

The shared [`HKSeriesType`](hkseriestype.md) instance based on the provided identifier.

#### Discussion

This method returns an instance of the [`HKSeriesType`](hkseriestype.md) concrete subclass. HealthKit uses series types to represent samples that store a series of items. You can’t directly instantiate these samples; instead, use a [`HKSeriesBuilder`](hkseriesbuilder.md) subclass to create them. Use series types to ask  for permission to read series data from the HealthKit store.

## Parameters

- `identifier`: A series type identifier. In iOS 11 and watchOS 4, there is only one series type identifier:  .

## See Also

- [class func workoutRoute() -> Self](hkseriestype/workoutroute.md)
  Returns a series type object for workout routes.
- [class HKWorkoutRoute](hkworkoutroute.md)
  A sample that contains a workout’s route data.
- [class HKWorkoutRouteBuilder](hkworkoutroutebuilder.md)
  A builder object that incrementally constructs a workout route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobjecttype/seriestype(foridentifier:))*