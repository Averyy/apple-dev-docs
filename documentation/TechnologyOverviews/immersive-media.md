# Spatial and immersive media

**Framework**: Technology Overviews

Create immersive video experiences in visionOS.

Apple Vision Pro is a revolutionary device for media playback. With ultra-high-resolution displays, advanced spatial audio, and ability to scale content to fit your environment, it’s like having a 3D movie theater with you wherever you go. Create apps to help people capture personal moments in spatial video, provide an extraordinary playback experience, or deliver your next feature film in Apple Immersive Video.

## Capture spatial video

Spatial video is an innovative 3D video format that captures scenes with depth and dimension. People record spatial videos directly on Apple Vision Pro or with the Camera app on supported iPhone models. Watching spatial video on Vision Pro gives the viewer the sense that the action is right in from of them, which makes it a great format for reliving their important moments.

Support spatial video capture in your own custom camera app using [AVFoundation](../AVFoundation/AVFoundation.md). The framework extends the features you use to [build a camera app](../AVFoundation/avcam-building-a-camera-app.md) to enable spatial video capture. Save recorded videos to a person’s Photos library with the [PhotoKit](../PhotoKit/PhotoKit.md) framework. By adopting PhotoKit, you ensure that people can store captured videos in the same place they expect to find all their memories.

## Play immersive media

Apple Vision Pro supports playback of a wide variety of video formats, including 2D, 3D, and fully immersive. Regardless of the type of video you want to play, Apple provides a consistent set of APIs to make it straightforward to build a compelling playback experience in visionOS.

Playing immersive media on Vision Pro builds on the same functionality provided by [AVFoundation](../AVFoundation/AVFoundation.md) that you [play video](./video.md) with on other platforms. This common functionality makes it straightforward to build playback apps that work across platforms, and deliver an immersive experience on Apple Vision Pro. To play spatial and immersive video in a [system player interface](../AVKit/playing-immersive-media-with-avkit.md), adopt [`AVPlayerViewController`](../AVKit/avplayerviewcontroller.md) from the [AVKit](../AVKit/AVKit.md) framework. This API provides the same playback interface found in the TV app and supports features like presenting video in system environments. In visionOS, a player view controller also provides an [`AVExperienceController`](../AVKit/avexperiencecontroller.md) that makes it simple to transition between different presentation styles like multiview or immersive. To build a [custom video player](../visionOS/playing-immersive-media-with-realitykit.md), use [RealityKit](../RealityKit/RealityKit.md) components to present spatial and immersive media. The framework’s [`VideoPlayerComponent`](../RealityKit/videoplayercomponent.md) enables you to present immersive video in your custom playback UI.

Beyond building a dedicated player interface, you can use the [Quick Look](../QuickLook/QuickLook.md) framework to preview video content in your app. The [`PreviewApplication`](../QuickLook/previewapplication.md) interface makes it easy to preview video files without launching a dedicated player.

## Prepare Apple Immersive Video

Apple Immersive Video is a format developed for Apple Vision Pro that’s designed to deliver an ultra-realistic, immersive viewing experience that places viewers at the center of the action. Captured using specialized camera systems like the Blackmagic URSA Cine Immersive, these videos feature 8K resolution per eye, Spatial Audio, and dynamic head tracking that creates a sense of depth that goes beyond traditional 2D or even 3D video. Content in this format is available through the Apple TV app and includes cinematic, sports, and music experiences.

In the latest releases of macOS and visionOS, you can deliver and play your own content in Apple Immersive Video. Adopt the [Immersive Media Support](../ImmersiveMediaSupport/ImmersiveMediaSupport.md) framework to enable reading and writing essential metadata to include with Apple Immersive Video. The framework also adds functionality for previewing Apple Immersive Video frames from another device, like previewing content on Apple Vision Pro from Mac directly without having processed Apple Immersive Video output files.

> **Note**: You can also use the [Apple Immersive Video Utility](https://apps.apple.com/us/app/apple-immersive-video-utility/id6477489398) to import, organize, and package Apple Immersive Video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/immersive-media)*