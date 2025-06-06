# CMTimebaseGetMasterTimebase(_:)

**Framework**: Core Media  
**Kind**: func

Returns the immediate host timebase of a timebase.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CMTimebaseGetMasterTimebase(_ timebase: CMTimebase) -> CMTimebase?
```

#### Discussion

Returns `NULL` if the timebase actually has a host clock instead of a host timebase.

## See Also

- [func CMTimebaseSetRateAndAnchorTime(CMTimebase, rate: Double, anchorTime: CMTime, immediateMasterTime: CMTime)](cmtimebasesetrateandanchortime(_:rate:anchortime:immediatemastertime:).md)
- [func CMTimebaseGetMasterClock(CMTimebase) -> CMClock?](cmtimebasegetmasterclock(_:).md)
  Returns the immediate host clock of a timebase.
- [func CMTimebaseGetMaster(CMTimebase) -> CMClockOrTimebase?](cmtimebasegetmaster(_:).md)
  Returns the immediate host (either timebase or clock) of a timebase.
- [func CMTimebaseGetUltimateMasterClock(CMTimebase) -> CMClock?](cmtimebasegetultimatemasterclock(_:).md)
  Returns the host clock that is the host of all of a timebase’s host timebases.
- [func CMTimebaseSetMasterClock(CMTimebase, CMClock) -> OSStatus](cmtimebasesetmasterclock(_:_:).md)
  Sets the time of a timebase at a particular source time.
- [func CMTimebaseSetMasterTimebase(CMTimebase, CMTimebase) -> OSStatus](cmtimebasesetmastertimebase(_:_:).md)
- [func CMTimebaseSetAnchorTime(CMTimebase, timebaseTime: CMTime, immediateMasterTime: CMTime)](cmtimebasesetanchortime(_:timebasetime:immediatemastertime:).md)
  Sets the time of a timebase at a particular source time.
- [func CMTimebaseCopyMaster(CMTimebase) -> CMClockOrTimebase](cmtimebasecopymaster(_:).md)
  Returns the immediate host timebase of a timebase.
- [func CMTimebaseCopyMasterClock(CMTimebase) -> CMClock?](cmtimebasecopymasterclock(_:).md)
  Returns the immediate host clock of a timebase.
- [func CMTimebaseCopyMasterTimebase(CMTimebase) -> CMTimebase?](cmtimebasecopymastertimebase(_:).md)
  Returns the immediate host timebase of a timebase.
- [func CMTimebaseCopyUltimateMasterClock(CMTimebase) -> CMClock](cmtimebasecopyultimatemasterclock(_:).md)
  Returns the host clock that is the host of all of a timebase’s host timebases.
- [func CMTimebaseCreateWithMasterClock(allocator: CFAllocator?, masterClock: CMClock, timebaseOut: UnsafeMutablePointer<CMTimebase?>) -> OSStatus](cmtimebasecreatewithmasterclock(allocator:masterclock:timebaseout:).md)
  Creates a timebase by using a primary clock.
- [func CMTimebaseCreateWithMasterTimebase(allocator: CFAllocator?, masterTimebase: CMTimebase, timebaseOut: UnsafeMutablePointer<CMTimebase?>) -> OSStatus](cmtimebasecreatewithmastertimebase(allocator:mastertimebase:timebaseout:).md)
  Creates a timebase by using a host timebase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasegetmastertimebase(_:))*