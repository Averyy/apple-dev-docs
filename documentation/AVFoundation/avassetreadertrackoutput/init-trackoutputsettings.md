# init(track:outputSettings:)

**Framework**: AVFoundation  
**Kind**: init

Creates an object that reads media data from an asset track.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(track: AVAssetTrack, outputSettings: [String : Any]?)
```

## Parameters

- `track`: The track from which to read media samples.
- `outputSettings`: You use keys and values from  ,  , or  , depending on the media type and the output format you require.

## See Also

- [Video settings](video-settings.md)
  Configure video processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/init(track:outputsettings:))*