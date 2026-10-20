# CMTimebaseSetAnchorTime(_:timebaseTime:immediateMasterTime:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Sets the time of a timebase at a particular source time.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0 (renamed: CMTimebaseSetAnchorTime(_:timebaseTime:immediateSourceTime:))
- iPadOS 6.0+ - Deprecated in 15.0 (renamed: CMTimebaseSetAnchorTime(_:timebaseTime:immediateSourceTime:))
- Mac Catalyst 6.0+ - Deprecated in 15.0 (renamed: CMTimebaseSetAnchorTime(_:timebaseTime:immediateSourceTime:))
- macOS 10.8+ - Deprecated in 12.0 (renamed: CMTimebaseSetAnchorTime(_:timebaseTime:immediateSourceTime:))
- tvOS 9.0+ - Deprecated in 15.0 (renamed: CMTimebaseSetAnchorTime(_:timebaseTime:immediateSourceTime:))
- visionOS
- watchOS 6.0+ - Deprecated in 8.0 (renamed: CMTimebaseSetAnchorTime(_:timebaseTime:immediateSourceTime:))

> **Deprecated**: Use [`CMTimebaseSetAnchorTime(_:timebaseTime:immediateSourceTime:)`](./cmtimebasesetanchortime%28_,timebasetime,immediatesourcetime%29.md) instead.

## Declaration

```swift
func CMTimebaseSetAnchorTime(_ timebase: CMTimebase, timebaseTime: CMTime, immediateMasterTime: CMTime)
```

## See Also

### Deprecations
- [func CMTimebaseSetRateAndAnchorTime(CMTimebase, rate: Double, anchorTime: CMTime, immediateMasterTime: CMTime)](./cmtimebasesetrateandanchortime%28_,rate,anchortime,immediatemastertime%29.md)
- [func CMTimebaseGetMasterTimebase(CMTimebase) -> CMTimebase?](./cmtimebasegetmastertimebase%28_%29.md)
  Returns the immediate host timebase of a timebase.
- [func CMTimebaseGetMasterClock(CMTimebase) -> CMClock?](./cmtimebasegetmasterclock%28_%29.md)
  Returns the immediate host clock of a timebase.
- [func CMTimebaseGetMaster(CMTimebase) -> CMClockOrTimebase?](./cmtimebasegetmaster%28_%29.md)
  Returns the immediate host (either timebase or clock) of a timebase.
- [func CMTimebaseGetUltimateMasterClock(CMTimebase) -> CMClock?](./cmtimebasegetultimatemasterclock%28_%29.md)
  Returns the host clock that is the host of all of a timebase’s host timebases.
- [func CMTimebaseSetMasterClock(CMTimebase, CMClock) -> OSStatus](./cmtimebasesetmasterclock%28_,_%29.md)
  Sets the time of a timebase at a particular source time.
- [func CMTimebaseSetMasterTimebase(CMTimebase, CMTimebase) -> OSStatus](./cmtimebasesetmastertimebase%28_,_%29.md)
- [func CMTimebaseCopyMaster(CMTimebase) -> CMClockOrTimebase](./cmtimebasecopymaster%28_%29.md)
  Returns the immediate host timebase of a timebase.
- [func CMTimebaseCopyMasterClock(CMTimebase) -> CMClock?](./cmtimebasecopymasterclock%28_%29.md)
  Returns the immediate host clock of a timebase.
- [func CMTimebaseCopyMasterTimebase(CMTimebase) -> CMTimebase?](./cmtimebasecopymastertimebase%28_%29.md)
  Returns the immediate host timebase of a timebase.
- [func CMTimebaseCopyUltimateMasterClock(CMTimebase) -> CMClock](./cmtimebasecopyultimatemasterclock%28_%29.md)
  Returns the host clock that is the host of all of a timebase’s host timebases.
- [func CMTimebaseCreateWithMasterClock(allocator: CFAllocator?, masterClock: CMClock, timebaseOut: UnsafeMutablePointer<CMTimebase?>) -> OSStatus](./cmtimebasecreatewithmasterclock%28allocator,masterclock,timebaseout%29.md)
  Creates a timebase by using a primary clock.
- [func CMTimebaseCreateWithMasterTimebase(allocator: CFAllocator?, masterTimebase: CMTimebase, timebaseOut: UnsafeMutablePointer<CMTimebase?>) -> OSStatus](./cmtimebasecreatewithmastertimebase%28allocator,mastertimebase,timebaseout%29.md)
  Creates a timebase by using a host timebase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasesetanchortime(_:timebasetime:immediatemastertime:))*