# isPlaying

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the list item displays its Now Playing indicator.

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

#### Discussion

If [`true`](../../Swift/true.md), the list item displays its Now Playing indicator and positions it using the location that the [`playingIndicatorLocation`](./playingindicatorlocation.md) property specifies. The default value is [`false`](../../Swift/false.md).

## See Also

### Managing Playback Information
- [var isExplicitContent: Bool](./isexplicitcontent.md)
  A Boolean value that determines whether the list item displays its explicit content indicator.
- [var playingIndicatorLocation: CPListItemPlayingIndicatorLocation](./playingindicatorlocation.md)
  The location where the list item displays its Now Playing indicator.
- [enum CPListItemPlayingIndicatorLocation](../cplistitemplayingindicatorlocation.md)
  The locations where a list item can display the Now Playing indicator.
- [var playbackProgress: CGFloat](./playbackprogress.md)
  The playback progress status for the content that the list item represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/isplaying)*