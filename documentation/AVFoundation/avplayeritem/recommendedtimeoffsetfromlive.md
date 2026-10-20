# recommendedTimeOffsetFromLive

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A recommended time offset from the live time based on observed network conditions.

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
var recommendedTimeOffsetFromLive: CMTime { get }
```

```objc
@property (readonly) CMTime recommendedTimeOffsetFromLive;
```

#### Discussion

For nonlive stream content, the value is [`invalid`](../../CoreMedia/cmtime/invalid.md).

## See Also

### Managing time offsets
- [var automaticallyPreservesTimeOffsetFromLive: Bool](./automaticallypreservestimeoffsetfromlive.md)
  A Boolean value that indicates whether the player preserves its time offset from the live time after a buffering operation.
- [var configuredTimeOffsetFromLive: CMTime](./configuredtimeoffsetfromlive.md)
  A time value that indicates the offset from the live time to start playback, or resume playback after a seek to positive infinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/recommendedtimeoffsetfromlive)*