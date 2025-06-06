# Sample buffer playback

**Framework**: AVFoundation

Create custom controllers to play and synchronize the timing of sample buffer streams.

## Topics

### Sample buffer generation
- [Playing custom audio with your own player](../AVFAudio/playing-custom-audio-with-your-own-player.md)
  Construct an audio player to play your custom audio data, and optionally take advantage of the advanced features of AirPlay 2.
- [class AVSampleBufferRequest](avsamplebufferrequest.md)
  An object that describes a sample buffer creation request.
- [class AVSampleBufferGenerator](avsamplebuffergenerator.md)
  An object that creates sample buffers.
- [class AVSampleBufferGeneratorBatch](avsamplebuffergeneratorbatch.md)
  An object that generates sample buffers in a batch.
### Presentation
- [protocol AVQueuedSampleBufferRendering](avqueuedsamplebufferrendering.md)
  Methods you can implement to enqueue sample buffers for presentation.
- [class AVSampleBufferRenderSynchronizer](avsamplebufferrendersynchronizer.md)
  An object used to synchronize multiple queued sample buffers to a single timeline.
- [class AVSampleBufferDisplayLayer](avsamplebufferdisplaylayer.md)
  An object that displays compressed or uncompressed video frames.
- [class AVSampleBufferVideoRenderer](avsamplebuffervideorenderer.md)
  An object that enqueues video sample buffers for rendering.
- [class AVSampleBufferAudioRenderer](avsamplebufferaudiorenderer.md)
  An object used to decompress audio and play compressed or uncompressed audio.

## See Also

- [Media playback](media-playback.md)
  Manage the playback of media assets and interstitial content, independent of how you present that content in your interface.
- [Offline playback and storage](offline-playback-and-storage.md)
  Download streamed content to disk to allow offline playback, and define policies to automatically remove downloaded assets.
- [Streaming and AirPlay](streaming-and-airplay.md)
  Stream content wirelessly to other devices using AirPlay, and handle requests involving FairPlay-protected assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/sample-buffer-playback)*