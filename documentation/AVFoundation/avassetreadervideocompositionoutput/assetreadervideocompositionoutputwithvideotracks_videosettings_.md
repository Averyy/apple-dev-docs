# assetReaderVideoCompositionOutputWithVideoTracks:videoSettings:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new object that reads composited video from the specified video tracks.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) assetReaderVideoCompositionOutputWithVideoTracks:(NSArray<AVAssetTrack *> *) videoTracks videoSettings:(NSDictionary<NSString *,id> *) videoSettings;
```

## Return Value

A new video composition output, or `nil` if initialization fails.

## Parameters

- `videoTracks`: An array of asset tracks from which the created object should read video frames for compositing. The media type of each track must be [`video`](../avmediatype/video.md).
- `videoSettings`: A dictionary of video settings to use for sample output, or `nil` if you want to receive decoded samples in a convenient uncompressed format, with properties determined according to the properties of the specified video tracks.

  You use keys from [`CVPixelBuffer`](../../CoreVideo/cvpixelbuffer.md), depending on the output format you want.

## See Also

### Creating a video composition output
- [init(videoTracks: [AVAssetTrack], videoSettings: [String : Any]?)](./init%28videotracks,videosettings%29.md)
  Creates an object that reads composited video frames from the specified video tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/assetreadervideocompositionoutputwithvideotracks:videosettings:)*