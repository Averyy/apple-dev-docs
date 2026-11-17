# isPlaying

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the list item displays the Now Playing indicator.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var isPlaying: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isPlaying) BOOL playing;
```

## Discussion

Set this property to `true` to display the Now Playing indicator for the item. CarPlay places this indicator using the information in the [`playingIndicatorLocation`](./playingindicatorlocation.md) property of the item. The default value of this property is `false`.

## See Also

### Managing playback information
- [var playbackProgress: CGFloat](./playbackprogress.md)
  The current playback progress for a media item.
- [var playingIndicatorLocation: CPListItemPlayingIndicatorLocation](./playingindicatorlocation.md)
  The placement of the Now Playing indicator in the list item’s row.
- [enum CPListItemPlayingIndicatorLocation](../cplistitemplayingindicatorlocation.md)
  The locations where a list item can display the Now Playing indicator.
- [var isExplicitContent: Bool](./isexplicitcontent.md)
  A Boolean value that indicates whether the list item displays an explicit content indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/isplaying)*