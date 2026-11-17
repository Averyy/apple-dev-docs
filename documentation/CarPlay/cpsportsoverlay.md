# CPSportsOverlay

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A type that displays sporting event details on top of a thumbnail image.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
@MainActor
class CPSportsOverlay
```

```objc
@interface CPSportsOverlay : NSObject
```

## Overview

Use a `CPSportsOverlay` object to place the score and details from a sporting event on top of the main image in a [`CPThumbnailImage`](./cpthumbnailimage.md) object. Sports apps use this overlay to show multiple game scores in the rows of a list interface. For example, the app might display division matches in a row and use row elements to show the current scores of games in that division.

You can add a `CPSportsOverlay` object to a thumbnail image at any time. CarPlay places the overlay content on the bottom half of the thumbnail image. Add a sports overlay to a thumbnail image close to the start of a match. When the match ends, remove the overlay after a reasonable delay to give someone time to see the final score. For example, remove the overlay an hour after the match finishes.

## Topics

### Creating a sports overlay
- [init(leftTeam: CPNowPlayingSportsTeam, rightTeam: CPNowPlayingSportsTeam, eventStatus: CPNowPlayingSportsEventStatus?)](./cpsportsoverlay/init%28leftteam,rightteam,eventstatus%29.md)
  Creates a now playing mode object configured with the specified team and sporting event information.
- [init?(coder: NSCoder)](./cpsportsoverlay/init%28coder%29.md)
### Getting the overlay information
- [var leftTeam: CPNowPlayingSportsTeam](./cpsportsoverlay/leftteam.md)
  Team-specific details to display in the left-bottom portion of the thumbnail image.
- [var rightTeam: CPNowPlayingSportsTeam](./cpsportsoverlay/rightteam.md)
  Team-specific details to display in the right-bottom portion of the thumbnail image.
- [var eventStatus: CPNowPlayingSportsEventStatus?](./cpsportsoverlay/eventstatus.md)
  Match details to display in the bottom center of the thumbnail image.

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

### Element overlays
- [class CPImageOverlay](./cpimageoverlay.md)
  A type that manages content you layer on top of a thumbnail image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsportsoverlay)*