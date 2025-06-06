# init(clockName:sourceIdentifier:getTimeCallMinimumInterval:numberOfEventsForRateSmoothing:numberOfAveragesForRateSmoothing:)

**Framework**: Core Media I/O  
**Kind**: init

Creates a custom clock configuration.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
init(clockName: String, sourceIdentifier: UUID, getTimeCallMinimumInterval: CMTime, numberOfEventsForRateSmoothing: UInt32, numberOfAveragesForRateSmoothing: UInt32)
```

## Parameters

- `clockName`: The name of the clock.
- `sourceIdentifier`: A universally unique identifier for the clock.
- `getTimeCallMinimumInterval`: A minimum call time interval for the clock. If you query the clock for its current time more often than this interval, it returns an interpolated value.
- `numberOfEventsForRateSmoothing`: The number of events to use for rate smoothing. This value must be greater than  .
- `numberOfAveragesForRateSmoothing`: The number of averages to use for rate smoothing. Specify  , to use the default smoothing algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamcustomclockconfiguration/init(clockname:sourceidentifier:gettimecallminimuminterval:numberofeventsforratesmoothing:numberofaveragesforratesmoothing:))*