# customClockConfigurationWithClockName:sourceIdentifier:getTimeCallMinimumInterval:numberOfEventsForRateSmoothing:numberOfAveragesForRateSmoothing:

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Type Method

Returns a new a custom clock configuration.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```objc
+ (instancetype) customClockConfigurationWithClockName:(NSString *) clockName sourceIdentifier:(NSUUID *) sourceIdentifier getTimeCallMinimumInterval:(CMTime) getTimeCallMinimumInterval numberOfEventsForRateSmoothing:(uint32_t) numberOfEventsForRateSmoothing numberOfAveragesForRateSmoothing:(uint32_t) numberOfAveragesForRateSmoothing;
```

## Return Value

A new custom clock configuration.

## Parameters

- `clockName`: The name of the clock.
- `sourceIdentifier`: A universally unique identifier for the clock.
- `getTimeCallMinimumInterval`: A minimum call time interval for the clock. If you query the clock for its current time more often than this interval, it returns an interpolated value.
- `numberOfEventsForRateSmoothing`: The number of events to use for rate smoothing. This value must be greater than `0`.
- `numberOfAveragesForRateSmoothing`: The number of averages to use for rate smoothing. Specify `0`, to use the default smoothing algorithm.

## See Also

### Creating a Clock Configuration
- [init(clockName: String, sourceIdentifier: UUID, getTimeCallMinimumInterval: CMTime, numberOfEventsForRateSmoothing: UInt32, numberOfAveragesForRateSmoothing: UInt32)](./init%28clockname,sourceidentifier,gettimecallminimuminterval,numberofeventsforratesmoothing,numberofaveragesforratesmoothing%29.md)
  Creates a custom clock configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamcustomclockconfiguration/customclockconfigurationwithclockname:sourceidentifier:gettimecallminimuminterval:numberofeventsforratesmoothing:numberofaveragesforratesmoothing:)*