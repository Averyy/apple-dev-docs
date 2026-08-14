# hasSufficientMediaDataForReliablePlaybackStart

**Framework**: AVFoundation  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the enqued media meets the required preroll level for reliable playback.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.4+

## Declaration

```swift
var hasSufficientMediaDataForReliablePlaybackStart: Bool { get }
```

#### Discussion

Starting playback when this property is [`false`](https://developer.apple.com/documentation/swift/false) may prevent smooth playback following an immediate start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/hassufficientmediadataforreliableplaybackstart)*