# supportedPlaybackRates

**Framework**: Media Player  
**Kind**: property

The supported playback rates for a media item.

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
var supportedPlaybackRates: [NSNumber] { get set }
```

#### Discussion

Contains an array of [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects. Each object is of type `float` and designates a supported playback rate. For example, a value of `2.0` would indicate the media item plays at double speed. Negative values are not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackratecommand/supportedplaybackrates)*