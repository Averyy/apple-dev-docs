# init(audioTracks:audioSettings:)

**Framework**: AVFoundation  
**Kind**: init

Creates an object that reads mixed audio from the specified audio tracks.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(audioTracks: [AVAssetTrack], audioSettings: [String : Any]?)
```

## Parameters

- `audioTracks`: An array of track objects of type   from which to source the sample buffers to mix.
- `audioSettings`: For non-  audio settings, the dictionary must contain values for the   keys. The output doesn’t support the   constant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/init(audiotracks:audiosettings:))*