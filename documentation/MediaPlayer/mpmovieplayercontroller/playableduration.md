# playableDuration

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The amount of currently playable content.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var playableDuration: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval playableDuration;
```

#### Discussion

For progressively downloaded network content, this property reflects the amount of content that can be played now.

## See Also

### Accessing the movie duration
- [var duration: TimeInterval](./duration.md)
  The duration of the movie, measured in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/playableduration)*