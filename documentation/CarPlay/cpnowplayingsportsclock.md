# CPNowPlayingSportsClock

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

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

```objc
@interface CPNowPlayingSportsClock : NSObject
```

## Overview

Or, a representation of the amount of time remaining in the event, or a section of the event (period/quarter/etc.) for events where the clock counts DOWN.

## Topics

### Initializers
- [init?(coder: NSCoder)](./cpnowplayingsportsclock/init%28coder%29.md)
- [init(elapsedTime: TimeInterval, paused: Bool)](./cpnowplayingsportsclock/init%28elapsedtime,paused%29.md)
  Represents a duration of time that has elapsed so far in this event, or play period of the event (quarter/inning/period).
- [init(timeRemaining: TimeInterval, paused: Bool)](./cpnowplayingsportsclock/init%28timeremaining,paused%29.md)
  Represents an amount of time remaining in the event, or play period of the event (quarter/inning/period).
### Instance Properties
- [var countsUp: Bool](./cpnowplayingsportsclock/countsup.md)
  If true, the timer is counting UP, so as to indicate an amount of time elapsed so far in this event.
- [var isPaused: Bool](./cpnowplayingsportsclock/ispaused.md)
  Whether the clock should be paused, e.g. due to a stoppage in play.
- [var timeValue: TimeInterval](./cpnowplayingsportsclock/timevalue.md)
  The time value in the clock; either elapsed time or time remaining.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsclock)*