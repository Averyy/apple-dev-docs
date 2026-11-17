# backgroundArtwork

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The image to display behind the match information.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@NSCopying
var backgroundArtwork: UIImage? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) UIImage * backgroundArtwork;
```

## Discussion

This property stores the image at the expected size, which is 500 by 500 points. A gradient or crossfade image works best for backgrounds, especially when it includes the primary colors of the competing teams.

## See Also

### Getting the event details
- [var leftTeam: CPNowPlayingSportsTeam](./leftteam.md)
  Team-specific details to display on the left side of the Now Playing interface.
- [var rightTeam: CPNowPlayingSportsTeam](./rightteam.md)
  Details for the team that appears on the right side of the display.
- [var eventStatus: CPNowPlayingSportsEventStatus?](./eventstatus.md)
  Match details to display in the center of the Now Playing interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingmodesports/backgroundartwork)*