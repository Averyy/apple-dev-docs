# isFavorite

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the team is one of the person’s favorites.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var isFavorite: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isFavorite) BOOL favorite;
```

## Discussion

When the value of this property is `true`, CarPlay displays a star next to the team information.

## See Also

### Getting the team information
- [var name: String](./name.md)
  The localized name of the team.
- [var logo: CPNowPlayingSportsTeamLogo](./logo.md)
  The logo information for the team.
- [var teamStandings: String?](./teamstandings.md)
  Team-specific information to display with the team’s name and logo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteam/isfavorite)*