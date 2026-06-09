# Third-party casting support

**Framework**: AVKit

Provide custom playback controls for third-party casting services and other media sources.

#### Overview

Use the [`AVInterfaceControllable`](avinterfacecontrollable-3xs3i.md) protocol suite to build custom transport controls that work with third-party casting services. The [`AVInterfaceControllable`](avinterfacecontrollable-3xs3i.md) composite protocol combines playback, time, media selection, volume, and metadata capabilities into a single interface.

## Topics

### Playback
- [protocol AVInterfacePlaybackControllable](avinterfaceplaybackcontrollable-44aba.md)
  Provides playback control and state management for media content.
- [enum AVInterfacePlaybackState](avinterfaceplaybackstate.md)
  Describes possible playback states of the interface source.
- [struct AVInterfaceSeekCapabilities](avinterfaceseekcapabilities.md)
  Describes navigation capabilities of the media source.
### Timeline
- [protocol AVInterfaceTimeControllable](avinterfacetimecontrollable-63tkp.md)
  Provides time control and navigation capabilities for media content.
- [class AVInterfaceTimelineSegment](avinterfacetimelinesegment.md)
  Represents a contiguous segment of timeline content with specific playback characteristics.
### Media selection
- [protocol AVInterfaceMediaSelectionControllable](avinterfacemediaselectioncontrollable-6wn31.md)
  Provides audio and subtitle selection capabilities for media content.
- [class AVInterfaceMediaSelectionOptionSource](avinterfacemediaselectionoptionsource.md)
  Represents a media selection option for audio tracks or subtitle tracks.
### Volume
- [protocol AVInterfaceVolumeControllable](avinterfacevolumecontrollable-5sjm1.md)
  Provides volume and audio muting control for media content.
### Metadata
- [protocol AVInterfaceMetadataProviding](avinterfacemetadataproviding-666nk.md)
  Provides metadata information about media content including title, artwork, and content type.
- [struct AVInterfaceMetadata](avinterfacemetadata-swift.struct.md)
  A Swift-friendly structure representing media metadata.
- [class AVInterfaceAlbumArtwork](avinterfacealbumartwork.md)
  Base class representing album artwork or cover art for media content.
### Complete interface
- [protocol AVInterfaceControllable](avinterfacecontrollable-3xs3i.md)
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