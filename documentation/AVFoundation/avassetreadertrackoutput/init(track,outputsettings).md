# init(track:outputSettings:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithTrack:(AVAssetTrack *) track outputSettings:(NSDictionary<NSString *,id> *) outputSettings;
```

## Parameters

- `track`: The track from which to read media samples.
- `outputSettings`: A dictionary of settings to use for sample output. Specify `nil` to receive samples in their storage format.

  You use keys and values from [Audio settings](../audio-settings.md), [Video settings](../video-settings.md), or [`CVPixelBuffer`](../../CoreVideo/cvpixelbuffer.md), depending on the media type and the output format you require.

## See Also

### Creating a track output
- [Video settings](../video-settings.md)
  Configure video processing settings using standard key and value constants.
- [+ assetReaderTrackOutputWithTrack:outputSettings:](./assetreadertrackoutputwithtrack_outputsettings_.md)
  Returns a new object that reads media data from an asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/init(track:outputsettings:))*