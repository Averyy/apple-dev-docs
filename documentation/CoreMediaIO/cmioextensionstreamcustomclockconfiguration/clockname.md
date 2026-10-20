# clockName

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

The name of the clock.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var clockName: String { get }
```

```objc
@property (atomic, strong, readonly) NSString * clockName;
```

## See Also

### Inspecting the Configuration
- [var sourceIdentifier: UUID](./sourceidentifier.md)
  A universally unique identifier for the clock.
- [var getTimeCallMinimumInterval: CMTime](./gettimecallminimuminterval.md)
  A minimum call time interval for the clock.
- [var numberOfEventsForRateSmoothing: UInt32](./numberofeventsforratesmoothing.md)
  The number of events to use for rate smoothing.
- [var numberOfAveragesForRateSmoothing: UInt32](./numberofaveragesforratesmoothing.md)
  The number of averages to use for rate smoothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamcustomclockconfiguration/clockname)*