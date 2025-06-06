# CMTimebaseGetEffectiveRate(_:)

**Framework**: Core Media  
**Kind**: func

Returns the effective rate of a timebase, which combines its rate with the rates of all its host timebases.

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
func CMTimebaseGetEffectiveRate(_ timebase: CMTimebase) -> Float64
```

#### Discussion

Calling `CMTimebaseGetEffectiveRate(timebase)` is equivalent to calling `CMSyncGetRelativeRate(timebase, CMTimebaseGetUltimateMasterClock(timebase))`.

## See Also

- [func CMTimebaseGetRate(CMTimebase) -> Float64](cmtimebasegetrate(_:).md)
  Returns the current rate of a timebase.
- [func CMTimebaseSetRate(CMTimebase, rate: Float64) -> OSStatus](cmtimebasesetrate(_:rate:).md)
  Sets the rate of a timebase.
- [func CMTimebaseSetRateAndAnchorTime(CMTimebase, rate: Float64, anchorTime: CMTime, immediateSourceTime: CMTime) -> OSStatus](cmtimebasesetrateandanchortime(_:rate:anchortime:immediatesourcetime:).md)
  Sets the time of a timebase at a particular host time, and changes the rate at exactly that time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasegeteffectiverate(_:))*