# ENExposureSummaryItem

**Framework**: Exposure Notification  
**Kind**: class

The summary of exposures for a specific time period or report type.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
class ENExposureSummaryItem
```

#### Overview

> ❗ **Important**:  This class is available in iOS 12.5, iOS 13.7, and later.

 This class is available in iOS 12.5, iOS 13.7, and later.

The exposure summary item provides a summary of exposures for a particular day. The framework computes this summary by compiling values for a [`weightedDurationSum`](enexposuresummaryitem/weighteddurationsum.md), a [`maximumScore`](enexposuresummaryitem/maximumscore.md) (the maximum of the exposure risk values), and a [`scoreSum`](enexposuresummaryitem/scoresum.md). This summary of exposures can be for a specific report type ([`confirmedTestSummary`](enexposuredaysummary/confirmedtestsummary.md)) or a combination across all report types ([`daySummary`](enexposuredaysummary/daysummary.md)). An instance of [`ENExposureDaySummary`](enexposuredaysummary.md) contains the exposure summary item.

To illustrate how the framework computes this value, assume Alice encounters Bob, Carol, and Dave on a particular day; each person has weights set by their respective Public Health Authority.

Bob’s minutes-at-attenuation weight is 50, his infectiousness weight is 100%, and his report type weight is 200% (a confirmed test). His exposure risk value is 100 as dictated by his Public Health Authority.

![A diagram showing that Bob’s exposure risk value is a product of his minutes-at-attenuation weight, infectiousness weight, and report type. ](https://docs-assets.developer.apple.com/published/edb87363ba43f32f6cea7ce3c0e77ea9/media-3744329%402x.png)

Carol’s minutes-at-attenuation weight is 30, her infectiousness weight is 100%, and her report type weight is 100% (a confirmed clinical diagnosis). Her exposure risk value is 30 as dictated by her Public Health Authority.

![A diagram showing that Carol’s exposure risk value is a product of her minutes-at-attenuation weight, infectiousness weight, and report type. ](https://docs-assets.developer.apple.com/published/996e341da3d94c1f1fd0224030a40e9b/media-3744330%402x.png)

Dave’s minutes-at-attenuation weight is 40, his infectiousness weight is 0%, and his report type weight is 80% (a self-diagnosis). His exposure risk value is 0 as dictated by his Public Health Authority.

![A diagram showing that Dave’s exposure risk value is a product of his minutes-at-attenuation weight, infectiousness weight, and report type. ](https://docs-assets.developer.apple.com/published/377c78066bdd32826913eefeea0a53d7/media-3744527%402x.png)

Alice’s exposure summary item for that day would be a [`weightedDurationSum`](enexposuresummaryitem/weighteddurationsum.md) of 120 (50 + 30 + 40), a [`maximumScore`](enexposuresummaryitem/maximumscore.md) of 100 (the maximum of the exposure risk values), and a [`scoreSum`](enexposuresummaryitem/scoresum.md) of 130 (100 + 30).

## Topics

### Getting Summary Properties
- [var maximumScore: Double](enexposuresummaryitem/maximumscore.md)
  The highest score of all exposures for this item.
- [var scoreSum: Double](enexposuresummaryitem/scoresum.md)
  The sum of scores for all exposure for this item.
- [var weightedDurationSum: TimeInterval](enexposuresummaryitem/weighteddurationsum.md)
  The sum of exposure durations weighted by their attenuation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ENExposureDetectionSummary](enexposuredetectionsummary.md)
  A summary of exposures.
- [class ENExposureDaySummary](enexposuredaysummary.md)
  The summary of exposure information for a single day.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposuresummaryitem)*