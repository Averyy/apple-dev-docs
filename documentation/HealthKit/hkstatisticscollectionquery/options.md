# options

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A list of options that define the type of statistical calculations performed and the way in which data from multiple sources are merged.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
var options: HKStatisticsOptions { get }
```

```objc
@property (readonly) HKStatisticsOptions options;
```

#### Discussion

For a list of valid options, see [`HKStatisticsOptions`](../hkstatisticsoptions.md).

## See Also

### Getting Property Data
- [var anchorDate: Date](./anchordate.md)
  The anchor date for the collection’s time intervals.
- [var intervalComponents: DateComponents](./intervalcomponents.md)
  The date components that define the time interval for each statistics object in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery/options)*