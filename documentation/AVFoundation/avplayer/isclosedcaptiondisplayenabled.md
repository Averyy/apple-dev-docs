# isClosedCaptionDisplayEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player uses closed captioning.

**Availability**:
- iOS 4.0+ - Deprecated in 11.0
- iPadOS 4.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Let a player enable closed captions automatically according to user preferences by setting the value of the [`appliesMediaSelectionCriteriaAutomatically`](./appliesmediaselectioncriteriaautomatically.md) property to [`true`](../../Swift/true.md).

## Declaration

```swift
var isClosedCaptionDisplayEnabled: Bool { get set }
```

```objc
@property (getter=isClosedCaptionDisplayEnabled) BOOL closedCaptionDisplayEnabled;
```

## Discussion

The player displays closed captions in the following cases:

- Closed captions are present in the media and the value of `closedCaptionDisplayEnabled` is [`true`](../../Swift/true.md), or
- A media selection option representing a stream of closed captions is selected in the legible media selection group.

> **Note**:  It’s strongly recommended that you don’t rely on this property to control the display of closed captions and instead use the media selection capabilities of [`AVPlayer`](../avplayer.md) and [`AVPlayerItem`](../avplayeritem.md). The media selection API works equally well for displaying SDH subtitles as well as other kinds of content offering accessibility features. See [`select(_:in:)`](../avplayeritem/select%28_,in%29.md) for more details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/isclosedcaptiondisplayenabled)*