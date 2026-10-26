# requestAVAsset(forVideo:options:resultHandler:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Requests AVFoundation objects representing the video asset’s content and state, to be loaded asynchronously.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func requestAVAsset(forVideo asset: PHAsset, options: PHVideoRequestOptions?, resultHandler: @escaping (AVAsset?, AVAudioMix?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

```objc
- (PHImageRequestID) requestAVAssetForVideo:(PHAsset *) asset options:(PHVideoRequestOptions *) options resultHandler:(void (^)(AVAsset *asset, AVAudioMix *audioMix, NSDictionary *info)) resultHandler;
```

#### Return Value

A numeric identifier for the request. If you need to cancel the request before it completes, pass this identifier to the [`cancelImageRequest(_:)`](./cancelimagerequest%28_%29.md) method.

#### Discussion

When you call this method, Photos downloads the video data (if necessary) and creates AVFoundation objects. It then calls your `resultHandler` block to provide the requested video.

Use this method when you want to work with the arrangement of audio and video tracks that an asset contains. If you plan to use the asset only for playback, call the [`requestPlayerItem(forVideo:options:resultHandler:)`](./requestplayeritem%28forvideo,options,resulthandler%29.md) method. If you plan to export the asset data, call the [`requestExportSession(forVideo:options:exportPreset:resultHandler:)`](./requestexportsession%28forvideo,options,exportpreset,resulthandler%29.md) method.

## Parameters

- `asset`: The video asset for which video objects are to be loaded.
- `options`: Options specifying how Photos should handle the request and notify your app of progress or errors. For details, see [`PHVideoRequestOptions`](../phvideorequestoptions.md).
- `resultHandler`: A block that Photos calls after loading the asset’s data.

  The block takes the following parameters:

  - **asset**: An object that provides access to the video asset as a collection of tracks and metadata. For details on working with [`AVAsset`](../../AVFoundation/avasset.md) objects, see [AVFoundation Programming Guide](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40010188).
  - **audioMix**: Use this object to rearrange the asset’s audio tracks, edit additional audio into the mix, or configure an [`AVAssetReaderOutput`](../../AVFoundation/avassetreaderoutput.md) object for exporting the asset’s audio data. If `nil`, the asset uses a default audio mix.
  - **info**: A dictionary providing information about the status of the request. See [Image Result Info Keys](../../PhotoKit/image-result-info-keys.md) for possible keys and values.

## See Also

### Requesting Video Objects
- [func requestPlayerItem(forVideo: PHAsset, options: PHVideoRequestOptions?, resultHandler: (AVPlayerItem?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID](./requestplayeritem%28forvideo,options,resulthandler%29.md)
  Requests a representation of the video asset for playback, to be loaded asynchronously.
- [func requestExportSession(forVideo: PHAsset, options: PHVideoRequestOptions?, exportPreset: String, resultHandler: (AVAssetExportSession?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID](./requestexportsession%28forvideo,options,exportpreset,resulthandler%29.md)
  Requests an export session for writing the video asset’s data to a file, to be loaded asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagemanager/requestavasset(forvideo:options:resulthandler:))*