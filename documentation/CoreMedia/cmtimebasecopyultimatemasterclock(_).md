# CMTimebaseCopyUltimateMasterClock(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the host clock that is the host of all of a timebase’s host timebases.

**Availability**:
- iOS 9.0+ - Deprecated in 9.0 (renamed: CMTimebaseCopyUltimateSourceClock(_:))
- iPadOS 9.0+ - Deprecated in 9.0 (renamed: CMTimebaseCopyUltimateSourceClock(_:))
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: CMTimebaseCopyUltimateSourceClock(_:))
- macOS 10.11+ - Deprecated in 10.11 (renamed: CMTimebaseCopyUltimateSourceClock(_:))
- tvOS 9.0+ - Deprecated in 9.0 (renamed: CMTimebaseCopyUltimateSourceClock(_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: CMTimebaseCopyUltimateSourceClock(_:))
- watchOS 6.0+ - Deprecated in 6.0 (renamed: CMTimebaseCopyUltimateSourceClock(_:))

> **Deprecated**: Use [`CMTimebaseCopyUltimateSourceClock(_:)`](./cmtimebasecopyultimatesourceclock%28_%29.md) instead.

## Declaration

```swift
func CMTimebaseCopyUltimateMasterClock(_ timebase: CMTimebase) -> CMClock
```

```c
static CMClockRefCMTimebaseCopyUltimateMasterClock(CMTimebaseRef timebase);
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
- [func CMTimebaseSetAnchorTime(CMTimebase, timebaseTime: CMTime, immediateMasterTime: CMTime)](./cmtimebasesetanchortime%28_,timebasetime,immediatemastertime%29.md)
  Sets the time of a timebase at a particular source time.
- [func CMTimebaseCopyMaster(CMTimebase) -> CMClockOrTimebase](./cmtimebasecopymaster%28_%29.md)
  Returns the immediate host timebase of a timebase.
- [func CMTimebaseCopyMasterClock(CMTimebase) -> CMClock?](./cmtimebasecopymasterclock%28_%29.md)
  Returns the immediate host clock of a timebase.
- [func CMTimebaseCopyMasterTimebase(CMTimebase) -> CMTimebase?](./cmtimebasecopymastertimebase%28_%29.md)
  Returns the immediate host timebase of a timebase.
- [func CMTimebaseCreateWithMasterClock(allocator: CFAllocator?, masterClock: CMClock, timebaseOut: UnsafeMutablePointer<CMTimebase?>) -> OSStatus](./cmtimebasecreatewithmasterclock%28allocator,masterclock,timebaseout%29.md)
  Creates a timebase by using a primary clock.
- [func CMTimebaseCreateWithMasterTimebase(allocator: CFAllocator?, masterTimebase: CMTimebase, timebaseOut: UnsafeMutablePointer<CMTimebase?>) -> OSStatus](./cmtimebasecreatewithmastertimebase%28allocator,mastertimebase,timebaseout%29.md)
  Creates a timebase by using a host timebase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasecopyultimatemasterclock(_:))*