# AVVariantPreferences

**Framework**: AVFoundation  
**Kind**: struct

Defines the preferences the player item uses when selecting variant playlists.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.4+

## Declaration

```swift
struct AVVariantPreferences
```

## Topics

### Preference settings
- [static var scalabilityToLosslessAudio: AVVariantPreferences](avvariantpreferences/scalabilitytolosslessaudio.md)
  A preference that indicates the player item supports variant playlists that contain losslessly encoded audio when sufficient bandwidth is available.
### Initializers
- [init(rawValue: UInt)](avvariantpreferences/init(rawvalue:).md)
  Creates a variant preferences structure with an integer value.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [var variantPreferences: AVVariantPreferences](avplayeritem/variantpreferences.md)
  The preferences the player item uses when selecting variant playlists.
- [var startsOnFirstEligibleVariant: Bool](avplayeritem/startsonfirsteligiblevariant.md)
  A Boolean value that indicates whether playback starts with the first eligible variant that appears in the stream’s main playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvariantpreferences)*