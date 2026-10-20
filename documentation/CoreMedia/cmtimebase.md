# CMTimebase

**Framework**: Core Media  
**Kind**: class  
**Role**: Class

A model of a timeline under application control.

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
class CMTimebase
```

```c
typedef struct OpaqueCMTimebase * CMTimebaseRef;
```

## Topics

### Timebases
- [static let farFuture: CFAbsoluteTime](./cmtimebase/farfuture.md)
  A time far into the future that represents the year 2257.
- [static let veryLongTimeInterval: CFTimeInterval](./cmtimebase/verylongtimeinterval.md)
  A time far into the future that represents 256 years.
### Inspecting Timebases
- [var time: CMTime](./cmtimebase/time.md)
  The current time.
- [var rate: Double](./cmtimebase/rate.md)
  The current rate relative to its immediate primary clock or timebase.
- [var source: any CMSyncProtocol](./cmtimebase/source.md)
  The immediate source that represents the clock or timebase.
- [var sourceClock: CMClock?](./cmtimebase/sourceclock.md)
  Returns the immediate source clock, if any.
- [var sourceTimebase: CMTimebase?](./cmtimebase/sourcetimebase.md)
  Returns the immediate source timebase, if any.
- [var effectiveRate: Double](./cmtimebase/effectiverate.md)
  The effective rate that combines its rate with the rates of all its primary timebases.
- [var timeAndRate: (time: CMTime, rate: Double)](./cmtimebase/timeandrate.md)
  Returns the current time and rate.
- [var ultimateSourceClock: CMClock](./cmtimebase/ultimatesourceclock.md)
  Returns the source clock that’s the source of all the other source timebases.
### Adding and Removing Timers
- [func addTimer(Timer, on: RunLoop) throws](./cmtimebase/addtimer%28_,on%29.md)
  Adds the timer to the list of timers the timebase manages.
- [func addTimer<T>(T) throws](./cmtimebase/addtimer%28_%29.md)
  Adds the timer dispatch source to the list of timers the timebase manages.
- [func removeTimer(Timer) throws](./cmtimebase/removetimer%28_%29-4f6re.md)
  Removes the timer from the list of timers the timebase manages.
- [func removeTimer<T>(T) throws](./cmtimebase/removetimer%28_%29-448o2.md)
  Removes the timer dispatch source from the list of timers the timebase manages.
### Getting and Setting Time
- [func setTime(CMTime) throws](./cmtimebase/settime%28_%29.md)
  Sets the current time.
- [func time(withTimescale: CMTimeScale, rounding: CMTimeRoundingMethod) -> CMTime](./cmtimebase/time%28withtimescale,rounding%29.md)
  Returns the current time in the timescale you request.
### Getting and Setting the Timebase Rate
- [func setRate(Double) throws](./cmtimebase/setrate%28_%29.md)
  Sets the rate.
- [func setRateAndAnchorTime(rate: Double, anchorTime: CMTime, referenceTime: CMTime) throws](./cmtimebase/setrateandanchortime%28rate,anchortime,referencetime%29.md)
  Sets the time at a particular primary time, and changes the rate at exactly that time.
### Setting Timers
- [func setTimerNextFireTime(Timer, fireTime: CMTime) throws](./cmtimebase/settimernextfiretime%28_,firetime%29-13hjt.md)
  Sets the time on the timebase’s timeline at which the timer should fire next.
- [func setTimerNextFireTime<T>(T, fireTime: CMTime) throws](./cmtimebase/settimernextfiretime%28_,firetime%29-2yvaa.md)
  Sets the time on the timebase’s timeline at which the timer dispatch source should fire next.
- [func setTimerToFireImmediately(Timer) throws](./cmtimebase/settimertofireimmediately%28_%29-9t3wi.md)
  Sets the timer to fire immediately once, overriding any previous calls.
- [func setTimerToFireImmediately<T>(T) throws](./cmtimebase/settimertofireimmediately%28_%29-4903g.md)
  Sets the timer dispatch source to fire immediately once, overriding any previous calls.
### Pausing Time Notifications
- [func notificationBarrier() throws](./cmtimebase/notificationbarrier%28%29.md)
  Requests that the timebase wait until it isn’t posting notifications.
### Setting the Anchor Time
- [func setAnchorTime(CMTime, referenceTime: CMTime) throws](./cmtimebase/setanchortime%28_,referencetime%29.md)
  Sets the time at a particular source time.
### Notifications
- [static let effectiveRateChanged: NSNotification.Name](./cmtimebase/effectiveratechanged.md)
  A notification that posts by a timebase after the effective rate changes.
- [static let timeJumped: NSNotification.Name](./cmtimebase/timejumped.md)
  A notification that posts by a timebase after a discontinuous time jump.
### Constants
- [CMTimebase.Error](./cmtimebase/error.md)
  Constants that describe timebase errors.
- [CMTimebase.NotificationKey](./cmtimebase/notificationkey.md)
  Constants that describe notification keys.
- [static var typeID: CFTypeID](./cmtimebase/typeid.md)
  A Core Foundation type identifier that represents a timebase object.
### Deprecations
- [var master: any CMSyncProtocol](./cmtimebase/master.md)
- [var masterClock: CMClock?](./cmtimebase/masterclock.md)
- [var masterTimebase: CMTimebase?](./cmtimebase/mastertimebase.md)
- [var ultimateMasterClock: CMClock](./cmtimebase/ultimatemasterclock.md)
### Initializers
- [init(referencing: CMTimebase)](./cmtimebase/init%28referencing%29.md)
### Type Aliases
- [CMTimebase.T](./cmtimebase/t.md)
### Default Implementations
- [CMSyncProtocol Implementations](./cmtimebase/cmsyncprotocol-implementations.md)

## Relationships

### Conforms To
- [CMSyncProtocol](./cmsyncprotocol.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Data Types
- [struct CMSync](./cmsync.md)
  A type that represents time syncing.
- [protocol CMSyncProtocol](./cmsyncprotocol.md)
  A type that provides behavior for syncing time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebase)*