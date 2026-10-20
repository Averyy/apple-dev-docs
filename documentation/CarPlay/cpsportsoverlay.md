# CPSportsOverlay

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A sports overlay that displays left and right team information.

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

## Topics

### Initializers
- [init?(coder: NSCoder)](./cpsportsoverlay/init%28coder%29.md)
- [init(leftTeam: CPNowPlayingSportsTeam, rightTeam: CPNowPlayingSportsTeam, eventStatus: CPNowPlayingSportsEventStatus?)](./cpsportsoverlay/init%28leftteam,rightteam,eventstatus%29.md)
  Initialize a sports overlay with left and right team objects.
### Instance Properties
- [var eventStatus: CPNowPlayingSportsEventStatus?](./cpsportsoverlay/eventstatus.md)
  The event status label.
- [var leftTeam: CPNowPlayingSportsTeam](./cpsportsoverlay/leftteam.md)
  The left team information.
- [var rightTeam: CPNowPlayingSportsTeam](./cpsportsoverlay/rightteam.md)
  The right team information.

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

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsportsoverlay)*