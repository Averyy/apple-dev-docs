# Third-party casting support

**Framework**: AVKit

Provide custom playback controls for third-party casting services and other media sources.

#### Overview

Use the [`AVPlaybackUserInterfaceControllable`](avplaybackuserinterfacecontrollable-92fri.md) protocol suite to build custom transport controls that work with third-party casting services. The [`AVPlaybackUserInterfaceControllable`](avplaybackuserinterfacecontrollable-92fri.md) composite protocol combines playback, timeline, media selection, volume, and metadata capabilities into a single interface.

## Topics

### Playback
- [protocol AVPlaybackUserInterfacePlaybackControllable](avplaybackuserinterfaceplaybackcontrollable-9he54.md)
  Provides playback control and state management for media content.
- [enum AVPlaybackUserInterfacePlaybackState](avplaybackuserinterfaceplaybackstate.md)
  Describes possible transport states of the playback source.
- [struct AVPlaybackUserInterfaceSeekCapabilities](avplaybackuserinterfaceseekcapabilities.md)
  Describes navigation capabilities of the media source.
### Timeline
- [protocol AVPlaybackUserInterfaceTimeControllable](avplaybackuserinterfacetimecontrollable-50vcy.md)
  Provides time control and navigation capabilities for media content.
- [class AVPlaybackUserInterfacePlaybackPosition](avplaybackuserinterfaceplaybackposition.md)
  A snapshot comprising a playback position recorded at a known host time and the rate of position advancement.
- [class AVPlaybackUserInterfaceTimelineSegment](avplaybackuserinterfacetimelinesegment.md)
  Represents a contiguous segment of timeline content with specific playback characteristics.
- [enum AVPlaybackUserInterfaceTimelineSegmentType](avplaybackuserinterfacetimelinesegmenttype.md)
  Describes the type of content within a timeline segment.
### Media selection
- [protocol AVPlaybackUserInterfaceMediaSelectionControllable](avplaybackuserinterfacemediaselectioncontrollable-8ee5z.md)
  Provides audio and subtitle selection capabilities for media content.
- [class AVPlaybackUserInterfaceMediaSelectionOption](avplaybackuserinterfacemediaselectionoption.md)
  Represents a media selection option for audio tracks or subtitle tracks.
### Volume
- [protocol AVPlaybackUserInterfaceVolumeControllable](avplaybackuserinterfacevolumecontrollable-4vgi1.md)
  Provides volume and audio muting control for media content.
### Metadata
- [protocol AVPlaybackUserInterfaceMetadataProviding](avplaybackuserinterfacemetadataproviding-814y4.md)
  Provides metadata information about media content including title, artwork, and content type.
- [struct AVPlaybackUserInterfaceContentMetadata](avplaybackuserinterfacecontentmetadata-swift.struct.md)
  A Swift-friendly structure representing media metadata.
- [class AVPlaybackUserInterfaceContentArtwork](avplaybackuserinterfacecontentartwork.md)
  Base class representing artwork or cover art for media content.
- [class AVPlaybackUserInterfaceContentURLArtwork](avplaybackuserinterfacecontenturlartwork.md)
  An artwork subclass that references artwork via a URL and content type.
### Complete interface
- [protocol AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-92fri.md)
  A comprehensive protocol that provides complete media control and information for playback, timeline navigation, audio/subtitle selection, volume control, and metadata access.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/third-party-casting-support)*