# DeviceActivityFilter.SegmentInterval.daily(during:)

**Framework**: DeviceActivity  
**Kind**: case

Indicates that the system aggregates data into daily segments within the specified interval.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
case daily(during: DateInterval)
```

#### Discussion

The system disregards any date components in the interval that are smaller than `.day` and instead uses the start of the day specified by `interval.start` and the end of the day specified by `interval.end`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityfilter/segmentinterval-swift.enum/daily(during:))*