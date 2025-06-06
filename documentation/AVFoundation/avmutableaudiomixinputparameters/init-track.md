# init(track:)

**Framework**: AVFoundation  
**Kind**: init

Creates a mutable input parameters object for a given track.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
convenience init(track: AVAssetTrack?)
```

#### Return Value

A mutable input parameters object with no volume ramps and [`trackID`](avmutableaudiomixinputparameters/trackid.md) set to `track`’s identifier.

## Parameters

- `track`: The track to associate with the input parameters object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/init(track:))*