# getTimeCallMinimumInterval

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

A minimum call time interval for the clock.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var getTimeCallMinimumInterval: CMTime { get }
```

```objc
@property (atomic, readonly) CMTime getTimeCallMinimumInterval;
```

#### Discussion

If you query the clock for its current time more often than this interval, the system returns an interpolated value.

## See Also

### Inspecting the Configuration
- [var clockName: String](./clockname.md)
  The name of the clock.
- [var sourceIdentifier: UUID](./sourceidentifier.md)
  A universally unique identifier for the clock.
- [var numberOfEventsForRateSmoothing: UInt32](./numberofeventsforratesmoothing.md)
  The number of events to use for rate smoothing.
- [var numberOfAveragesForRateSmoothing: UInt32](./numberofaveragesforratesmoothing.md)
  The number of averages to use for rate smoothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamcustomclockconfiguration/gettimecallminimuminterval)*