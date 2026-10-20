# hasSufficientMediaDataForReliablePlaybackStart

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the enqued media meets the required preroll level for reliable playback.

**Availability**:
- iOS 14.5+ - Deprecated in 27.0
- iPadOS 14.5+ - Deprecated in 27.0
- Mac Catalyst 14.5+ - Deprecated in 27.0
- macOS 11.3+ - Deprecated in 27.0
- tvOS 14.5+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 7.4+ - Deprecated in 27.0

## Declaration

```swift
var hasSufficientMediaDataForReliablePlaybackStart: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasSufficientMediaDataForReliablePlaybackStart;
```

#### Discussion

Starting playback when this property is [`false`](../../Swift/false.md) may prevent smooth playback following an immediate start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/hassufficientmediadataforreliableplaybackstart)*