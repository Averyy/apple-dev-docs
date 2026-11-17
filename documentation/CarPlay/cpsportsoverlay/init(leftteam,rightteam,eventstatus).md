# init(leftTeam:rightTeam:eventStatus:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a now playing mode object configured with the specified team and sporting event information.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
init(leftTeam: CPNowPlayingSportsTeam, rightTeam: CPNowPlayingSportsTeam, eventStatus: CPNowPlayingSportsEventStatus?)
```

```objc
- (instancetype) initWithLeftTeam:(CPNowPlayingSportsTeam *) leftTeam rightTeam:(CPNowPlayingSportsTeam *) rightTeam eventStatus:(CPNowPlayingSportsEventStatus *) eventStatus;
```

## Return Value

An initialized sports overlay object.

## Discussion

After creating the overlay object, initialize a [`CPThumbnailImage`](../cpthumbnailimage.md) object with it or assign it to the thumbnail image’s [`sportsOverlay`](../cpthumbnailimage/sportsoverlay.md) property.

## Parameters

- `leftTeam`: The visiting team information. CarPlay displays this information on the left side of the thumbnail image.
- `rightTeam`: The home team information. CarPlay displays this information on the right side of the thumbnail image.
- `eventStatus`: The current state of the sports event. Specify the event clock information and event-specific details.

## See Also

### Creating a sports overlay
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsportsoverlay/init(leftteam:rightteam:eventstatus:))*