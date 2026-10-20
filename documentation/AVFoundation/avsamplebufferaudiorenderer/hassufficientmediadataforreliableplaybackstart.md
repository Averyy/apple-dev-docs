# hasSufficientMediaDataForReliablePlaybackStart

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Indicates whether the enqueued media data meets the renderer’s preroll level.

**Availability**:
- iOS 14.5+ - Deprecated in 27.0
- iPadOS 14.5+ - Deprecated in 27.0
- Mac Catalyst 14.5+ - Deprecated in 27.0
- macOS 11.3+ - Deprecated in 27.0
- tvOS 14.5+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 7.4+ - Deprecated in 27.0

> **Deprecated**: For smooth playback, attach the renderer to a render synchronizer and set the synchronizer's delaysRateChangeUntilHasSufficientMediaData property to true instead

## Declaration

```swift
var hasSufficientMediaDataForReliablePlaybackStart: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasSufficientMediaDataForReliablePlaybackStart;
```

#### Discussion

Clients should fetch the value of this property to learn if the renderer has had enough media data enqueued to start playback reliably. Starting playback when this property is NO may prevent smooth playback following an immediate start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/hassufficientmediadataforreliableplaybackstart)*