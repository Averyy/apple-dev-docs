# sourceIdentifier

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

A universally unique identifier for the clock.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var sourceIdentifier: UUID { get }
```

```objc
@property (atomic, strong, readonly) NSUUID * sourceIdentifier;
```

## See Also

### Inspecting the Configuration
- [var clockName: String](./clockname.md)
  The name of the clock.
- [var getTimeCallMinimumInterval: CMTime](./gettimecallminimuminterval.md)
  A minimum call time interval for the clock.
- [var numberOfEventsForRateSmoothing: UInt32](./numberofeventsforratesmoothing.md)
  The number of events to use for rate smoothing.
- [var numberOfAveragesForRateSmoothing: UInt32](./numberofaveragesforratesmoothing.md)
  The number of averages to use for rate smoothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamcustomclockconfiguration/sourceidentifier)*