# CPListItemPlayingIndicatorLocation

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

The locations where a list item can display the Now Playing indicator.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum CPListItemPlayingIndicatorLocation
```

```c
enum CPListItemPlayingIndicatorLocation : NSInteger;
```

## Overview

Use these constants to configure the [`playingIndicatorLocation`](./cplistitem/playingindicatorlocation.md) property of the list item. When you set a list item’s [`isPlaying`](./cplistitem/isplaying.md) property to `true`, CarPlay displays Now Playing information the item’s row and positions it according to the constant you specified.

## Topics

### Now Playing indicator locations
- [CPListItemPlayingIndicatorLocation.leading](./cplistitemplayingindicatorlocation/leading.md)
  An option to display the Now Playing indicator on the leading edge of the list item’s row.
- [CPListItemPlayingIndicatorLocation.trailing](./cplistitemplayingindicatorlocation/trailing.md)
  An option to display the Now Playing indicator on the trailing edge of the list item’s row.
### Initializers
- [init?(rawValue: Int)](./cplistitemplayingindicatorlocation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing playback information
- [var isPlaying: Bool](./cplistitem/isplaying.md)
  A Boolean value that indicates whether the list item displays the Now Playing indicator.
- [var playbackProgress: CGFloat](./cplistitem/playbackprogress.md)
  The current playback progress for a media item.
- [var playingIndicatorLocation: CPListItemPlayingIndicatorLocation](./cplistitem/playingindicatorlocation.md)
  The placement of the Now Playing indicator in the list item’s row.
- [var isExplicitContent: Bool](./cplistitem/isexplicitcontent.md)
  A Boolean value that indicates whether the list item displays an explicit content indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitemplayingindicatorlocation)*