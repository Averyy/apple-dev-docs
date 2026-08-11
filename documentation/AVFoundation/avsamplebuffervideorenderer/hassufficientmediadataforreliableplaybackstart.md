# hasSufficientMediaDataForReliablePlaybackStart

**Framework**: AVFoundation  
**Kind**: property

Indicates whether the enqueued media data meets the renderer’s preroll level.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
var hasSufficientMediaDataForReliablePlaybackStart: Bool { get }
```

#### Discussion

Clients should fetch the value of this property to learn if the renderer has had enough media data enqueued to start playback reliably. Starting playback when this property is NO may prevent smooth playback following an immediate start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/hassufficientmediadataforreliableplaybackstart)*