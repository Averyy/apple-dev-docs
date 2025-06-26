# configuredTimeOffsetFromLive

**Framework**: AVFoundation  
**Kind**: property

A time value that indicates the offset from the live time to start playback, or resume playback after a seek to positive infinity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
var configuredTimeOffsetFromLive: CMTime { get set }
```

#### Discussion

For nonlive stream content, the value is [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid).

## See Also

- [var automaticallyPreservesTimeOffsetFromLive: Bool](avplayeritem/automaticallypreservestimeoffsetfromlive.md)
  A Boolean value that indicates whether the player preserves its time offset from the live time after a buffering operation.
- [var recommendedTimeOffsetFromLive: CMTime](avplayeritem/recommendedtimeoffsetfromlive.md)
  A recommended time offset from the live time based on observed network conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/configuredtimeoffsetfromlive)*