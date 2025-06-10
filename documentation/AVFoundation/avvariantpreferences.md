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

### Preference Settings
- [static var scalabilityToLosslessAudio: AVVariantPreferences](avvariantpreferences/scalabilitytolosslessaudio.md)
  A preference that indicates the player item supports variant playlists that contain losslessly encoded audio when sufficient bandwidth is available.
### Initializers
- [init(rawValue: UInt)](avvariantpreferences/init(rawvalue:).md)
  Creates a variant preferences structure with an integer value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var variantPreferences: AVVariantPreferences](avplayeritem/variantpreferences.md)
  The preferences the player item uses when selecting variant playlists.
- [var startsOnFirstEligibleVariant: Bool](avplayeritem/startsonfirsteligiblevariant.md)
  A Boolean value that indicates whether playback starts with the first eligible variant that appears in the stream’s main playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvariantpreferences)*