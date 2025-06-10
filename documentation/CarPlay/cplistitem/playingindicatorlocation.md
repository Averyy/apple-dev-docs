# playingIndicatorLocation

**Framework**: CarPlay  
**Kind**: property

The location where the list item displays its Now Playing indicator.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
var playingIndicatorLocation: CPListItemPlayingIndicatorLocation { get set }
```

#### Discussion

If the list item’s [`isPlaying`](cplistitem/isplaying.md) property is set to [`true`](https://developer.apple.com/documentation/swift/true), it uses the value of this property to position its Now Playing indicator. The default value is [`CPListItemPlayingIndicatorLocation.leading`](cplistitemplayingindicatorlocation/leading.md).

## See Also

- [var isExplicitContent: Bool](cplistitem/isexplicitcontent.md)
  A Boolean value that determines whether the list item displays its explicit content indicator.
- [var isPlaying: Bool](cplistitem/isplaying.md)
  A Boolean value that determines whether the list item displays its Now Playing indicator.
- [enum CPListItemPlayingIndicatorLocation](cplistitemplayingindicatorlocation.md)
  The locations where a list item can display the Now Playing indicator.
- [var playbackProgress: CGFloat](cplistitem/playbackprogress.md)
  The playback progress status for the content that the list item represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/playingindicatorlocation)*