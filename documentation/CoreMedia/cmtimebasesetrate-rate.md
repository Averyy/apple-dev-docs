# CMTimebaseSetRate(_:rate:)

**Framework**: Core Media  
**Kind**: func

Sets the rate of a timebase.

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
func CMTimebaseSetRate(_ timebase: CMTimebase, rate: Float64) -> OSStatus
```

## See Also

- [func CMTimebaseGetRate(CMTimebase) -> Float64](cmtimebasegetrate(_:).md)
  Returns the current rate of a timebase.
- [func CMTimebaseGetEffectiveRate(CMTimebase) -> Float64](cmtimebasegeteffectiverate(_:).md)
  Returns the effective rate of a timebase, which combines its rate with the rates of all its host timebases.
- [func CMTimebaseSetRateAndAnchorTime(CMTimebase, rate: Float64, anchorTime: CMTime, immediateSourceTime: CMTime) -> OSStatus](cmtimebasesetrateandanchortime(_:rate:anchortime:immediatesourcetime:).md)
  Sets the time of a timebase at a particular host time, and changes the rate at exactly that time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasesetrate(_:rate:))*