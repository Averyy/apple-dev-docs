# playbackProgress

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The current playback progress for a media item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var playbackProgress: CGFloat { get set }
```

```objc
@property (nonatomic, assign) CGFloat playbackProgress;
```

## Discussion

Set the value of this property to a floating-point value between `0.0` and `1.0`, with `0.0` indicating the start of playback and `1.0` indicating the end of playback.

When the [`isPlaying`](./isplaying.md) property is `true`, CarPlay displays a progress bar and configures it with the value in this property. If you change the value of this property while the list item is visible, CarPlay updates the interface to reflect the new value.

## See Also

### Managing playback information
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether the list item displays the Now Playing indicator.
- [var playingIndicatorLocation: CPListItemPlayingIndicatorLocation](./playingindicatorlocation.md)
  The placement of the Now Playing indicator in the list item’s row.
- [enum CPListItemPlayingIndicatorLocation](../cplistitemplayingindicatorlocation.md)
  The locations where a list item can display the Now Playing indicator.
- [var isExplicitContent: Bool](./isexplicitcontent.md)
  A Boolean value that indicates whether the list item displays an explicit content indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/playbackprogress)*