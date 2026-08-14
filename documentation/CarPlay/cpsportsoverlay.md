# CPSportsOverlay

**Framework**: CarPlay  
**Kind**: class

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

## Topics

### Initializers
- [init?(coder: NSCoder)](cpsportsoverlay/init(coder:).md)
- [init(leftTeam: CPNowPlayingSportsTeam, rightTeam: CPNowPlayingSportsTeam, eventStatus: CPNowPlayingSportsEventStatus?)](cpsportsoverlay/init(leftteam:rightteam:eventstatus:).md)
  Initialize a sports overlay with left and right team objects.
### Instance Properties
- [var eventStatus: CPNowPlayingSportsEventStatus?](cpsportsoverlay/eventstatus.md)
  The event status label.
- [var leftTeam: CPNowPlayingSportsTeam](cpsportsoverlay/leftteam.md)
  The left team information.
- [var rightTeam: CPNowPlayingSportsTeam](cpsportsoverlay/rightteam.md)
  The right team information.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsportsoverlay)*