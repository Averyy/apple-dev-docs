# playbackRate

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The chosen playback rate for the command event.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 7.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var playbackRate: Float { get }
```

```objc
@property (nonatomic, readonly) float playbackRate;
```

#### Discussion

The `playbackRate` property is equal to a value stored in the [`supportedPlaybackRates`](../mpchangeplaybackratecommand/supportedplaybackrates.md) array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackratecommandevent/playbackrate)*