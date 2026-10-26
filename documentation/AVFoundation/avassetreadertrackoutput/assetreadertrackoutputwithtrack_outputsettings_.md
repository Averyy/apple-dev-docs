# assetReaderTrackOutputWithTrack:outputSettings:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new object that reads media data from an asset track.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) assetReaderTrackOutputWithTrack:(AVAssetTrack *) track outputSettings:(NSDictionary<NSString *,id> *) outputSettings;
```

#### Return Value

A new asset reader, or `nil` if initialization fails.

## Parameters

- `track`: The track from which to read media samples.
- `outputSettings`: A dictionary of settings to use for sample output. Specify `nil` to receive samples in their storage format.

  You use keys and values from [Audio settings](../audio-settings.md), [Video settings](../video-settings.md), or [`CVPixelBuffer`](../../CoreVideo/cvpixelbuffer.md), depending on the media type and the output format you require.

## See Also

### Creating a track output
- [init(track: AVAssetTrack, outputSettings: [String : Any]?)](./init%28track,outputsettings%29.md)
  Creates an object that reads media data from an asset track.
- [Video settings](../video-settings.md)
  Configure video processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/assetreadertrackoutputwithtrack:outputsettings:)*