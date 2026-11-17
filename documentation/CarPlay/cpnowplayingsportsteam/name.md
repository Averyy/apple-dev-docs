# name

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The localized name of the team.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var name: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * name;
```

## Discussion

CarPlay displays this string with the team logo in the Now Playing interface.

## See Also

### Getting the team information
- [var logo: CPNowPlayingSportsTeamLogo](./logo.md)
  The logo information for the team.
- [var isFavorite: Bool](./isfavorite.md)
  A Boolean value that indicates whether the team is one of the person’s favorites.
- [var teamStandings: String?](./teamstandings.md)
  Team-specific information to display with the team’s name and logo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteam/name)*