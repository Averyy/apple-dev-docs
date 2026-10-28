# requestExportSession(forVideo:options:exportPreset:resultHandler:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Requests an export session for writing the video asset’s data to a file, to be loaded asynchronously.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func requestExportSession(forVideo asset: PHAsset, options: PHVideoRequestOptions?, exportPreset: String, resultHandler: @escaping (AVAssetExportSession?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

```objc
- (PHImageRequestID) requestExportSessionForVideo:(PHAsset *) asset options:(PHVideoRequestOptions *) options exportPreset:(NSString *) exportPreset resultHandler:(void (^)(AVAssetExportSession *exportSession, NSDictionary *info)) resultHandler;
```

## Return Value

A numeric identifier for the request. If you need to cancel the request before it completes, pass this identifier to the [`cancelImageRequest(_:)`](./cancelimagerequest%28_%29.md) method.

## Discussion

When you call this method, Photos downloads the video data (if necessary) and creates an export session. It then calls your `resultHandler` block to provide the requested video.

For additional export options, use the [`requestAVAsset(forVideo:options:resultHandler:)`](./requestavasset%28forvideo,options,resulthandler%29.md) method and then create [`AVAssetReader`](../../AVFoundation/avassetreader.md) and [`AVAssetWriter`](../../AVFoundation/avassetwriter.md) objects to transcode and output the video asset’s data.

## Parameters

- `asset`: The video asset for which an export session is to be created.
- `options`: Options specifying how Photos should handle the request and notify your app of progress or errors. For details, see [`PHVideoRequestOptions`](../phvideorequestoptions.md).
- `exportPreset`: The export preset name for exporting the asset. For available presets, see [`AVAssetExportSession`](../../AVFoundation/avassetexportsession.md).
- `resultHandler`: A block that Photos calls after loading the asset’s data and preparing the export session.

  The block takes the following parameters:

  - **exportSession**: An [`AVAssetExportSession`](../../AVFoundation/avassetexportsession.md) object that you can use for writing the video asset’s data to a file.
  - **info**: A dictionary that provides information about the status of the request. See [Image Result Info Keys](../../PhotoKit/image-result-info-keys.md) for possible keys and values.

## See Also

### Requesting Video Objects
- [func requestPlayerItem(forVideo: PHAsset, options: PHVideoRequestOptions?, resultHandler: (AVPlayerItem?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID](./requestplayeritem%28forvideo,options,resulthandler%29.md)
  Requests a representation of the video asset for playback, to be loaded asynchronously.
- [func requestAVAsset(forVideo: PHAsset, options: PHVideoRequestOptions?, resultHandler: (AVAsset?, AVAudioMix?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID](./requestavasset%28forvideo,options,resulthandler%29.md)
  Requests AVFoundation objects representing the video asset’s content and state, to be loaded asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagemanager/requestexportsession(forvideo:options:exportpreset:resulthandler:))*