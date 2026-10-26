# init(reportToPersistenceDelayTime:reportToPersistenceDelayTimeMax:recentReportTimesMaxCount:timeBetweenReportsTooShortThreshold:timeBetweenReportsTooShortMinThreshold:reportToPersistenceDelayMaxMultiplier:deviceReportingExcessivelyIntervalThreshold:)

**Framework**: Matter  
**Kind**: init  
**Role**: Initializer

Create configuration with specified values. See description below for details, and the list of properties below for valid ranges of these values.

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
convenience init(reportToPersistenceDelayTime: TimeInterval, reportToPersistenceDelayTimeMax: TimeInterval, recentReportTimesMaxCount: Int, timeBetweenReportsTooShortThreshold: TimeInterval, timeBetweenReportsTooShortMinThreshold: TimeInterval, reportToPersistenceDelayMaxMultiplier: Double, deviceReportingExcessivelyIntervalThreshold: TimeInterval)
```

```objc
+ (instancetype) configurationWithReportToPersistenceDelayTime:(NSTimeInterval) reportToPersistenceDelayTime reportToPersistenceDelayTimeMax:(NSTimeInterval) reportToPersistenceDelayTimeMax recentReportTimesMaxCount:(NSUInteger) recentReportTimesMaxCount timeBetweenReportsTooShortThreshold:(NSTimeInterval) timeBetweenReportsTooShortThreshold timeBetweenReportsTooShortMinThreshold:(NSTimeInterval) timeBetweenReportsTooShortMinThreshold reportToPersistenceDelayMaxMultiplier:(double) reportToPersistenceDelayMaxMultiplier deviceReportingExcessivelyIntervalThreshold:(NSTimeInterval) deviceReportingExcessivelyIntervalThreshold;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicestoragebehaviorconfiguration/init(reporttopersistencedelaytime:reporttopersistencedelaytimemax:recentreporttimesmaxcount:timebetweenreportstooshortthreshold:timebetweenreportstooshortminthreshold:reporttopersistencedelaymaxmultiplier:devicereportingexcessivelyintervalt-6xgqf)*