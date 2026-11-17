# logo

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The logo information for the team.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@NSCopying
var logo: CPNowPlayingSportsTeamLogo { get }
```

```objc
@property (nonatomic, copy, readonly) CPNowPlayingSportsTeamLogo * logo;
```

## Discussion

Logo information can include either an image with the team’s logo or an abbreviation of the team’s name.

## See Also

### Getting the team information
- [var name: String](./name.md)
  The localized name of the team.
- [var isFavorite: Bool](./isfavorite.md)
  A Boolean value that indicates whether the team is one of the person’s favorites.
- [var teamStandings: String?](./teamstandings.md)
  Team-specific information to display with the team’s name and logo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteam/logo)*