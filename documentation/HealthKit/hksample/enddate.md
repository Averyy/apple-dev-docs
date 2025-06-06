# endDate

**Framework**: HealthKit  
**Kind**: property

The sample’s end date.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var endDate: Date { get }
```

## Mentions

- [Adding samples to a workout](adding-samples-to-a-workout.md)

#### Discussion

The sample’s end date must be equal to or later than its start date.

Some samples—for example, body temperature—represent a single point in time. For these samples, both the start and the end date are the same, because they both refer to the point in time when the sample was taken.

Other samples—for example, step count—represent data over a time interval. Here, the sample should use different start and end dates. These dates mark the beginning and end of the sample’s time interval, respectively.

## See Also

- [var startDate: Date](hksample/startdate.md)
  The sample’s start date.
- [var hasUndeterminedDuration: Bool](hksample/hasundeterminedduration.md)
  Indicates whether the sample has an unknown duration.
- [var sampleType: HKSampleType](hksample/sampletype.md)
  The sample type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksample/enddate)*