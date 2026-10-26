# AVVariantPreferenceNone

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Enumeration Case

Indicates that the player item uses the default behavior for determining variant playlist selection.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.4+

## Declaration

```c
AVVariantPreferenceNone
```

#### Discussion

By default, a player item bases variant selection on the available bandwidth, compatibility of the indicated codec or codecs, dimensions of the visual output, and number of available audio output channels.

## See Also

### Preference settings
- [static var scalabilityToLosslessAudio: AVVariantPreferences](./scalabilitytolosslessaudio.md)
  A preference that indicates the player item supports variant playlists that contain losslessly encoded audio when sufficient bandwidth is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvariantpreferences/avvariantpreferencenone)*