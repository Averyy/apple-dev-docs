# rightTeam

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Details for the team that appears on the right side of the display.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var rightTeam: CPNowPlayingSportsTeam { get }
```

```objc
@property (nonatomic, strong, readonly) CPNowPlayingSportsTeam * rightTeam;
```

## Discussion

This property displays information about a team, including its name, logo artwork, and the team’s current points. CarPlay displays this information on the right side of the display, even for right-to-left languages and right-hand-drive vehicles. Typically, the visiting team appears on the left side and the home team appears on the right side of the display.

## See Also

### Getting the event details
- [var leftTeam: CPNowPlayingSportsTeam](./leftteam.md)
  Team-specific details to display on the left side of the Now Playing interface.
- [var eventStatus: CPNowPlayingSportsEventStatus?](./eventstatus.md)
  Match details to display in the center of the Now Playing interface.
- [var backgroundArtwork: UIImage?](./backgroundartwork.md)
  The image to display behind the match information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingmodesports/rightteam)*