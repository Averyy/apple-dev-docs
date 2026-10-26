# AVPlaybackUserInterfaceMediaSelectionControllable

**Framework**: AVKit  
**Kind**: protocol  
**Role**: Protocol

Provides audio and subtitle selection capabilities for media content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@protocol AVPlaybackUserInterfaceMediaSelectionControllable <NSObject>
```

## Topics

### Instance Properties
- [audioDescriptionOptions](./avplaybackuserinterfacemediaselectioncontrollable-2fftn/audiodescriptionoptions.md)
  Array of available audio description track options. Audio description tracks provide narrated descriptions of visual content for visually impaired viewers. Audio description options are distinct from those in `audioOptions` — they provide a narration layer played alongside the primary audio rather than replacing it. Options are ordered by preference with the primary language or default audio description track typically appearing first. May be empty for content without audio description tracks. Must be key-value observable.
- [audioOptions](./avplaybackuserinterfacemediaselectioncontrollable-2fftn/audiooptions.md)
  Array of available audio track options. This includes all audio streams provided by the media source such as different languages, director’s commentary, and alternative audio mixes. Options are ordered by preference with the primary language or default audio track typically appearing first. May be empty for content without selectable audio options. Must be key-value observable.
- [currentAudioDescriptionOption](./avplaybackuserinterfacemediaselectioncontrollable-2fftn/currentaudiodescriptionoption.md)
  The currently selected audio description track. Should be one of the options in `audioDescriptionOptions`. Must be key-value observable.
- [currentAudioOption](./avplaybackuserinterfacemediaselectioncontrollable-2fftn/currentaudiooption.md)
  The currently selected audio track. Should be one of the options in `audioOptions`. Must be key-value observable.
- [currentLegibleOption](./avplaybackuserinterfacemediaselectioncontrollable-2fftn/currentlegibleoption.md)
  The currently selected subtitle or caption track. Should be one of the options in `legibleOptions`. Must be key-value observable.
- [legibleOptions](./avplaybackuserinterfacemediaselectioncontrollable-2fftn/legibleoptions.md)
  Array of available subtitle and caption track options. This includes text overlays in different languages, closed captions for accessibility, forced narrative subtitles, and sign language interpretation tracks. May be empty for content without text tracks. Must be key-value observable.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [AVPlaybackUserInterfaceControllable](./avplaybackuserinterfacecontrollable-7ti30.md)

## See Also

### Media selection
- [class AVPlaybackUserInterfaceMediaSelectionOption](./avplaybackuserinterfacemediaselectionoption.md)
  Represents a media selection option for audio tracks or subtitle tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-2fftn)*