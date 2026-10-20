# automaticallyPreservesTimeOffsetFromLive

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player preserves its time offset from the live time after a buffering operation.

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
var automaticallyPreservesTimeOffsetFromLive: Bool { get set }
```

```objc
@property (nonatomic) BOOL automaticallyPreservesTimeOffsetFromLive;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md). If the value is [`true`](../../Swift/true.md), the player seeks forward after it finishes buffering to restore the position that the playhead had when buffering began, relative to the end of the player item’s [`seekableTimeRanges`](./seekabletimeranges.md) property value.

> **Note**:  This property value has no effect if the asset isn’t a live stream.

## See Also

### Managing time offsets
- [var recommendedTimeOffsetFromLive: CMTime](./recommendedtimeoffsetfromlive.md)
  A recommended time offset from the live time based on observed network conditions.
- [var configuredTimeOffsetFromLive: CMTime](./configuredtimeoffsetfromlive.md)
  A time value that indicates the offset from the live time to start playback, or resume playback after a seek to positive infinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/automaticallypreservestimeoffsetfromlive)*