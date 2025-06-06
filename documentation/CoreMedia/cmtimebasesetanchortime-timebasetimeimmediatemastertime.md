# CMTimebaseSetAnchorTime(_:timebaseTime:immediateMasterTime:)

**Framework**: Core Media  
**Kind**: func

Sets the time of a timebase at a particular source time.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst ?+
- macOS 10.8+
- tvOS 9.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func CMTimebaseSetAnchorTime(_ timebase: CMTimebase, timebaseTime: CMTime, immediateMasterTime: CMTime)
```

## See Also

- [func CMTimebaseSetRateAndAnchorTime(CMTimebase, rate: Double, anchorTime: CMTime, immediateMasterTime: CMTime)](cmtimebasesetrateandanchortime(_:rate:anchortime:immediatemastertime:).md)
- [func CMTimebaseGetMasterTimebase(CMTimebase) -> CMTimebase?](cmtimebasegetmastertimebase(_:).md)
  Returns the immediate host timebase of a timebase.
- [func CMTimebaseGetMasterClock(CMTimebase) -> CMClock?](cmtimebasegetmasterclock(_:).md)
  Returns the immediate host clock of a timebase.
- [func CMTimebaseGetMaster(CMTimebase) -> CMClockOrTimebase?](cmtimebasegetmaster(_:).md)
  Returns the immediate host (either timebase or clock) of a timebase.
- [func CMTimebaseGetUltimateMasterClock(CMTimebase) -> CMClock?](cmtimebasegetultimatemasterclock(_:).md)
  Returns the host clock that is the host of all of a timebase’s host timebases.
- [func CMTimebaseSetMasterClock(CMTimebase, CMClock) -> OSStatus](cmtimebasesetmasterclock(_:_:).md)
  Sets the time of a timebase at a particular source time.
- [func CMTimebaseSetMasterTimebase(CMTimebase, CMTimebase) -> OSStatus](cmtimebasesetmastertimebase(_:_:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasesetanchortime(_:timebasetime:immediatemastertime:))*