# AVPlaybackUserInterfaceControllable

**Framework**: AVKit  
**Kind**: protocol

A comprehensive protocol that provides complete media control and information for playback, timeline navigation, audio/subtitle selection, volume control, and metadata access.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
protocol AVPlaybackUserInterfaceControllable : AVPlaybackUserInterfaceMediaSelectionControllable, AVPlaybackUserInterfaceMetadataProviding, AVPlaybackUserInterfacePlaybackControllable, AVPlaybackUserInterfaceTimeControllable, AVPlaybackUserInterfaceVolumeControllable
```

#### Overview

This protocol consolidates all media source capabilities into a single interface, enabling rich media experiences with full control over playback state, timeline interactions, and content metadata.

## Relationships

### Inherits From
- [AVPlaybackUserInterfaceMediaSelectionControllable](avplaybackuserinterfacemediaselectioncontrollable-8ee5z.md)
- [AVPlaybackUserInterfaceMetadataProviding](avplaybackuserinterfacemetadataproviding-814y4.md)
- [AVPlaybackUserInterfacePlaybackControllable](avplaybackuserinterfaceplaybackcontrollable-9he54.md)
- [AVPlaybackUserInterfaceTimeControllable](avplaybackuserinterfacetimecontrollable-50vcy.md)
- [AVPlaybackUserInterfaceVolumeControllable](avplaybackuserinterfacevolumecontrollable-4vgi1.md)
- [Observable](../observation/observable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontrollable-92fri)*