# VideoMaterial

**Framework**: RealityKit  
**Kind**: struct

A material that supports animated textures.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS ?+

## Declaration

```swift
struct VideoMaterial
```

#### Overview

In RealityKit, a  is an object that defines the surface properties of a rendered 3D object. A `VideoMaterial` is a material that maps a movie file on to the surface of an entity. Video materials are , which means that scene lighting doesn’t affect them. Video materials support transparency if the source video’s file format also supports transparency.

Video materials use an [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) instance to control movie playback. You can use any movie file format that [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) supports to create a video material. To control playback of the material’s video, use the [`avPlayer`](videomaterial/avplayer.md) property, which offers methods like [`play()`](https://developer.apple.com/documentation/AVFoundation/AVPlayer/play()) and [`pause()`](https://developer.apple.com/documentation/AVFoundation/AVPlayer/pause()).

The following code demonstrates how to create and start playing a video material using a movie file from your application bundle.

```swift
// Create a URL that points to the movie file.
if let url = Bundle.main.url(forResource: "MyMovie", withExtension: "mp4") {

    // Create an AVPlayer instance to control playback of that movie.
    let player = AVPlayer(url: url)

    // Instantiate and configure the video material.
    let material = VideoMaterial(avPlayer: player)

    // Configure audio playback mode.
    material.controller.audioInputMode = .spatial

    // Create a new model entity using the video material.
    let modelEntity = ModelEntity(mesh: cube, materials: [material])

    // Start playing the video.
    player.play()
}
```

To see an example of using a video texture in RealityKit, see [`Creating a game with scene understanding`](creating_a_game_with_scene_understanding.md).

## Topics

### Creating a video material
- [init(avPlayer: AVPlayer)](videomaterial/init(avplayer:).md)
  Creates a new video material.
### Controlling playback
- [var avPlayer: AVPlayer?](videomaterial/avplayer.md)
  The material’s video playback controller.
- [var controller: VideoPlaybackController](videomaterial/controller.md)
  An object that configures framework-specific video options.
### Initializers
- [init(videoRenderer: AVSampleBufferVideoRenderer)](videomaterial/init(videorenderer:).md)
  Creates and initializes a video material for a sample buffer video renderer object.
### Instance Properties
- [var faceCulling: VideoMaterial.FaceCulling](videomaterial/faceculling-swift.property.md)
  A process in which the system specifies polygons to remove before rendering a mesh using this material.
- [var readsDepth: Bool](videomaterial/readsdepth.md)
  A boolean value that determines whether this material performs the depth test by reading RealityKit’s depth buffer.
- [var triangleFillMode: VideoMaterial.TriangleFillMode](videomaterial/trianglefillmode-swift.property.md)
  The object that controls how RealityKit draws triangles.
- [var videoRenderer: AVSampleBufferVideoRenderer?](videomaterial/videorenderer.md)
  The material’s video renderer.
- [var writesDepth: Bool](videomaterial/writesdepth.md)
  A boolean value that determines whether this material writes its depth into RealityKit’s depth buffer.
### Type Aliases
- [VideoMaterial.FaceCulling](videomaterial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [VideoMaterial.TriangleFillMode](videomaterial/trianglefillmode-swift.typealias.md)
### Default Implementations
- [Material Implementations](videomaterial/material-implementations.md)

## Relationships

### Conforms To
- [Material](material.md)

## See Also

- [VideoMaterial.FaceCulling](videomaterial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [VideoMaterial.TriangleFillMode](videomaterial/trianglefillmode-swift.typealias.md)
- [VideoMaterial.Parameters](videomaterial/parameters.md)
  The parameter type that custom materials uses for properties the framework passes to shader functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videomaterial)*