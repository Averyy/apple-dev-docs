# init(videoTracks:videoSettings:)

**Framework**: AVFoundation  
**Kind**: init

Creates an object that reads composited video frames from the specified video tracks.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(videoTracks: [AVAssetTrack], videoSettings: [String : Any]?)
```

## Parameters

- `videoTracks`: An array of asset tracks from which to read video frames for compositing. The media type of each track must be  .
- `videoSettings`: Specifying a   value configures the output to return samples in an uncompressed format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/init(videotracks:videosettings:))*