# AVInterfaceMediaSelectionControllable

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
protocol AVInterfaceMediaSelectionControllable : Observable
```

## Topics

### Inspecting media selection options
- [var audioOptions: [AVInterfaceMediaSelectionOptionSource]](avinterfacemediaselectioncontrollable-6wn31/audiooptions.md)
  Array of available audio track options for selection.
- [var currentAudioOption: AVInterfaceMediaSelectionOptionSource?](avinterfacemediaselectioncontrollable-6wn31/currentaudiooption.md)
  Currently selected audio track for playback.
- [var legibleOptions: [AVInterfaceMediaSelectionOptionSource]](avinterfacemediaselectioncontrollable-6wn31/legibleoptions.md)
  Array of available subtitle and caption track options.
- [var currentLegibleOption: AVInterfaceMediaSelectionOptionSource?](avinterfacemediaselectioncontrollable-6wn31/currentlegibleoption.md)
  Currently selected subtitle or caption track.

## Relationships

### Inherits From
- [Observable](../Observation/Observable.md)
### Inherited By
- [AVInterfaceControllable](avinterfacecontrollable-3xs3i.md)

## See Also

- [class AVInterfaceMediaSelectionOptionSource](avinterfacemediaselectionoptionsource.md)
  Represents a media selection option for audio tracks or subtitle tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemediaselectioncontrollable-6wn31)*