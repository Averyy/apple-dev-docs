# CPNowPlayingSportsClock

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A type that specifies the elapsed or remaining time in a match and the state of the clock.

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

Use a `CPNowPlayingSportsClock` object to specify clock-related information for the current section of a sporting event. Clocks in sporting events either count up to reflect the elapsed time of the match or count down to indicate the amount of time remaining. For example, the clock in a hockey game counts down from an initial value of 20 minutes.

Create a `CPNowPlayingSportsClock` object with the initial time information when configuring the Now Playing interface. Create additional instances throughout the match when gameplay pauses or resumes, or when you need to adjust the time on the clock. Assign your clock objects to the [`CPNowPlayingSportsEventStatus`](./cpnowplayingsportseventstatus.md) object you use to report the state of the match to the Now Playing interface.

Keep the clock in the Now Playing interface synchronized with the rest of your content. When the [`isPaused`](./cpnowplayingsportsclock/ispaused.md) property is `false`, CarPlay increments and decrements the clock value once a second as a convenience so you don’t have to update the clock information yourself. However, CarPlay doesn’t make the updated clock value available to your app. When you need to create new [`CPNowPlayingSportsClock`](./cpnowplayingsportsclock.md) objects, initialize them with actual game data to ensure the displayed clock remains synchronized with the rest of your content.

## Topics

### Creating a sports mode type
- [init(elapsedTime: TimeInterval, paused: Bool)](./cpnowplayingsportsclock/init%28elapsedtime,paused%29.md)
  Creates a clock that counts up to measure the elapsed time from the specified value.
- [init(timeRemaining: TimeInterval, paused: Bool)](./cpnowplayingsportsclock/init%28timeremaining,paused%29.md)
  Creates a clock that counts down from the specified value.
- [init?(coder: NSCoder)](./cpnowplayingsportsclock/init%28coder%29.md)
### Getting the clock attributes
- [var timeValue: TimeInterval](./cpnowplayingsportsclock/timevalue.md)
  The time value you specify at initialization.
- [var countsUp: Bool](./cpnowplayingsportsclock/countsup.md)
  A Boolean value that indicates whether the event clock counts up.
- [var isPaused: Bool](./cpnowplayingsportsclock/ispaused.md)
  A Boolean value that indicates whether the clock is paused.

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

## See Also

### Sports mode content
- [class CPNowPlayingSportsTeam](./cpnowplayingsportsteam.md)
  A type that specifies team-specific details, including the name, standings, and current score in the match.
- [class CPNowPlayingSportsTeamLogo](./cpnowplayingsportsteamlogo.md)
  A type that manages logo information for a sports team.
- [class CPNowPlayingSportsEventStatus](./cpnowplayingsportseventstatus.md)
  A type that manages match-focused information, including the event clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsclock)*