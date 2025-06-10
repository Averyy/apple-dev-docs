# weightedDurationSum

**Framework**: Exposure Notification  
**Kind**: property

The sum of exposure durations weighted by their attenuation.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var weightedDurationSum: TimeInterval { get }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

This value is stored as seconds, rounded up to the next minute. Divide by 60 to convert to minutes when displaying to the user.

[`weightedDurationSum`](enexposuresummaryitem/weighteddurationsum.md) ignores [`infectiousness`](enexposurewindow/infectiousness.md) and [`diagnosisReportType`](enexposurewindow/diagnosisreporttype.md); therefore, it can be nonzero for encounters that have a infectiousness weight or diagnosis report type weight of `0`.

## See Also

- [var maximumScore: Double](enexposuresummaryitem/maximumscore.md)
  The highest score of all exposures for this item.
- [var scoreSum: Double](enexposuresummaryitem/scoresum.md)
  The sum of scores for all exposure for this item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposuresummaryitem/weighteddurationsum)*