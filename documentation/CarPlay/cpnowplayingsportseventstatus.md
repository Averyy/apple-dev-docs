# CPNowPlayingSportsEventStatus

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A type that manages match-focused information, including the event clock.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@MainActor
class CPNowPlayingSportsEventStatus
```

```objc
@interface CPNowPlayingSportsEventStatus : NSObject
```

## Overview

A `CPNowPlayingSportsEventStatus` object contains information that isn’t tied to a particular team. You specify this content using a combination of text and images, so it can be anything that’s relevant for the sport. For example, a baseball game might display the inning information, the bases that have runners, the number of outs, and the number of balls and strikes for the current batter. CarPlay displays this information in the center area of the Now Playing interface between the team details.

Create a `CPNowPlayingSportsEventStatus` object during the creation of match-related content for the Now Playing interface. Use the object you create to initialize the [`CPNowPlayingModeSports`](./cpnowplayingmodesports.md) objects you assign to the [`nowPlayingMode`](./cpnowplayingtemplate/nowplayingmode.md) property of the shared [`CPNowPlayingTemplate`](./cpnowplayingtemplate.md) object. During the course of the event, update the information in this object as needed to reflect changes. For example, update the inning information in a baseball match, or update the clock information when the play clock pauses and resumes.

## Topics

### Creating a sports mode type
- [init(eventStatusText: [String]?, eventStatusImage: UIImage?, eventClock: CPNowPlayingSportsClock?)](./cpnowplayingsportseventstatus/init%28eventstatustext,eventstatusimage,eventclock%29.md)
  Creates an event status object from information you provide.
- [init?(coder: NSCoder)](./cpnowplayingsportseventstatus/init%28coder%29.md)
### Getting the event status
- [var eventStatusText: [String]?](./cpnowplayingsportseventstatus/eventstatustext.md)
  One to three strings you use to convey event-related details in the Now Playing interface.
- [var eventStatusImage: UIImage?](./cpnowplayingsportseventstatus/eventstatusimage.md)
  An image you use to convey event-related details in the Now Playing interface.
- [var eventClock: CPNowPlayingSportsClock?](./cpnowplayingsportseventstatus/eventclock.md)
  The clock information you provided for the event.

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
- [class CPNowPlayingSportsClock](./cpnowplayingsportsclock.md)
  A type that specifies the elapsed or remaining time in a match and the state of the clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportseventstatus)*