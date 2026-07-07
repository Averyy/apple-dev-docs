# AVPlaybackUserInterfaceMediaSelectionControllable

**Framework**: AVKit  
**Kind**: protocol

Provides audio and subtitle selection capabilities for media content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
protocol AVPlaybackUserInterfaceMediaSelectionControllable : AnyObject, Observable
```

## Topics

### Instance Properties
- [var audioDescriptionOptions: [AVPlaybackUserInterfaceMediaSelectionOption]](avplaybackuserinterfacemediaselectioncontrollable-8ee5z/audiodescriptionoptions.md)
  Array of available audio description track options.
- [var audioOptions: [AVPlaybackUserInterfaceMediaSelectionOption]](avplaybackuserinterfacemediaselectioncontrollable-8ee5z/audiooptions.md)
  Array of available audio track options.
- [var currentAudioDescriptionOption: AVPlaybackUserInterfaceMediaSelectionOption?](avplaybackuserinterfacemediaselectioncontrollable-8ee5z/currentaudiodescriptionoption.md)
  The currently selected audio description track.
- [var currentAudioOption: AVPlaybackUserInterfaceMediaSelectionOption?](avplaybackuserinterfacemediaselectioncontrollable-8ee5z/currentaudiooption.md)
  The currently selected audio track.
- [var currentLegibleOption: AVPlaybackUserInterfaceMediaSelectionOption?](avplaybackuserinterfacemediaselectioncontrollable-8ee5z/currentlegibleoption.md)
  The currently selected subtitle or caption track.
- [var legibleOptions: [AVPlaybackUserInterfaceMediaSelectionOption]](avplaybackuserinterfacemediaselectioncontrollable-8ee5z/legibleoptions.md)
  Array of available subtitle and caption track options.

## Relationships

### Inherits From
- [Observable](../Observation/Observable.md)
### Inherited By
- [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-92fri.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-8ee5z)*