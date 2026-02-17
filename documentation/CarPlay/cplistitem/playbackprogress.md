# playbackProgress

**Framework**: CarPlay  
**Kind**: property

The playback progress status for the content that the list item represents.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var playbackProgress: CGFloat { get set }
```

#### Discussion

If the list item represents media content that is playable, set this property’s value to a fractional number between 0 and 1 to indicate its playback progress. The list item displays a progress bar that derives its value from this property.

## See Also

- [var isExplicitContent: Bool](cplistitem/isexplicitcontent.md)
  A Boolean value that determines whether the list item displays its explicit content indicator.
- [var isPlaying: Bool](cplistitem/isplaying.md)
  A Boolean value that determines whether the list item displays its Now Playing indicator.
- [var playingIndicatorLocation: CPListItemPlayingIndicatorLocation](cplistitem/playingindicatorlocation.md)
  The location where the list item displays its Now Playing indicator.
- [enum CPListItemPlayingIndicatorLocation](cplistitemplayingindicatorlocation.md)
  The locations where a list item can display the Now Playing indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/playbackprogress)*