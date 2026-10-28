# maximumCount

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, readonly) NSUInteger maximumCount;
```

## Discussion

After reaching the maximum count, any attempt to call the [`addHeartbeatWithTimeInterval(sinceSeriesStartDate:precededByGap:completion:)`](./addheartbeatwithtimeinterval%28sinceseriesstartdate,precededbygap,completion%29.md) method fails.

## See Also

### Creating a Heartbeat Series Builder
- [init(healthStore: HKHealthStore, device: HKDevice?, start: Date)](./init%28healthstore,device,start%29.md)
  Creates a new heartbeat series builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriesbuilder/maximumcount)*