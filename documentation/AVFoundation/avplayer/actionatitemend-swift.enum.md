# AVPlayer.ActionAtItemEnd

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

The actions a player can take when it finishes playing.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum ActionAtItemEnd
```

```c
enum AVPlayerActionAtItemEnd : NSInteger;
```

## Topics

### Actions
- [AVPlayer.ActionAtItemEnd.advance](./actionatitemend-swift.enum/advance.md)
  The player should advance to the next item, if there is one.
- [AVPlayer.ActionAtItemEnd.pause](./actionatitemend-swift.enum/pause.md)
  The player should pause playing.
- [AVPlayer.ActionAtItemEnd.none](./actionatitemend-swift.enum/none.md)
  The player should do nothing.
### Initializers
- [init?(rawValue: Int)](./actionatitemend-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Responding when playback ends
- [var actionAtItemEnd: AVPlayer.ActionAtItemEnd](./actionatitemend-swift.property.md)
  The action to perform when the current player item has finished playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/actionatitemend-swift.enum)*