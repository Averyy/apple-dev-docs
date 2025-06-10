# CMTimebase

**Framework**: Core Media  
**Kind**: class

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

## Topics

### Timebases
- [static let farFuture: CFAbsoluteTime](cmtimebase/farfuture.md)
  A time far into the future that represents the year 2257.
- [static let veryLongTimeInterval: CFTimeInterval](cmtimebase/verylongtimeinterval.md)
  A time far into the future that represents 256 years.
### Inspecting Timebases
- [var time: CMTime](cmtimebase/time.md)
  The current time.
- [var rate: Double](cmtimebase/rate.md)
  The current rate relative to its immediate primary clock or timebase.
- [var source: any CMSyncProtocol](cmtimebase/source.md)
  The immediate source that represents the clock or timebase.
- [var sourceClock: CMClock?](cmtimebase/sourceclock.md)
  Returns the immediate source clock, if any.
- [var sourceTimebase: CMTimebase?](cmtimebase/sourcetimebase.md)
  Returns the immediate source timebase, if any.
- [var effectiveRate: Double](cmtimebase/effectiverate.md)
  The effective rate that combines its rate with the rates of all its primary timebases.
- [var timeAndRate: (time: CMTime, rate: Double)](cmtimebase/timeandrate.md)
  Returns the current time and rate.
- [var ultimateSourceClock: CMClock](cmtimebase/ultimatesourceclock.md)
  Returns the source clock that’s the source of all the other source timebases.
### Adding and Removing Timers
- [func addTimer(Timer, on: RunLoop) throws](cmtimebase/addtimer(_:on:).md)
  Adds the timer to the list of timers the timebase manages.
- [func addTimer<T>(T) throws](cmtimebase/addtimer(_:).md)
  Adds the timer dispatch source to the list of timers the timebase manages.
- [func removeTimer(Timer) throws](cmtimebase/removetimer(_:)-4f6re.md)
  Removes the timer from the list of timers the timebase manages.
- [func removeTimer<T>(T) throws](cmtimebase/removetimer(_:)-448o2.md)
  Removes the timer dispatch source from the list of timers the timebase manages.
### Getting and Setting Time
- [func setTime(CMTime) throws](cmtimebase/settime(_:).md)
  Sets the current time.
- [func time(withTimescale: CMTimeScale, rounding: CMTimeRoundingMethod) -> CMTime](cmtimebase/time(withtimescale:rounding:).md)
  Returns the current time in the timescale you request.
### Getting and Setting the Timebase Rate
- [func setRate(Double) throws](cmtimebase/setrate(_:).md)
  Sets the rate.
- [func setRateAndAnchorTime(rate: Double, anchorTime: CMTime, referenceTime: CMTime) throws](cmtimebase/setrateandanchortime(rate:anchortime:referencetime:).md)
  Sets the time at a particular primary time, and changes the rate at exactly that time.
### Setting Timers
- [func setTimerNextFireTime(Timer, fireTime: CMTime) throws](cmtimebase/settimernextfiretime(_:firetime:)-13hjt.md)
  Sets the time on the timebase’s timeline at which the timer should fire next.
- [func setTimerNextFireTime<T>(T, fireTime: CMTime) throws](cmtimebase/settimernextfiretime(_:firetime:)-2yvaa.md)
  Sets the time on the timebase’s timeline at which the timer dispatch source should fire next.
- [func setTimerToFireImmediately(Timer) throws](cmtimebase/settimertofireimmediately(_:)-9t3wi.md)
  Sets the timer to fire immediately once, overriding any previous calls.
- [func setTimerToFireImmediately<T>(T) throws](cmtimebase/settimertofireimmediately(_:)-4903g.md)
  Sets the timer dispatch source to fire immediately once, overriding any previous calls.
### Pausing Time Notifications
- [func notificationBarrier() throws](cmtimebase/notificationbarrier.md)
  Requests that the timebase wait until it isn’t posting notifications.
### Setting the Anchor Time
- [func setAnchorTime(CMTime, referenceTime: CMTime) throws](cmtimebase/setanchortime(_:referencetime:).md)
  Sets the time at a particular source time.
### Notifications
- [static let effectiveRateChanged: NSNotification.Name](cmtimebase/effectiveratechanged.md)
  A notification that posts by a timebase after the effective rate changes.
- [static let timeJumped: NSNotification.Name](cmtimebase/timejumped.md)
  A notification that posts by a timebase after a discontinuous time jump.
### Constants
- [CMTimebase.Error](cmtimebase/error.md)
  Constants that describe timebase errors.
- [CMTimebase.NotificationKey](cmtimebase/notificationkey.md)
  Constants that describe notification keys.
- [static var typeID: CFTypeID](cmtimebase/typeid.md)
  A Core Foundation type identifier that represents a timebase object.
### Deprecations
- [var master: any CMSyncProtocol](cmtimebase/master.md)
- [var masterClock: CMClock?](cmtimebase/masterclock.md)
- [var masterTimebase: CMTimebase?](cmtimebase/mastertimebase.md)
- [var ultimateMasterClock: CMClock](cmtimebase/ultimatemasterclock.md)
### Initializers
- [init(referencing: CMTimebase)](cmtimebase/init(referencing:).md)
### Type Aliases
- [CMTimebase.T](cmtimebase/t.md)
### Default Implementations
- [CMSyncProtocol Implementations](cmtimebase/cmsyncprotocol-implementations.md)

## Relationships

### Conforms To
- [CMSyncProtocol](cmsyncprotocol.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CMSync](cmsync.md)
  A type that represents time syncing.
- [protocol CMSyncProtocol](cmsyncprotocol.md)
  A type that provides behavior for syncing time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebase)*