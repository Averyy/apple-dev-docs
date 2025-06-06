# CMTimebaseGetRate(_:)

**Framework**: Core Media  
**Kind**: func

Returns the current rate of a timebase.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMTimebaseGetRate(_ timebase: CMTimebase) -> Float64
```

#### Discussion

This is the rate relative to its immediate host clock or timebase. For example, if a timebase is running at twice the rate of its host, its rate is 2.0.

## See Also

- [func CMTimebaseGetEffectiveRate(CMTimebase) -> Float64](cmtimebasegeteffectiverate(_:).md)
  Returns the effective rate of a timebase, which combines its rate with the rates of all its host timebases.
- [func CMTimebaseSetRate(CMTimebase, rate: Float64) -> OSStatus](cmtimebasesetrate(_:rate:).md)
  Sets the rate of a timebase.
- [func CMTimebaseSetRateAndAnchorTime(CMTimebase, rate: Float64, anchorTime: CMTime, immediateSourceTime: CMTime) -> OSStatus](cmtimebasesetrateandanchortime(_:rate:anchortime:immediatesourcetime:).md)
  Sets the time of a timebase at a particular host time, and changes the rate at exactly that time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasegetrate(_:))*