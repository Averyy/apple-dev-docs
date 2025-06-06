# getTimeCallMinimumInterval

**Framework**: Core Media I/O  
**Kind**: property

A minimum call time interval for the clock.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var getTimeCallMinimumInterval: CMTime { get }
```

#### Discussion

If you query the clock for its current time more often than this interval, the system returns an interpolated value.

## See Also

- [var clockName: String](cmioextensionstreamcustomclockconfiguration/clockname.md)
  The name of the clock.
- [var sourceIdentifier: UUID](cmioextensionstreamcustomclockconfiguration/sourceidentifier.md)
  A universally unique identifier for the clock.
- [var numberOfEventsForRateSmoothing: UInt32](cmioextensionstreamcustomclockconfiguration/numberofeventsforratesmoothing.md)
  The number of events to use for rate smoothing.
- [var numberOfAveragesForRateSmoothing: UInt32](cmioextensionstreamcustomclockconfiguration/numberofaveragesforratesmoothing.md)
  The number of averages to use for rate smoothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamcustomclockconfiguration/gettimecallminimuminterval)*