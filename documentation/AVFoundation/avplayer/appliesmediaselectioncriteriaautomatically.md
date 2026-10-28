# appliesMediaSelectionCriteriaAutomatically

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver should apply the current selection criteria automatically to player items.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
var appliesMediaSelectionCriteriaAutomatically: Bool { get set }
```

```objc
@property BOOL appliesMediaSelectionCriteriaAutomatically;
```

## Mentions

- [Selecting subtitles and alternative audio tracks](../selecting-subtitles-and-alternative-audio-tracks.md)

## Discussion

By default, the `AVPlayer` instance applies selection criteria based on system accessibility preferences. To override the default criteria for any media selection group, use [`setMediaSelectionCriteria(_:forMediaCharacteristic:)`](./setmediaselectioncriteria%28_,formediacharacteristic%29.md).

> **Note**:  For clients linked against the iOS 7.0 and later or against the macOS 10.9 and later, the default is [`true`](../../Swift/true.md). For all others, the default is [`false`](../../Swift/false.md).

## See Also

### Configuring media selection criteria
- [func mediaSelectionCriteria(forMediaCharacteristic: AVMediaCharacteristic) -> AVPlayerMediaSelectionCriteria?](./mediaselectioncriteria%28formediacharacteristic%29.md)
  Returns the automatic selection criteria for media items with the specified media characteristic.
- [func setMediaSelectionCriteria(AVPlayerMediaSelectionCriteria?, forMediaCharacteristic: AVMediaCharacteristic)](./setmediaselectioncriteria%28_,formediacharacteristic%29.md)
  Applies automatic selection criteria for media that has the specified media characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/appliesmediaselectioncriteriaautomatically)*