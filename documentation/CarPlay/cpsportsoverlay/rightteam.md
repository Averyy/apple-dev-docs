# rightTeam

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Team-specific details to display in the right-bottom portion of the thumbnail image.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var rightTeam: CPNowPlayingSportsTeam { get }
```

```objc
@property (nonatomic, strong, readonly) CPNowPlayingSportsTeam * rightTeam;
```

## Discussion

This property contains information about the team, including its name, logo artwork, and the number of points the team scored. Typically, the visiting team appears on the left side of the element and the home team appears on the right side.

## See Also

### Getting the overlay information
- [var leftTeam: CPNowPlayingSportsTeam](./leftteam.md)
  Team-specific details to display in the left-bottom portion of the thumbnail image.
- [var eventStatus: CPNowPlayingSportsEventStatus?](./eventstatus.md)
  Match details to display in the bottom center of the thumbnail image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsportsoverlay/rightteam)*