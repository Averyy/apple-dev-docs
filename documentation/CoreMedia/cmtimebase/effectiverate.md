# effectiveRate

**Framework**: Core Media  
**Kind**: property

The effective rate that combines its rate with the rates of all its primary timebases.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var effectiveRate: Double { get }
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
- [var timeAndRate: (time: CMTime, rate: Double)](cmtimebase/timeandrate.md)
  Returns the current time and rate.
- [var ultimateSourceClock: CMClock](cmtimebase/ultimatesourceclock.md)
  Returns the source clock that’s the source of all the other source timebases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebase/effectiverate)*