# playingIndicatorLocation

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The placement of the Now Playing indicator in the list item’s row.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var playingIndicatorLocation: CPListItemPlayingIndicatorLocation { get set }
```

```objc
@property (nonatomic, assign) CPListItemPlayingIndicatorLocation playingIndicatorLocation;
```

## Discussion

When the [`isPlaying`](./isplaying.md) property is `true`, CarPlay displays the Now Playing indicator for the list item and places it according to the value in this property. The default value of this property is [`CPListItemPlayingIndicatorLocation.leading`](../cplistitemplayingindicatorlocation/leading.md).

## See Also

### Managing playback information
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether the list item displays the Now Playing indicator.
- [var playbackProgress: CGFloat](./playbackprogress.md)
  The current playback progress for a media item.
- [enum CPListItemPlayingIndicatorLocation](../cplistitemplayingindicatorlocation.md)
  The locations where a list item can display the Now Playing indicator.
- [var isExplicitContent: Bool](./isexplicitcontent.md)
  A Boolean value that indicates whether the list item displays an explicit content indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/playingindicatorlocation)*