# Playback interfaces

**Framework**: AVKit

Present video with the system player, complete with transport controls and Picture in Picture.

#### Overview

AVKit provides the best way to build a playback interface for your app. The player it presents is the one people use in the apps that come with their devices, so its controls need no explanation. It also connects to the system features that surround playback, from Now Playing to Picture in Picture and AirPlay. Your work goes into your content instead of into controls.

The same player provides the right playback experience on supported Apple platforms. Video expands to full screen on iPad and iPhone, and keeps playing in a corner when someone switches apps. The transport bar answers the remote on Apple TV, where the player can also offer what to watch next. On Mac, it sits in a window with trimming. On Apple Vision Pro it grows from inline video to a large screen or a fully immersive scene. As the system player gains new behavior, your app picks it up.

For information about managing playback itself, see [`Media playback`](https://developer.apple.com/documentation/avfoundation/media-playback).

## Topics

### Standard player interfaces
- [Playing video content in a standard user interface](playing-video-content-in-a-standard-user-interface.md)
  Play media full screen, embedded inline, or in a floating Picture in Picture (PiP) window using a player view controller.
- [Customizing the tvOS playback experience](customizing-the-tvos-playback-experience.md)
  Adopt the latest features of the redesigned tvOS player user interface to provide a more streamlined way to watch your content.
- [Adopting the system player interface in visionOS](adopting-the-system-player-interface-in-visionos.md)
  Provide an optimized viewing experience for watching 3D video content.
- [class AVPlayerViewController](avplayerviewcontroller.md)
  A view controller that displays content from a player and presents a native user interface to control playback.
- [protocol AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to player view controller events.
- [class AVPlayerView](avplayerview.md)
  A view that displays content from a player and presents a native user interface to control playback.
- [protocol AVPlayerViewDelegate](avplayerviewdelegate.md)
  A protocol that defines the methods to implement to participate in the player view’s full-screen presentation life cycle.
- [struct VideoPlayer](videoplayer.md)
  A view that displays content from a player and a native user interface to control playback.
### Immersive and multiview media
- [Playing immersive media with AVKit](playing-immersive-media-with-avkit.md)
  Adopt the system playback interface to provide an immersive video watching experience.
- [Creating a multiview video playback experience in visionOS](creating-a-multiview-video-playback-experience-in-visionos.md)
  Build an interface that plays multiple videos simultaneously and handles transitions to different experience types gracefully.
- [class AVExperienceController](avexperiencecontroller.md)
  An object that controls video experiences.
- [class AVMultiviewManager](avmultiviewmanager.md)
  An object that manages viewing multiple videos at once.
- [class AVGroupExperienceCoordinator](avgroupexperiencecoordinator.md)
  An object that synchronizes viewing environment state across participants in a SharePlay session.
- [class AVViewport](avviewport.md)
  An object that provides configuration options for how the player displays content in different viewing contexts.
- [class AVPortalViewport](avportalviewport.md)
  An object that defines the visual parameters for content displayed within a portal frame.
### Interstitials and markers
- [Working with interstitial content](working-with-interstitial-content.md)
  Present additional content alongside your main media presentation using HTTP Live Streaming support.
- [Presenting navigation markers](presenting-navigation-markers.md)
  Present navigation markers in the Chapters panel to help users quickly navigate your content.
- [class AVInterstitialTimeRange](avinterstitialtimerange.md)
  A time range in an audiovisual presentation for content with an interstitial designation, such as advertisements or legal notices.
- [class AVNavigationMarkersGroup](avnavigationmarkersgroup.md)
  A set of markers for navigating playback of an audiovisual presentation.
### Content proposals and parental controls
- [Presenting content proposals in tvOS](presenting-content-proposals-in-tvos.md)
  Display a preview of an upcoming media item at the conclusion of the currently playing media item.
- [Working with overlays and parental controls in tvOS](working-with-overlays-and-parental-controls-in-tvos.md)
  Add interactive overlays, parental controls, and livestream channel flipping using a player view controller.
- [class AVContentProposal](avcontentproposal.md)
  An object that describes the content to propose playing after the current item finishes.
- [enum AVContentProposalAction](avcontentproposalaction.md)
  Constant that indicate the action a user takes when dismissing a content proposal.
- [class AVContentProposalViewController](avcontentproposalviewcontroller.md)
  A view controller that proposes content to watch next.
### Media trimming and export
- [Implementing trimming in a macOS player](implementing-trimming-in-a-macos-player.md)
  Provide a QuickTime media-trimming experience in your macOS app.
- [Trimming and exporting media in visionOS](trimming-and-exporting-media-in-visionos.md)
  Display standard controls in your app to edit the timeline of the currently playing media.
- [enum AVPlayerViewTrimResult](avplayerviewtrimresult.md)
  Constants that specify an action a user takes when trimming media in a player view.
### Display management
- [class AVDisplayManager](avdisplaymanager.md)
  A tvOS management object that controls whether a TV switches modes to match the video’s native mode.
- [enum AVDisplayDynamicRange](avdisplaydynamicrange.md)
  Describes how High Dynamic Range (HDR) video content renders.
### Picture in Picture
- [Adopting Picture in Picture in a standard player](adopting-picture-in-picture-in-a-standard-player.md)
  Add Picture in Picture (PiP) playback to your app using a player view controller.
- [Adopting Picture in Picture in a custom player](adopting-picture-in-picture-in-a-custom-player.md)
  Add controls to your custom player user interface to invoke Picture in Picture (PiP) playback.
- [Adopting Picture in Picture for video calls](adopting-picture-in-picture-for-video-calls.md)
  Add multitasking capability to your video-call apps by using Picture in Picture (PiP).
- [Adopting Picture in Picture playback in tvOS](adopting-picture-in-picture-playback-in-tvos.md)
  Add advanced multitasking capabilities to your video apps by using Picture in Picture playback in tvOS.
- [class AVPictureInPictureController](avpictureinpicturecontroller.md)
  A controller that responds to user-initiated Picture in Picture playback of video in a floating, resizable window.
- [protocol AVPictureInPictureControllerDelegate](avpictureinpicturecontrollerdelegate.md)
  A protocol to adopt to respond to Picture in Picture events.
- [protocol AVPictureInPictureSampleBufferPlaybackDelegate](avpictureinpicturesamplebufferplaybackdelegate.md)
  A protocol for controlling playback from a sample buffer display layer in Picture in Picture.
- [class AVPictureInPictureVideoCallViewController](avpictureinpicturevideocallviewcontroller.md)
  A view controller that presents content from a video call in Picture in Picture.
- [protocol AVPlayerViewPictureInPictureDelegate](avplayerviewpictureinpicturedelegate.md)
  A protocol that defines the methods to implement to respond to Picture in Picture playback events.
### Media and content selection
- [class AVLegibleMediaOptionsMenuController](avlegiblemediaoptionsmenucontroller.md)
- [struct AVLegibleMediaOptionsMenuState](avlegiblemediaoptionsmenustate.md)
- [class AVContentSelectionViewController](avcontentselectionviewcontroller.md)
  A view controller for providing additional UI to the multiview experience.
### Route selection
- [class AVRoutePickerView](avroutepickerview.md)
  A view that presents a list of nearby media receivers.
- [protocol AVRoutePickerViewDelegate](avroutepickerviewdelegate.md)
  A protocol that defines the methods to adopt to respond to route picker view presentation events.
- [enum AVRoutePickerViewButtonStyle](avroutepickerviewbuttonstyle.md)
  Constants that define the button styles a route picker view supports.
### Third-party casting
- [Third-party casting support](third-party-casting-support.md)
  Provide custom playback controls for third-party casting services and other media sources.
### Metadata identifiers
- [AVKit metadata identifiers](avkit-metadata-identifiers.md)
  Additional metadata that an asset contains.

## See Also

- [Capture interfaces](avkit-capture-interfaces.md)
  Capture from hardware buttons and AirPods, present an audio input picker, and connect a nearby iPhone as a camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avkit-playback-interfaces)*