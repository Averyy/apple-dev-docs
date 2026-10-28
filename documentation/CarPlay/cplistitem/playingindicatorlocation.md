# playingIndicatorLocation

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The location where the list item displays its Now Playing indicator.

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

If the list item’s [`isPlaying`](./isplaying.md) property is set to [`true`](../../Swift/true.md), it uses the value of this property to position its Now Playing indicator. The default value is [`CPListItemPlayingIndicatorLocation.leading`](../cplistitemplayingindicatorlocation/leading.md).

## See Also

### Managing Playback Information
- [var isExplicitContent: Bool](./isexplicitcontent.md)
  A Boolean value that determines whether the list item displays its explicit content indicator.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that determines whether the list item displays its Now Playing indicator.
- [enum CPListItemPlayingIndicatorLocation](../cplistitemplayingindicatorlocation.md)
  The locations where a list item can display the Now Playing indicator.
- [var playbackProgress: CGFloat](./playbackprogress.md)
  The playback progress status for the content that the list item represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/playingindicatorlocation)*