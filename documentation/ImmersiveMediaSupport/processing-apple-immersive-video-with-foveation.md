# Processing Apple Immersive Video with foveation

**Framework**: Immersive Media Support

Reduce a video’s data rate while maintaining high acuity in the center of the imagery by applying foveation to immersive video content.

**Availability**:
- macOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

Apple Immersive Video (AIV) uses very high resolution cameras capable of capturing video that exceeds 8K per eye at 90 frames per second (fps), which is over 10 billion pixels per second.

Because it’s impractical to stream that many pixels over even the fastest available networks, AIV can optionally use static foveation to reduce the overall resolution to a streamable 4K, while maintaining most of the perceptual resolution at the original 90 fps.

> **Note**: This sample code project is associated with WWDC26 session 287: [`Build next generation experiences with visionOS 27`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2026/287).

##### Configure the Sample Code Project

To run this sample app, you need to [`download`](https://developer.apple.comhttps://devstreaming-cdn.apple.com/videos/streaming/examples/immersive-media/AIV/Apple_Immersive_Video_Dual_Track_Foveation.zip) and expand a zip file that contains an example QuickTime movie and supporting content.

To run the app in Xcode, choose Product > Scheme > Edit Scheme, and update the command-line arguments to reference the downloaded files:

- **`--input`**: An Apple Immersive Video (AIV) mezzanine QuickTime file with two ProRes tracks.
- **`--aime`**: An Apple Immersive Media Embedded (AIME) metadata file with the correct camera calibrations for the provided input file.
- **`--output`**: A directory path where the sample writes the updated AIME metadata file and foveated AIV QuickTime file.

## See Also

- [Authoring Apple Immersive Video](authoring-apple-immersive-video.md)
  Prepare and package immersive video content for delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/processing-apple-immersive-video-with-foveation)*