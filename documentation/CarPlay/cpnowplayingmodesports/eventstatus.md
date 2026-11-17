# eventStatus

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Match details to display in the center of the Now Playing interface.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var eventStatus: CPNowPlayingSportsEventStatus? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) CPNowPlayingSportsEventStatus * eventStatus;
```

## Discussion

Use this property to get details about the playing of the match. For example, a baseball game might display the inning number, the current runner positions, the number of outs, and the number of balls and strikes for the current batter.

## See Also

### Getting the event details
- [var leftTeam: CPNowPlayingSportsTeam](./leftteam.md)
  Team-specific details to display on the left side of the Now Playing interface.
- [var rightTeam: CPNowPlayingSportsTeam](./rightteam.md)
  Details for the team that appears on the right side of the display.
- [var backgroundArtwork: UIImage?](./backgroundartwork.md)
  The image to display behind the match information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingmodesports/eventstatus)*