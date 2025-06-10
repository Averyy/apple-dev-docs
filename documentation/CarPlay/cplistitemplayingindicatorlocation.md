# CPListItemPlayingIndicatorLocation

**Framework**: CarPlay  
**Kind**: enum

The locations where a list item can display the Now Playing indicator.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum CPListItemPlayingIndicatorLocation
```

#### Overview

Use these constants to set the value of a list item’s [`playingIndicatorLocation`](cplistitem/playingindicatorlocation.md) property. When you set a list item’s [`isPlaying`](cplistitem/isplaying.md) property to `true`, it uses the specified location to position the Now Playing indicator.

## Topics

### Now Playing Indicator Locations
- [CPListItemPlayingIndicatorLocation.leading](cplistitemplayingindicatorlocation/leading.md)
  Align the Now Playing indicator with the leading edge of the list item.
- [CPListItemPlayingIndicatorLocation.trailing](cplistitemplayingindicatorlocation/trailing.md)
  Align the Now Playing indicator with the trailing edge of the list item.
### Initializers
- [init?(rawValue: Int)](cplistitemplayingindicatorlocation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isExplicitContent: Bool](cplistitem/isexplicitcontent.md)
  A Boolean value that determines whether the list item displays its explicit content indicator.
- [var isPlaying: Bool](cplistitem/isplaying.md)
  A Boolean value that determines whether the list item displays its Now Playing indicator.
- [var playingIndicatorLocation: CPListItemPlayingIndicatorLocation](cplistitem/playingindicatorlocation.md)
  The location where the list item displays its Now Playing indicator.
- [var playbackProgress: CGFloat](cplistitem/playbackprogress.md)
  The playback progress status for the content that the list item represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitemplayingindicatorlocation)*