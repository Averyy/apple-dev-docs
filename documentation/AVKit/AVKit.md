# AVKit

**Framework**: AVKit  
**Kind**: module

Create user interfaces for media playback, complete with transport controls, chapter navigation, picture-in-picture support, and display of subtitles and closed captions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 9.0+

## Mentions

- [Adopting Picture in Picture for video calls](adopting-picture-in-picture-for-video-calls.md)

## Topics

### iOS playback and capture
- [Playing video content in a standard user interface](playing-video-content-in-a-standard-user-interface.md)
  Play media full screen, embedded inline, or in a floating Picture in Picture (PiP) window using a player view controller.
- [class AVPlayerViewController](avplayerviewcontroller.md)
  A view controller that displays content from a player and presents a native user interface to control playback.
- [protocol AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to player view controller events.
- [class AVCaptureEventInteraction](avcaptureeventinteraction.md)
  An object that registers handlers to respond to capture events from system hardware buttons.
- [class AVCaptureEvent](avcaptureevent.md)
  An object that describes a user interaction with a system hardware button.
- [class AVCaptureEventSound](avcaptureeventsound.md)
  A sound object for a capture event.
- [class AVInputPickerInteraction](avinputpickerinteraction.md)
  Use `AVInputPickerInteraction` to present an input picker.
### tvOS playback and capture
- [Customizing the tvOS Playback Experience](customizing-the-tvos-playback-experience.md)
  Adopt the latest features of the redesigned tvOS player user interface to provide a more streamlined way to watch your content.
- [Presenting Navigation Markers](presenting-navigation-markers.md)
  Present navigation markers in the Chapters panel to help users quickly navigate your content.
- [Working with Interstitial Content](working-with-interstitial-content.md)
  Present additional content alongside your main media presentation using HTTP Live Streaming support.
- [Presenting Content Proposals in tvOS](presenting-content-proposals-in-tvos.md)
  Display a preview of an upcoming media item at the conclusion of the currently playing media item.
- [Working with Overlays and Parental Controls in tvOS](working-with-overlays-and-parental-controls-in-tvos.md)
  Add interactive overlays, parental controls, and livestream channel flipping using a player view controller.
- [Supporting Continuity Camera in your tvOS app](supporting-continuity-camera-in-your-tvos-app.md)
  Capture high-quality photos, video, and audio in your Apple TV app by connecting an iPhone or iPad as a continuity device.
- [class AVPlayerViewController](avplayerviewcontroller.md)
  A view controller that displays content from a player and presents a native user interface to control playback.
- [protocol AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to player view controller events.
- [class AVInterstitialTimeRange](avinterstitialtimerange.md)
  A time range in an audiovisual presentation for content with an interstitial designation, such as advertisements or legal notices.
- [class AVNavigationMarkersGroup](avnavigationmarkersgroup.md)
  A set of markers for navigating playback of an audiovisual presentation.
- [class AVContentProposalViewController](avcontentproposalviewcontroller.md)
  A view controller that proposes content to watch next.
- [class AVDisplayManager](avdisplaymanager.md)
  A tvOS management object that controls whether a TV switches modes to match the video’s native mode.
- [class AVContinuityDevicePickerViewController](avcontinuitydevicepickerviewcontroller.md)
  A view controller that provides an interface to a person so they can select and connect a continuity device to the system.
- [protocol AVContinuityDevicePickerViewControllerDelegate](avcontinuitydevicepickerviewcontrollerdelegate.md)
  An interface that responds to events from a continuity device picker view controller.
### visionOS playback
- [Playing immersive media with AVKit](playing-immersive-media-with-avkit.md)
  Adopt the system playback interface to provide an immersive video watching experience.
- [Creating a multiview video playback experience in visionOS](creating-a-multiview-video-playback-experience-in-visionos.md)
  Build an interface that plays multiple videos simultaneously and handles transitions to different experience types gracefully.
- [Adopting the system player interface in visionOS](adopting-the-system-player-interface-in-visionos.md)
  Provide an optimized viewing experience for watching 3D video content.
- [Trimming and exporting media in visionOS](trimming-and-exporting-media-in-visionos.md)
  Display standard controls in your app to edit the timeline of the currently playing media.
- [class AVPlayerViewController](avplayerviewcontroller.md)
  A view controller that displays content from a player and presents a native user interface to control playback.
- [protocol AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to player view controller events.
- [class AVExperienceController](avexperiencecontroller.md)
  An object that controls video experiences.
- [class AVMultiviewManager](avmultiviewmanager.md)
  An object that manages viewing multiple videos at once.
- [class AVGroupExperienceCoordinator](avgroupexperiencecoordinator.md)
  An object that synchronizes viewing environment state across participants in a SharePlay session.
### macOS playback and capture
- [Implementing Trimming in a macOS Player](implementing-trimming-in-a-macos-player.md)
  Provide a QuickTime media-trimming experience in your macOS app.
- [class AVPlayerView](avplayerview.md)
  A view that displays content from a player and presents a native user interface to control playback.
- [class AVCaptureView](avcaptureview.md)
  A view that displays standard user interface controls for capturing media data.
### Multiplatform playback and capture
- [struct VideoPlayer](videoplayer.md)
  A view that displays content from a player and a native user interface to control playback.
### Picture in Picture
- [Adopting Picture in Picture Playback in tvOS](adopting-picture-in-picture-playback-in-tvos.md)
  Add advanced multitasking capabilities to your video apps by using Picture in Picture playback in tvOS.
- [Adopting Picture in Picture in a Standard Player](adopting-picture-in-picture-in-a-standard-player.md)
  Add Picture in Picture (PiP) playback to your app using a player view controller.
- [Adopting Picture in Picture in a Custom Player](adopting-picture-in-picture-in-a-custom-player.md)
  Add controls to your custom player user interface to invoke Picture in Picture (PiP) playback.
- [Adopting Picture in Picture for video calls](adopting-picture-in-picture-for-video-calls.md)
  Add multitasking capability to your video-call apps by using Picture in Picture (PiP).
- [Accessing the camera while multitasking on iPad](accessing-the-camera-while-multitasking-on-ipad.md)
  Operate the camera in Split View, Slide Over, Picture in Picture, and Stage Manager modes.
- [class AVPictureInPictureController](avpictureinpicturecontroller.md)
  A controller that responds to user-initiated Picture in Picture playback of video in a floating, resizable window.
### Playback route selection
- [class AVRoutePickerView](avroutepickerview.md)
  A view that presents a list of nearby media receivers.
### Metadata
- [AVKit Metadata Identifiers](avkit-metadata-identifiers.md)
  Additional metadata that an asset contains.
### Errors
- [let AVKitErrorDomain: String](avkiterrordomain.md)
  The domain of errors the framework generates.
- [struct AVKitError](avkiterror-swift.struct.md)
  A structure that represents a framework error.
- [AVKitError.Code](avkiterror-swift.struct/code.md)
  Constants that identify framework error codes.
### Macros
- [Macros](avkit-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AVKit)*