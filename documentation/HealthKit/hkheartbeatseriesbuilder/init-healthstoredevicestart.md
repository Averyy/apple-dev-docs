# init(healthStore:device:start:)

**Framework**: HealthKit  
**Kind**: init

Creates a new heartbeat series builder.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(healthStore: HKHealthStore, device: HKDevice?, start startDate: Date)
```

## Parameters

- `healthStore`: The HealthKit store.
- `device`: An object representing the device that provided the heartbeat data. Pass   if the app is generating its own data.
- `startDate`: The sample’s start date.

## See Also

- [class var maximumCount: Int](hkheartbeatseriesbuilder/maximumcount.md)
  The maximum number of heartbeats you can add to the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriesbuilder/init(healthstore:device:start:))*