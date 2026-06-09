# AVInterfaceControllable

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
protocol AVInterfaceControllable : AVInterfaceMediaSelectionControllable, AVInterfaceMetadataProviding, AVInterfacePlaybackControllable, AVInterfaceTimeControllable, AVInterfaceVolumeControllable
```

#### Overview

This protocol consolidates all media source capabilities into a single interface, enabling rich media experiences with full control over playback state, timeline interactions, and content metadata.

## Relationships

### Inherits From
- [AVInterfaceMediaSelectionControllable](avinterfacemediaselectioncontrollable-6wn31.md)
- [AVInterfaceMetadataProviding](avinterfacemetadataproviding-666nk.md)
- [AVInterfacePlaybackControllable](avinterfaceplaybackcontrollable-44aba.md)
- [AVInterfaceTimeControllable](avinterfacetimecontrollable-63tkp.md)
- [AVInterfaceVolumeControllable](avinterfacevolumecontrollable-5sjm1.md)
- [Observable](../Observation/Observable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacecontrollable-3xs3i)*