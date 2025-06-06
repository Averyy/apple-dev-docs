# CPNowPlayingSportsTeamLogo

**Framework**: CarPlay  
**Kind**: class

A logo image or, if no image is available, an abbreviation or initialism for this team.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
class CPNowPlayingSportsTeamLogo
```

## Topics

### Initializers
- [init(teamInitials: String)](cpnowplayingsportsteamlogo/init(teaminitials:).md)
  If no team logo image is available, initialize a team logo with an abbreviation or initialism for this team.
- [init(teamLogo: UIImage)](cpnowplayingsportsteamlogo/init(teamlogo:).md)
  Initialize a team logo with an image representation of this team. Provide an image no larger than 350x350; larger images will be resized down.
### Instance Properties
- [var initials: String?](cpnowplayingsportsteamlogo/initials.md)
  An abbreviation or initialism for this team, used only if no logo image is available for this team.
- [var logo: UIImage?](cpnowplayingsportsteamlogo/logo.md)
  A team logo image for this team.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteamlogo)*