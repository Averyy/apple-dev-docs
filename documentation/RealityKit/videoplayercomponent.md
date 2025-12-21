# VideoPlayerComponent

**Framework**: RealityKit  
**Kind**: struct

A component that supports general video-playback experience with an AV player.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct VideoPlayerComponent
```

#### Overview

To streamline and enhance video playback controls, a video player component empowers an app to support captions, subtitles, light spill, and passthrough tinting (visionOS only). Attach a `VideoPlayerComponent` to an entity to start configuring playback controls.

The example below shows an entity with a [`VideoPlayerComponent`](videoplayercomponent.md) attached:

The following code example shows the basic setup for initializing a `VideoPlayerComponent` with an [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer):

```swift
// Create an entity for display.
let videoEntity = Entity()

// Create an AV player with a URL.
let player = AVPlayer(url: "PLACEMENT_URL")

// Create a video player component with the AV player.
let videoPlayerComponent = VideoPlayerComponent(avPlayer: player)

// Attach the video player component to the entity.
videoEntity.components.set(videoPlayerComponent)
```

Here are some common usage scenarios before attaching the video player component to the entity:

```swift
// Set the desired viewing mode to stereo to enable 
// stereoscopic playback of the video, if available.
videoPlayerComponent.desiredViewingMode = VideoPlaybackController.ViewingMode.stereo

// Enable passthrough tinting during video playback.
videoPlayerComponent.isPassthroughTintingEnabled = true
```

Here are a few event subscription examples for [`VideoPlayerEvents`](videoplayerevents.md):

```swift
RealityView { content in
    // Set up a video player component with an AV player.
    let entity = Entity()
    let player = AVPlayer(url: "PLACEMENT_URL")
    let videoPlayerComponent = VideoPlayerComponent(avPlayer: player)
    player.play()
    entity.components.set(videoPlayerComponent)

    var subscription: EventSubscription?

    // Subscribe to the video screen size change event.
    subscription = content.subscribe(to:
        VideoPlayerEvents.VideoSizeDidChange.self) { event in
        print("video size did change: \(event.videoDimension)")
    }

   // Subscribe to the current viewing mode change event.
    subscription = content.subscribe(to:
        VideoPlayerEvents.ViewingModeDidChange.self) { event in
        print("viewing mode did change: \(event.currentViewingMode)")
    }

    // Subscribe to the content type change event.
    subscription = content.subscribe(to:
        VideoPlayerEvents.ContentTypeDidChange.self) { event in
        print("content type did change: \(event.contentType.rawValue)")
    }

    content.add(entity)
}
```

##### Playing Immersive Video

On visionOS, you can also use `VideoPlayerComponent` to play immersive media with RealityKit. Watch videos in a window alongside other Shared Space apps, or watch immersive video with a 180-degree field of view in a fully immersive space, or watch immersive video with a progressive view in a progressive immersive space

##### Playing Immersive Video with a 180 Degree Field of View

To play the immersive media with a 180-degree field of view, first set up a fully immersive space, and then set [`desiredImmersiveViewingMode`](videoplayercomponent/desiredimmersiveviewingmode.md) to [`VideoPlayerComponent.ImmersiveViewingMode.full`](videoplayercomponent/immersiveviewingmode-swift.enum/full.md).

If you want to switch the immersive-viewing mode to `full` while immersive-media playback is in [`VideoPlayerComponent.ImmersiveViewingMode.portal`](videoplayercomponent/immersiveviewingmode-swift.enum/portal.md) mode, wait for the scene event named [`VideoPlayerEvents.ImmersiveViewingModeDidChange`](videoplayerevents/immersiveviewingmodedidchange.md) to trigger after you set [`desiredImmersiveViewingMode`](videoplayercomponent/desiredimmersiveviewingmode.md) to `full`. Then, dismiss the window scene and open up a fully immersive space scene.

##### Playing Immersive Video with a Progressive View

To play the immersive media with a progressive view, first set up a progressive immersive space, and then set [`desiredImmersiveViewingMode`](videoplayercomponent/desiredimmersiveviewingmode.md) to [`VideoPlayerComponent.ImmersiveViewingMode.progressive`](videoplayercomponent/immersiveviewingmode-swift.enum/progressive.md).

If you want to switch the immersive-viewing mode to `progressive` while immersive-media playback is in [`VideoPlayerComponent.ImmersiveViewingMode.portal`](videoplayercomponent/immersiveviewingmode-swift.enum/portal.md) mode, wait for the scene event named [`VideoPlayerEvents.ImmersiveViewingModeDidChange`](videoplayerevents/immersiveviewingmodedidchange.md) to trigger after you set [`desiredImmersiveViewingMode`](videoplayercomponent/desiredimmersiveviewingmode.md) to `progressive`. Then, dismiss the window scene and open up a progressive immersive space scene.

##### Playing Immersive Video in a Portal Window

To play the immersive video in a portal window, set up a window scene in the Shared Space, and then set [`desiredImmersiveViewingMode`](videoplayercomponent/desiredimmersiveviewingmode.md) to [`VideoPlayerComponent.ImmersiveViewingMode.portal`](videoplayercomponent/immersiveviewingmode-swift.enum/portal.md).

If you want to switch the immersive-viewing mode to `portal` while immersive-media playback is in `full` or is in `progressive` mode, wait for the scene event named [`VideoPlayerEvents.ImmersiveViewingModeDidChange`](videoplayerevents/immersiveviewingmodedidchange.md) to trigger after you set [`desiredImmersiveViewingMode`](videoplayercomponent/desiredimmersiveviewingmode.md) to `portal`. Then, dismiss the fully/progressive immersive space and open up a window scene.

##### Updating the Ui During Transitions

The system triggers scene events named [`VideoPlayerEvents.ImmersiveViewingModeWillTransition`](videoplayerevents/immersiveviewingmodewilltransition.md) and [`VideoPlayerEvents.ImmersiveViewingModeDidTransition`](videoplayerevents/immersiveviewingmodedidtransition.md) at the start and end of the immersive-viewing mode transitions, respectively. Apps can listen to these scene events to turn playback controls or other UI items on or off during transitions.

## Topics

### Creating a video player component
- [init(avPlayer: AVPlayer)](videoplayercomponent/init(avplayer:).md)
  Creates a video player component from an AV player object.
- [init(videoRenderer: AVSampleBufferVideoRenderer)](videoplayercomponent/init(videorenderer:).md)
  Creates a video player component from a sample buffer video renderer object.
### Configuring the video player
- [var isPassthroughTintingEnabled: Bool](videoplayercomponent/ispassthroughtintingenabled.md)
  A Boolean value that indicates whether the passthrough camera feed is tinted, emphasizing the video content.
- [var desiredViewingMode: VideoPlaybackController.ViewingMode](videoplayercomponent/desiredviewingmode.md)
  The viewer’s selected content-viewing mode.
### Accessing video player properties
- [var avPlayer: AVPlayer?](videoplayercomponent/avplayer.md)
  The AV player that the component plays.
- [var playerScreenSize: SIMD2<Float>](videoplayercomponent/playerscreensize.md)
  The screen entity size of the current video player in meters.
- [var screenVideoDimension: SIMD2<Float>](videoplayercomponent/screenvideodimension.md)
  The video resolution size.
- [var videoRenderer: AVSampleBufferVideoRenderer?](videoplayercomponent/videorenderer.md)
  The component’s video renderer.
- [var viewingMode: VideoPlaybackController.ViewingMode?](videoplayercomponent/viewingmode.md)
  The current content-viewing mode for video playback.
### Playing immersive media
- [var desiredImmersiveViewingMode: VideoPlayerComponent.ImmersiveViewingMode](videoplayercomponent/desiredimmersiveviewingmode.md)
  The viewer’s selected immersive-viewing mode.
- [var immersiveViewingMode: VideoPlayerComponent.ImmersiveViewingMode?](videoplayercomponent/immersiveviewingmode-swift.property.md)
  The current immersive-viewing mode.
### Instance Properties
- [var currentRenderingStatus: VideoPlayerComponent.RenderingStatus](videoplayercomponent/currentrenderingstatus.md)
- [var desiredSpatialVideoMode: VideoPlayerComponent.SpatialVideoMode](videoplayercomponent/desiredspatialvideomode.md)
  The viewer’s selected spatial video rendering mode.
- [var spatialVideoMode: VideoPlayerComponent.SpatialVideoMode](videoplayercomponent/spatialvideomode-swift.property.md)
  The currently active spatial video rendering mode.
### Enumerations
- [VideoPlayerComponent.ImmersiveViewingMode](videoplayercomponent/immersiveviewingmode-swift.enum.md)
  Options for viewing the video during immersive-media playback.
- [VideoPlayerComponent.RenderingStatus](videoplayercomponent/renderingstatus.md)
- [VideoPlayerComponent.SpatialVideoMode](videoplayercomponent/spatialvideomode-swift.enum.md)
  Spatial Videos’s rendering mode.
- [VideoPlayerComponent.VideoComfortMitigation](videoplayercomponent/videocomfortmitigation.md)

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [VideoPlayerComponent.ImmersiveViewingMode](videoplayercomponent/immersiveviewingmode-swift.enum.md)
  Options for viewing the video during immersive-media playback.
- [struct VideoMaterial](videomaterial.md)
  A material that supports animated textures.
- [class VideoPlaybackController](videoplaybackcontroller.md)
  An object that controls the playback of video for a video material.
- [VideoPlaybackController.ViewingMode](videoplaybackcontroller/viewingmode.md)
  Options for viewing video playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videoplayercomponent)*