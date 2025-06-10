# CPNowPlayingSportsClock

**Framework**: CarPlay  
**Kind**: class

A representation of the amount of time elapsed so far in this event, for events where the clock counts UP.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@MainActor
class CPNowPlayingSportsClock
```

#### Overview

Or, a representation of the amount of time remaining in the event, or a section of the event (period/quarter/etc.) for events where the clock counts DOWN.

## Topics

### Initializers
- [init(elapsedTime: TimeInterval, paused: Bool)](cpnowplayingsportsclock/init(elapsedtime:paused:).md)
  Represents a duration of time that has elapsed so far in this event, or play period of the event (quarter/inning/period).
- [init(timeRemaining: TimeInterval, paused: Bool)](cpnowplayingsportsclock/init(timeremaining:paused:).md)
  Represents an amount of time remaining in the event, or play period of the event (quarter/inning/period).
### Instance Properties
- [var countsUp: Bool](cpnowplayingsportsclock/countsup.md)
  If true, the timer is counting UP, so as to indicate an amount of time elapsed so far in this event.
- [var isPaused: Bool](cpnowplayingsportsclock/ispaused.md)
  Whether the clock should be paused, e.g. due to a stoppage in play.
- [var timeValue: TimeInterval](cpnowplayingsportsclock/timevalue.md)
  The time value in the clock; either elapsed time or time remaining.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsclock)*