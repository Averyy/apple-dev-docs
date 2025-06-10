# init(videoRenderer:)

**Framework**: RealityKit  
**Kind**: init

Creates a video player component from a sample buffer video renderer object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(videoRenderer: AVSampleBufferVideoRenderer)
```

#### Discussion

To create a `VideoPlayerComponent`, first create an [`AVSampleBufferVideoRenderer`](https://developer.apple.com/documentation/AVFoundation/AVSampleBufferVideoRenderer) instance with no parameters and then pass that to the `VideoPlayerComponent` initializer. After creating the `VideoPlayerComponent`, create an [`AVAssetReader`](https://developer.apple.com/documentation/AVFoundation/AVAssetReader) with the [`AVURLAsset`](https://developer.apple.com/documentation/AVFoundation/AVURLAsset) and load the media (video), which you need to track as the [`AVAssetTrack`](https://developer.apple.com/documentation/AVFoundation/AVAssetTrack). Feed this `AVAssetTrack` to the [`AVAssetReaderTrackOutput`](https://developer.apple.com/documentation/AVFoundation/AVAssetReaderTrackOutput)
and add this output tracker to the `AVAssetReader`.

Wait for setup to finish and start reading. Read the sample buffers from the reader and enqueue it into the `AVSampleBufferVideoRenderer` object. `AVSampleBufferVideoRenderer` uses a push model, so feed the video sample buffers until the queue is full, and then resume feeding it when it’s ready for more. You can use `isReadyForMoreMediaData` on the `AVSampleBufferVideoRenderer` object in a while-loop to check whether you need to enqueue more sample buffers. You can’t use the same `AVSampleBufferVideoRenderer` object with more than one `VideoPlayerComponent`.

You need to synchronize the audio, captions, and playback rate separately in your app.

The following code example demonstrates this process:

```swift
// Create an `AVSampleBufferVideoRenderer` instance to control playback of a movie.
let videoRenderer = AVSampleBufferVideoRenderer()

// Create an entity for display.
let videoEntity = Entity()

// Create a `VideoPlayerComponent` object that supplies the `AVSampleBufferVideoRenderer` object.
let videoPlayerComponent = VideoPlayerComponent(videoRenderer: videoRenderer)
videoEntity.components[VideoPlayerComponent.self] = videoPlayerComponent

// Create a URL that points to the movie file.
if let url = Bundle.main.url(forResource: "MyMovie", withExtension: "mp4") {

    let sourceAsset = AVURLAsset(url: url)
    let sourceAssetReader = AVAssetReader(asset: sourceAsset)
    let sourceAssetVideoTrack = sourceAsset.loadTracks(withMediaType: .video).first
    let sourceAssetReaderVideoTrackOutput = AVAssetReaderTrackOutput(track: sourceAssetVideoTrack!, outputSettings: nil)
    sourceAssetReader.add(sourceAssetReaderVideoTrackOutput!)

    sourceAssetReader.startReading()
    videoRenderer.requestMediaDataWhenReady(on: DispatchQueue.global()) {
      while videoRenderer.isReadyForMoreMediaData {
          if let sampleBuffer = sourceAssetReaderVideoTrackOutput!.copyNextSampleBuffer() {
              videoRenderer.enqueue(sampleBuffer)
          } else {
              videoRenderer.stopRequestingMediaData()
              return
          }
      }
  }
}
```

## Parameters

- `videoRenderer`: The sample buffer video renderer with the visual contents the component   presents.

## See Also

- [init(avPlayer: AVPlayer)](videoplayercomponent/init(avplayer:).md)
  Creates a video player component from an AV player object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videoplayercomponent/init(videorenderer:))*