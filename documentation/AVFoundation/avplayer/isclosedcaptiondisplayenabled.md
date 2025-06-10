# isClosedCaptionDisplayEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the player uses closed captioning.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+

## Declaration

```swift
@MainActor
var isClosedCaptionDisplayEnabled: Bool { get set }
```

#### Discussion

The player displays closed captions in the following cases:

- Closed captions are present in the media and the value of `closedCaptionDisplayEnabled` is [`true`](https://developer.apple.com/documentation/swift/true), or
- A media selection option representing a stream of closed captions is selected in the legible media selection group.

> **Note**:  It’s strongly recommended that you don’t rely on this property to control the display of closed captions and instead use the media selection capabilities of [`AVPlayer`](avplayer.md) and [`AVPlayerItem`](avplayeritem.md). The media selection API works equally well for displaying SDH subtitles as well as other kinds of content offering accessibility features. See [`select(_:in:)`](avplayeritem/select(_:in:).md) for more details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/isclosedcaptiondisplayenabled)*