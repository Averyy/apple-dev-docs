# CMTimebase

**Framework**: Core Media  
**Role**: API Collection

A model of a timeline under application control.

#### Overview

A timebase represents a timeline that clients can control by setting the rate and time. Each timebase has either a host clock or a host timebase, and its rate is expressed relative to its host:

- When a timebase has rate 0.0, its time is fixed and doesn’t change as its host’s time changes.
- When a timebase has rate 1.0, its time increases one second as its host’s time increases by one second.
- When a timebase has rate 2.0, its time increases two seconds as its host’s time increases by one second.
- When a timebase has rate -1.0, its time decreases one second as its host’s time increases by one second.

If a timebase has a host timebase, the host timebase’s rate is a factor in determining the timebase’s effective rate. In fact, a timebase’s effective rate is defined as the product of its rate, its host timebase’s rate, its host timebase’s host timebase’s rate, and so on up to the ultimate host clock. This is the rate at which the timebase’s time changes relative to the ultimate host clock.

## Topics

### Creating Timebases
- [func CMTimebaseCreateWithSourceClock(allocator: CFAllocator?, sourceClock: CMClock, timebaseOut: UnsafeMutablePointer<CMTimebase?>) -> OSStatus](./cmtimebasecreatewithsourceclock%28allocator,sourceclock,timebaseout%29.md)
  Creates a timebase by using a source clock.
- [func CMTimebaseCreateWithSourceTimebase(allocator: CFAllocator?, sourceTimebase: CMTimebase, timebaseOut: UnsafeMutablePointer<CMTimebase?>) -> OSStatus](./cmtimebasecreatewithsourcetimebase%28allocator,sourcetimebase,timebaseout%29.md)
  Creates a timebase by using a source timebase.
### Copying Timebases
- [func CMTimebaseCopySource(CMTimebase) -> CMClockOrTimebase](./cmtimebasecopysource%28_%29.md)
  Returns the immediate source — either a clock or timebase — of a timebase.
- [func CMTimebaseCopySourceClock(CMTimebase) -> CMClock?](./cmtimebasecopysourceclock%28_%29.md)
  Returns the immediate source clock of a timebase.
- [func CMTimebaseCopySourceTimebase(CMTimebase) -> CMTimebase?](./cmtimebasecopysourcetimebase%28_%29.md)
  Returns the immediate source timebase of a timebase.
- [func CMTimebaseCopyUltimateSourceClock(CMTimebase) -> CMClock](./cmtimebasecopyultimatesourceclock%28_%29.md)
  Returns the source clock that’s the source of all of a timebase’s source timebases.
### Getting and Setting Time
- [func CMTimebaseGetTime(CMTimebase) -> CMTime](./cmtimebasegettime%28_%29.md)
  Returns the current time from a timebase.
- [func CMTimebaseGetTimeWithTimeScale(CMTimebase, timescale: CMTimeScale, method: CMTimeRoundingMethod) -> CMTime](./cmtimebasegettimewithtimescale%28_,timescale,method%29.md)
  Returns the current time from a timebase in the specified timescale.
- [func CMTimebaseGetTimeAndRate(CMTimebase, timeOut: UnsafeMutablePointer<CMTime>?, rateOut: UnsafeMutablePointer<Float64>?) -> OSStatus](./cmtimebasegettimeandrate%28_,timeout,rateout%29.md)
  Returns the current time and rate of a timebase.
- [func CMTimebaseSetTime(CMTimebase, time: CMTime) -> OSStatus](./cmtimebasesettime%28_,time%29.md)
  Sets the current time of a timebase.
- [func CMTimebaseSetSourceClock(CMTimebase, CMClock) -> OSStatus](./cmtimebasesetsourceclock%28_,_%29.md)
  Sets the source clock of a timebase.
- [func CMTimebaseSetSourceTimebase(CMTimebase, CMTimebase) -> OSStatus](./cmtimebasesetsourcetimebase%28_,_%29.md)
  Sets the source timebase of a timebase.
- [func CMTimebaseSetAnchorTime(CMTimebase, timebaseTime: CMTime, immediateSourceTime: CMTime) -> OSStatus](./cmtimebasesetanchortime%28_,timebasetime,immediatesourcetime%29.md)
  Sets the time of a timebase at a particular host time.
### Getting and Setting the Time Rate
- [func CMTimebaseGetRate(CMTimebase) -> Float64](./cmtimebasegetrate%28_%29.md)
  Returns the current rate of a timebase.
- [func CMTimebaseGetEffectiveRate(CMTimebase) -> Float64](./cmtimebasegeteffectiverate%28_%29.md)
  Returns the effective rate of a timebase, which combines its rate with the rates of all its host timebases.
- [func CMTimebaseSetRate(CMTimebase, rate: Float64) -> OSStatus](./cmtimebasesetrate%28_,rate%29.md)
  Sets the rate of a timebase.
- [func CMTimebaseSetRateAndAnchorTime(CMTimebase, rate: Float64, anchorTime: CMTime, immediateSourceTime: CMTime) -> OSStatus](./cmtimebasesetrateandanchortime%28_,rate,anchortime,immediatesourcetime%29.md)
  Sets the time of a timebase at a particular host time, and changes the rate at exactly that time.
### Interacting with Timers
- [func CMTimebaseAddTimer(CMTimebase, timer: CFRunLoopTimer, runloop: CFRunLoop) -> OSStatus](./cmtimebaseaddtimer%28_,timer,runloop%29.md)
  Adds the timer to the list of timers the timebase manages.
- [func CMTimebaseAddTimerDispatchSource(CMTimebase, timerSource: dispatch_source_t) -> OSStatus](./cmtimebaseaddtimerdispatchsource%28_,timersource%29.md)
  Adds the timer dispatch source to the list of timers the timebase manages.
- [func CMTimebaseRemoveTimer(CMTimebase, timer: CFRunLoopTimer) -> OSStatus](./cmtimebaseremovetimer%28_,timer%29.md)
  Removes the timer from the list of timers the timebase manages.
- [func CMTimebaseRemoveTimerDispatchSource(CMTimebase, timerSource: dispatch_source_t) -> OSStatus](./cmtimebaseremovetimerdispatchsource%28_,timersource%29.md)
  Removes the timer dispatch source from the list of timers the timebase manages.
- [func CMTimebaseSetTimerNextFireTime(CMTimebase, timer: CFRunLoopTimer, fireTime: CMTime, flags: UInt32) -> OSStatus](./cmtimebasesettimernextfiretime%28_,timer,firetime,flags%29.md)
  Sets the time on the timebase’s timeline at which the timer should fire next.
- [func CMTimebaseSetTimerToFireImmediately(CMTimebase, timer: CFRunLoopTimer) -> OSStatus](./cmtimebasesettimertofireimmediately%28_,timer%29.md)
  Sets the timer to fire immediately once, overriding any previous timer calls.
- [func CMTimebaseSetTimerDispatchSourceNextFireTime(CMTimebase, timerSource: dispatch_source_t, fireTime: CMTime, flags: UInt32) -> OSStatus](./cmtimebasesettimerdispatchsourcenextfiretime%28_,timersource,firetime,flags%29.md)
  Sets the time on the timebase’s timeline at which the timer dispatch source should fire next.
- [func CMTimebaseSetTimerDispatchSourceToFireImmediately(CMTimebase, timerSource: dispatch_source_t) -> OSStatus](./cmtimebasesettimerdispatchsourcetofireimmediately%28_,timersource%29.md)
  Sets the timer dispatch source to fire immediately once, overriding any previous timer call.
### Pausing Time Notifications
- [func CMTimebaseNotificationBarrier(CMTimebase) -> OSStatus](./cmtimebasenotificationbarrier%28_%29.md)
  Requests that the timebase wait until it isn’t posting notifications.
### Data Types
- [class CMTimebase](./cmtimebase.md)
  A model of a timeline under application control.
- [struct CMSync](./cmsync.md)
  A type that represents time syncing.
- [protocol CMSyncProtocol](./cmsyncprotocol.md)
  A type that provides behavior for syncing time.
### Timebase Errors
- [var kCMTimebaseError_MissingRequiredParameter: OSStatus](./kcmtimebaseerror_missingrequiredparameter.md)
  A timebase error that indicates a parameter is missing.
- [var kCMTimebaseError_InvalidParameter: OSStatus](./kcmtimebaseerror_invalidparameter.md)
  A timebase error that indicates a parameter isn’t valid.
- [var kCMTimebaseError_AllocationFailed: OSStatus](./kcmtimebaseerror_allocationfailed.md)
  A timebase error that indicates the memory allocation fails.
- [var kCMTimebaseError_TimerIntervalTooShort: OSStatus](./kcmtimebaseerror_timerintervaltooshort.md)
  A timebase error that indicates the time interval is too short.
- [var kCMTimebaseError_ReadOnly: OSStatus](./kcmtimebaseerror_readonly.md)
  A timebase error that indicates the system attempts to modify a read-only timebase.
### Constants
- [func CMTimebaseGetTypeID() -> CFTypeID](./cmtimebasegettypeid%28%29.md)
  Returns the Core Foundation type identifier that identifies a timebase object.
- [kCMTimebaseVeryLongCFTimeInterval](./kcmtimebaseverylongcftimeinterval.md)
  A constant that defines a very long elapsed time in seconds.
- [kCMTimebaseFarFutureCFAbsoluteTime](./kcmtimebasefarfuturecfabsolutetime.md)
  A constant that defines a point of time in the far, far future.
### Notifications
- [let kCMTimebaseNotificationKey_EventTime: CFString](./kcmtimebasenotificationkey_eventtime.md)
  A notification that a timebase posts after a discontinuous time jump.
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
- [func CMTimebaseCopyUltimateMasterClock(CMTimebase) -> CMClock](./cmtimebasecopyultimatemasterclock%28_%29.md)
  Returns the host clock that is the host of all of a timebase’s host timebases.
- [func CMTimebaseCreateWithMasterClock(allocator: CFAllocator?, masterClock: CMClock, timebaseOut: UnsafeMutablePointer<CMTimebase?>) -> OSStatus](./cmtimebasecreatewithmasterclock%28allocator,masterclock,timebaseout%29.md)
  Creates a timebase by using a primary clock.
- [func CMTimebaseCreateWithMasterTimebase(allocator: CFAllocator?, masterTimebase: CMTimebase, timebaseOut: UnsafeMutablePointer<CMTimebase?>) -> OSStatus](./cmtimebasecreatewithmastertimebase%28allocator,mastertimebase,timebaseout%29.md)
  Creates a timebase by using a host timebase.

## See Also

### Media Synchronization
- [CMClock](./cmclock-api.md)
  A reference clock you use to synchronize applications and devices.
- [CMAudioClock](./cmaudioclock-api.md)
  A specialized reference clock that synchronizes with audio sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebase-api)*