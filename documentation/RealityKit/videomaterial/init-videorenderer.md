# init(videoRenderer:)

**Framework**: RealityKit  
**Kind**: init

Creates and initializes a video material for a sample buffer video renderer object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
init(videoRenderer: AVSampleBufferVideoRenderer)
```

#### Discussion

To create a `VideoMaterial`, first create an [`AVSampleBufferVideoRenderer`](https://developer.apple.com/documentation/AVFoundation/AVSampleBufferVideoRenderer) instance with no parameters and then pass that to the `VideoMaterial` initializer. After creating the `VideoMaterial`, create a [`AVAssetReader`](https://developer.apple.com/documentation/AVFoundation/AVAssetReader) with the [`AVURLAsset`](https://developer.apple.com/documentation/AVFoundation/AVURLAsset) and load the media (video), which you need to track as the [`AVAssetTrack`](https://developer.apple.com/documentation/AVFoundation/AVAssetTrack). Feed this `AVAssetTrack` to the [`AVAssetReaderTrackOutput`](https://developer.apple.com/documentation/AVFoundation/AVAssetReaderTrackOutput) and add this output tracker to the `AVAssetReader` you created before. Wait for setup to finish and start reading. Read the sample buffers from the reader and enqueue it into the `AVSampleBufferVideoRenderer` object. `AVSampleBufferVideoRenderer` uses a push model, so feed the video sample buffers until the queue is full and then resume feeding it when it’s ready for more. You can use `isReadyForMoreMediaData` on the `AVSampleBufferVideoRenderer` object in a while-loop to check if you need to enqueue more sample buffers. You can’t use the same `AVSampleBufferVideoRenderer` object with more than one `VideoMaterial`.

You need to synchronize the audio, captions, and playback rate separately in your application.

The following code example demonstrates how to synchronize video with audio:

```swift
// Create an `AVSampleBufferVideoRenderer` instance to control playback of a movie.
let videoRenderer = AVSampleBufferVideoRenderer()

// Create an `AVSampleBufferAudioRenderer` instance to control audio of the playback.
let audioRenderer = AVSampleBufferAudioRenderer()

// Create a `AVSampleBufferRenderSynchronizer` instance to synchronize video and audio.
let synchronizer = AVSampleBufferRenderSynchronizer()

// Add both videoRenderer and audioRenderer to the synchronizer.
synchronizer.addRenderer(videoRenderer)
synchronizer.addRenderer(audioRenderer)

// Create an entity for display.
let entity = ModelEntity()

// Create a `VideoMaterial` object that supplies the `AVSampleBufferVideoRenderer` object.
entity.model = .init(mesh: plane, materials: [VideoMaterial(videoRenderer: videoRenderer)])

// Create a URL that points to the movie file.
if let url = Bundle.main.url(forResource: "MyMovie", withExtension: "mp4") {

    let sourceAsset = AVURLAsset(url: url)
    let sourceAssetReader = AVAssetReader(asset: sourceAsset)
    let sourceAssetVideoTrack = sourceAsset.loadTracks(withMediaType: .video).first
    let sourceAssetAudioTrack = sourceAsset.loadTracks(withMediaType: .audio).first
    let sourceAssetReaderVideoTrackOutput = AVAssetReaderTrackOutput(track: sourceAssetVideoTrack!, outputSettings: nil)
    let sourceAssetReaderAudioTrackOutput = AVAssetReaderTrackOutput(track: sourceAssetAudioTrack!, outputSettings: nil)
    sourceAssetReader.add(sourceAssetReaderVideoTrackOutput!)
    sourceAssetReader.add(sourceAssetReaderAudioTrackOutput!)

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

    audioRenderer.requestMediaDataWhenReady(on: DispatchQueue.global()) {
        while audioRenderer.isReadyForMoreMediaData {
            if let sampleBuffer = sourceAssetReaderAudioTrackOutput!.copyNextSampleBuffer() {
                audioRenderer.enqueue(sampleBuffer)
            } else {
                audioRenderer.stopRequestingMediaData()
                return
            }
        }
    }

    // Start the playback immediately.
    synchronizer.setRate(1, time: .zero)

}
```

## Parameters

- `videoRenderer`: The sample buffer video renderer whose visual contents the material presents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videomaterial/init(videorenderer:))*