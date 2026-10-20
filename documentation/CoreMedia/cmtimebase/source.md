# source

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

The immediate source that represents the clock or timebase.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var source: any CMSyncProtocol { get set }
```

## See Also

### Inspecting Timebases
- [var time: CMTime](./time.md)
  The current time.
- [var rate: Double](./rate.md)
  The current rate relative to its immediate primary clock or timebase.
- [var sourceClock: CMClock?](./sourceclock.md)
  Returns the immediate source clock, if any.
- [var sourceTimebase: CMTimebase?](./sourcetimebase.md)
  Returns the immediate source timebase, if any.
- [var effectiveRate: Double](./effectiverate.md)
  The effective rate that combines its rate with the rates of all its primary timebases.
- [var timeAndRate: (time: CMTime, rate: Double)](./timeandrate.md)
  Returns the current time and rate.
- [var ultimateSourceClock: CMClock](./ultimatesourceclock.md)
  Returns the source clock that’s the source of all the other source timebases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebase/source)*