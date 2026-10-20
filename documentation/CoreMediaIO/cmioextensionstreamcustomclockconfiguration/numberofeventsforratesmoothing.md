# numberOfEventsForRateSmoothing

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

The number of events to use for rate smoothing.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var numberOfEventsForRateSmoothing: UInt32 { get }
```

```objc
@property (atomic, readonly) uint32_t numberOfEventsForRateSmoothing;
```

#### Discussion

The property value is always greater than `0`.

## See Also

### Inspecting the Configuration
- [var clockName: String](./clockname.md)
  The name of the clock.
- [var sourceIdentifier: UUID](./sourceidentifier.md)
  A universally unique identifier for the clock.
- [var getTimeCallMinimumInterval: CMTime](./gettimecallminimuminterval.md)
  A minimum call time interval for the clock.
- [var numberOfAveragesForRateSmoothing: UInt32](./numberofaveragesforratesmoothing.md)
  The number of averages to use for rate smoothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamcustomclockconfiguration/numberofeventsforratesmoothing)*