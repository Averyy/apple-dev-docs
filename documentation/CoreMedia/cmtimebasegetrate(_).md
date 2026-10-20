# CMTimebaseGetRate(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern Float64 CMTimebaseGetRate(CMTimebaseRef timebase);
```

#### Discussion

This is the rate relative to its immediate host clock or timebase. For example, if a timebase is running at twice the rate of its host, its rate is 2.0.

## See Also

### Getting and Setting the Time Rate
- [func CMTimebaseGetEffectiveRate(CMTimebase) -> Float64](./cmtimebasegeteffectiverate%28_%29.md)
  Returns the effective rate of a timebase, which combines its rate with the rates of all its host timebases.
- [func CMTimebaseSetRate(CMTimebase, rate: Float64) -> OSStatus](./cmtimebasesetrate%28_,rate%29.md)
  Sets the rate of a timebase.
- [func CMTimebaseSetRateAndAnchorTime(CMTimebase, rate: Float64, anchorTime: CMTime, immediateSourceTime: CMTime) -> OSStatus](./cmtimebasesetrateandanchortime%28_,rate,anchortime,immediatesourcetime%29.md)
  Sets the time of a timebase at a particular host time, and changes the rate at exactly that time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasegetrate(_:))*