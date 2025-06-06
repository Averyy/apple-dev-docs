# ultimateSourceClock

**Framework**: Core Media  
**Kind**: property

Returns the source clock that’s the source of all the other source timebases.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var ultimateSourceClock: CMClock { get }
```

## See Also

- [var time: CMTime](cmtimebase/time.md)
  The current time.
- [var rate: Double](cmtimebase/rate.md)
  The current rate relative to its immediate primary clock or timebase.
- [var source: any CMSyncProtocol](cmtimebase/source.md)
  The immediate source that represents the clock or timebase.
- [var sourceClock: CMClock?](cmtimebase/sourceclock.md)
  Returns the immediate source clock, if any.
- [var sourceTimebase: CMTimebase?](cmtimebase/sourcetimebase.md)
  Returns the immediate source timebase, if any.
- [var effectiveRate: Double](cmtimebase/effectiverate.md)
  The effective rate that combines its rate with the rates of all its primary timebases.
- [var timeAndRate: (time: CMTime, rate: Double)](cmtimebase/timeandrate.md)
  Returns the current time and rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebase/ultimatesourceclock)*