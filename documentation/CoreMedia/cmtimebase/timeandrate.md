# timeAndRate

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

Returns the current time and rate.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var timeAndRate: (time: CMTime, rate: Double) { get }
```

## See Also

### Inspecting Timebases
- [var time: CMTime](./time.md)
  The current time.
- [var rate: Double](./rate.md)
  The current rate relative to its immediate primary clock or timebase.
- [var source: any CMSyncProtocol](./source.md)
  The immediate source that represents the clock or timebase.
- [var sourceClock: CMClock?](./sourceclock.md)
  Returns the immediate source clock, if any.
- [var sourceTimebase: CMTimebase?](./sourcetimebase.md)
  Returns the immediate source timebase, if any.
- [var effectiveRate: Double](./effectiverate.md)
  The effective rate that combines its rate with the rates of all its primary timebases.
- [var ultimateSourceClock: CMClock](./ultimatesourceclock.md)
  Returns the source clock that’s the source of all the other source timebases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebase/timeandrate)*