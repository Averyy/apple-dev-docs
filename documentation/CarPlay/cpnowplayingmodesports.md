# CPNowPlayingModeSports

**Framework**: CarPlay  
**Kind**: class

The sports mode represents a layout for now playing suited to live-streaming or recorded playback of a sporting event that features exactly two teams.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@MainActor
class CPNowPlayingModeSports
```

## Topics

### Initializers
- [init(leftTeam: CPNowPlayingSportsTeam, rightTeam: CPNowPlayingSportsTeam, eventStatus: CPNowPlayingSportsEventStatus?, backgroundArtwork: UIImage?)](cpnowplayingmodesports/init(leftteam:rightteam:eventstatus:backgroundartwork:).md)
  Initialize a sports mode for display on the CarPlay now playing screen.
### Instance Properties
- [var backgroundArtwork: UIImage?](cpnowplayingmodesports/backgroundartwork.md)
  A large colorful image for the background of the now playing screen. A gradient or crossfade image works best, especially when it includes the primary colors of each team. Provide an image no larger than 500x500.
- [var eventStatus: CPNowPlayingSportsEventStatus?](cpnowplayingmodesports/eventstatus.md)
  A representation of the current event status. See
- [var leftTeam: CPNowPlayingSportsTeam](cpnowplayingmodesports/leftteam.md)
  The sports team that should appear on the left side of the now playing screen. This is commonly (but not always) the AWAY or VISITING team. This team will be on the left in all layouts; it does not flip to the right side when in a right-to-left language or a right-hand-drive vehicle.
- [var rightTeam: CPNowPlayingSportsTeam](cpnowplayingmodesports/rightteam.md)
  The sports team that should appear on the right side of the now playing screen. This is commonly (but not always) the HOME team. This team will be on the right in all layouts; it does not flip to the left side when in a right-to-left language or a right-hand-drive vehicle.

## Relationships

### Inherits From
- [CPNowPlayingMode](cpnowplayingmode.md)
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
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingmodesports)*