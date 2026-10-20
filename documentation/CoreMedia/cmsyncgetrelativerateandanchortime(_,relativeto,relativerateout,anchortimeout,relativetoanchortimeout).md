# CMSyncGetRelativeRateAndAnchorTime(_:relativeTo:relativeRateOut:anchorTimeOut:relativeToAnchorTimeOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the relative rate of one timebase or clock relative to another timebase or clock and the times of each timebase or clock at which the relative rate went into effect.

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
func CMSyncGetRelativeRateAndAnchorTime(_ ofClockOrTimebase: CMClockOrTimebase, relativeTo relativeToClockOrTimebase: CMClockOrTimebase, relativeRateOut outRelativeRate: UnsafeMutablePointer<Float64>?, anchorTimeOut outOfClockOrTimebaseAnchorTime: UnsafeMutablePointer<CMTime>?, relativeToAnchorTimeOut outRelativeToClockOrTimebaseAnchorTime: UnsafeMutablePointer<CMTime>?) -> OSStatus
```

```c
extern OSStatus CMSyncGetRelativeRateAndAnchorTime(CMClockOrTimebaseRef ofClockOrTimebase, CMClockOrTimebaseRef relativeToClockOrTimebase, Float64 *outRelativeRate, CMTime *outOfClockOrTimebaseAnchorTime, CMTime *outRelativeToClockOrTimebaseAnchorTime);
```

#### Discussion

If both have a common host, the function syncs the clock or timebase based on the rates in the common tree rooted in that host.

If they have different host clocks (or are both clocks), this calculation takes into account the measured drift between the two clocks, using host time as a pivot. The rate of a moving timebase relative to a stopped timebase is a NaN.

## See Also

### Getting and Syncing Time
- [func CMSyncGetTime(CMClockOrTimebase) -> CMTime](./cmsyncgettime%28_%29.md)
  Returns the time from a clock or timebase.
- [func CMSyncGetRelativeRate(CMClockOrTimebase, relativeTo: CMClockOrTimebase) -> Float64](./cmsyncgetrelativerate%28_,relativeto%29.md)
  Returns the relative rate of one timebase or clock relative to another timebase or clock.
- [func CMSyncConvertTime(CMTime, from: CMClockOrTimebase, to: CMClockOrTimebase) -> CMTime](./cmsyncconverttime%28_,from,to%29.md)
  Converts a time from one timebase or clock to another timebase or clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsyncgetrelativerateandanchortime(_:relativeto:relativerateout:anchortimeout:relativetoanchortimeout:))*