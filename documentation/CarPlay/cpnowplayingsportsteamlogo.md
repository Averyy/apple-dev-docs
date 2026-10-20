# CPNowPlayingSportsTeamLogo

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A logo image or, if no image is available, an abbreviation or initialism for this team.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@MainActor
class CPNowPlayingSportsTeamLogo
```

```objc
@interface CPNowPlayingSportsTeamLogo : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./cpnowplayingsportsteamlogo/init%28coder%29.md)
- [init(teamInitials: String)](./cpnowplayingsportsteamlogo/init%28teaminitials%29.md)
  If no team logo image is available, initialize a team logo with an abbreviation or initialism for this team.
- [init(teamLogo: UIImage)](./cpnowplayingsportsteamlogo/init%28teamlogo%29.md)
  Initialize a team logo with an image representation of this team. Provide an image no larger than 350x350; larger images will be resized down.
### Instance Properties
- [var initials: String?](./cpnowplayingsportsteamlogo/initials.md)
  An abbreviation or initialism for this team, used only if no logo image is available for this team.
- [var logo: UIImage?](./cpnowplayingsportsteamlogo/logo.md)
  A team logo image for this team.

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

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteamlogo)*