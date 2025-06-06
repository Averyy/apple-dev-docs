# numberOfAveragesForRateSmoothing

**Framework**: Core Media I/O  
**Kind**: property

The number of averages to use for rate smoothing.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var numberOfAveragesForRateSmoothing: UInt32 { get }
```

#### Discussion

A value of `0` indicates that it uses the default smoothing algorithm.

## See Also

- [var clockName: String](cmioextensionstreamcustomclockconfiguration/clockname.md)
  The name of the clock.
- [var sourceIdentifier: UUID](cmioextensionstreamcustomclockconfiguration/sourceidentifier.md)
  A universally unique identifier for the clock.
- [var getTimeCallMinimumInterval: CMTime](cmioextensionstreamcustomclockconfiguration/gettimecallminimuminterval.md)
  A minimum call time interval for the clock.
- [var numberOfEventsForRateSmoothing: UInt32](cmioextensionstreamcustomclockconfiguration/numberofeventsforratesmoothing.md)
  The number of events to use for rate smoothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamcustomclockconfiguration/numberofaveragesforratesmoothing)*