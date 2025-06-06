# maximumCount

**Framework**: HealthKit  
**Kind**: property

The maximum number of heartbeats you can add to the sample.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class var maximumCount: Int { get }
```

#### Discussion

After reaching the maximum count, any attempt to call the [`addHeartbeatWithTimeInterval(sinceSeriesStartDate:precededByGap:completion:)`](hkheartbeatseriesbuilder/addheartbeatwithtimeinterval(sinceseriesstartdate:precededbygap:completion:).md) method fails.

## See Also

- [init(healthStore: HKHealthStore, device: HKDevice?, start: Date)](hkheartbeatseriesbuilder/init(healthstore:device:start:).md)
  Creates a new heartbeat series builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriesbuilder/maximumcount)*