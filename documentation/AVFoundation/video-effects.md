# Video effects

**Framework**: AVFoundation

Define standard video transition effects, synchronize layer animations with media timing, and create custom video compositors.

## Topics

### Core Animation integration
- [class AVVideoCompositionCoreAnimationTool](avvideocompositioncoreanimationtool.md)
  An object used to incorporate Core Animation into a video composition.
### Built-in video compositing
- [Editing and playing HDR video](editing-and-playing-hdr-video.md)
  Support high-dynamic-range (HDR) video content in your app by using the HDR editing and playback capabilities of AVFoundation.
- [Debugging AVFoundation audio mixes, compositions, and video compositions](debugging-avfoundation-audio-mixes-compositions-and-video-compositions.md)
  Resolve common problems when creating compositions, video compositions, and audio mixes.
- [class AVVideoComposition](avvideocomposition.md)
  An object that describes how to compose video frames at particular points in time.
- [class AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md)
  An operation that a compositor performs.
- [class AVVideoCompositionLayerInstruction](avvideocompositionlayerinstruction.md)
  An object used to modify the transform, cropping, and opacity ramps applied to a given track in a composition.
- [class AVMutableVideoComposition](avmutablevideocomposition.md)
  A mutable video composition subclass.
- [class AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md)
  A mutable video composition instruction subclass.
- [class AVMutableVideoCompositionLayerInstruction](avmutablevideocompositionlayerinstruction.md)
  An object used to modify the transform, cropping, and opacity ramps applied to a given track in a mutable composition.
### Custom video compositing
- [Processing spatial video with a custom video compositor](processing-spatial-video-with-a-custom-video-compositor.md)
  Create a custom video compositor to edit spatial video for playback and export.
- [protocol AVVideoCompositing](avvideocompositing.md)
  A protocol that defines the methods custom video compositors must implement.

## See Also

- [Composite assets](composite-assets.md)
  Combine tracks and segments of tracks from multiple assets into a composite asset that you can play or process.
- [QuickTime movies](quicktime-movies.md)
  Access the contents of a QuickTime movie file, and perform sample-level edits of its media tracks.
- [Audio mixing](audio-mixing.md)
  Define how to mix the audio levels from multiple audio tracks over an asset’s duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/video-effects)*