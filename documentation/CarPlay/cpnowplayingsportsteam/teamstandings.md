# teamStandings

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Team-specific information to display with the team’s name and logo.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var teamStandings: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * teamStandings;
```

## Discussion

This property stores additional team-specific information that people might find interesting. For example, it can display the team’s win-loss record, their standings in the league, or other relevant statistics. The amount of text CarPlay can show depends on the display, but is typically no more than 15 to 20 characters.

## See Also

### Getting the team information
- [var name: String](./name.md)
  The localized name of the team.
- [var logo: CPNowPlayingSportsTeamLogo](./logo.md)
  The logo information for the team.
- [var isFavorite: Bool](./isfavorite.md)
  A Boolean value that indicates whether the team is one of the person’s favorites.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteam/teamstandings)*