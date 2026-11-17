# eventStatus

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Match details to display in the bottom center of the thumbnail image.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var eventStatus: CPNowPlayingSportsEventStatus? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) CPNowPlayingSportsEventStatus * eventStatus;
```

## Discussion

Use this property to get details about the playing of the sports event. For example, a baseball game might display the inning number, the current runner positions, the number of outs, and the number of balls and strikes for the current batter.

## See Also

### Getting the overlay information
- [var leftTeam: CPNowPlayingSportsTeam](./leftteam.md)
  Team-specific details to display in the left-bottom portion of the thumbnail image.
- [var rightTeam: CPNowPlayingSportsTeam](./rightteam.md)
  Team-specific details to display in the right-bottom portion of the thumbnail image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsportsoverlay/eventstatus)*