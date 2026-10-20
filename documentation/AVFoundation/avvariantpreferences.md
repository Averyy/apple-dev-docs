# AVVariantPreferences

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum AVVariantPreferences : NSUInteger;
```

## Topics

### Preference settings
- [static var scalabilityToLosslessAudio: AVVariantPreferences](./avvariantpreferences/scalabilitytolosslessaudio.md)
  A preference that indicates the player item supports variant playlists that contain losslessly encoded audio when sufficient bandwidth is available.
### Initializers
- [init(rawValue: UInt)](./avvariantpreferences/init%28rawvalue%29.md)
  Creates a variant preferences structure with an integer value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Setting variant behavior
- [var variantPreferences: AVVariantPreferences](./avplayeritem/variantpreferences.md)
  The preferences the player item uses when selecting variant playlists.
- [var startsOnFirstEligibleVariant: Bool](./avplayeritem/startsonfirsteligiblevariant.md)
  A Boolean value that indicates whether playback starts with the first eligible variant that appears in the stream’s main playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvariantpreferences)*