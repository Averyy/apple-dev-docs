# requestPlayerItem(forVideo:options:resultHandler:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Requests a representation of the video asset for playback, to be loaded asynchronously.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func requestPlayerItem(forVideo asset: PHAsset, options: PHVideoRequestOptions?, resultHandler: @escaping (AVPlayerItem?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

```objc
- (PHImageRequestID) requestPlayerItemForVideo:(PHAsset *) asset options:(PHVideoRequestOptions *) options resultHandler:(void (^)(AVPlayerItem *playerItem, NSDictionary *info)) resultHandler;
```

#### Return Value

A numeric identifier for the request. If you need to cancel the request before it completes, pass this identifier to the [`cancelImageRequest(_:)`](./cancelimagerequest%28_%29.md) method.

#### Discussion

When you call this method, Photos downloads the video data (if necessary) and creates a player item. It then calls your `resultHandler` block to provide the requested video.

Use this method when you want to simply play back the video asset as it currently exists. For more detailed options or to work with the asset’s audio and video tracks, use the [`requestAVAsset(forVideo:options:resultHandler:)`](./requestavasset%28forvideo,options,resulthandler%29.md) method instead.

## Parameters

- `asset`: The video asset to be played back.
- `options`: Options specifying how Photos should handle the request and notify your app of progress or errors. For details, see [`PHVideoRequestOptions`](../phvideorequestoptions.md).
- `resultHandler`: A block Photos calls after loading the asset’s data and preparing the player item.

  The block takes the following parameters:

  - **playerItem**: An [`AVPlayerItem`](../../AVFoundation/avplayeritem.md) object that you can use for playing back the video asset.
  - **info**: A dictionary providing information about the status of the request. See [Image Result Info Keys](../../PhotoKit/image-result-info-keys.md) for possible keys and values.

## See Also

### Requesting Video Objects
- [func requestExportSession(forVideo: PHAsset, options: PHVideoRequestOptions?, exportPreset: String, resultHandler: (AVAssetExportSession?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID](./requestexportsession%28forvideo,options,exportpreset,resulthandler%29.md)
  Requests an export session for writing the video asset’s data to a file, to be loaded asynchronously.
- [func requestAVAsset(forVideo: PHAsset, options: PHVideoRequestOptions?, resultHandler: (AVAsset?, AVAudioMix?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID](./requestavasset%28forvideo,options,resulthandler%29.md)
  Requests AVFoundation objects representing the video asset’s content and state, to be loaded asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagemanager/requestplayeritem(forvideo:options:resulthandler:))*