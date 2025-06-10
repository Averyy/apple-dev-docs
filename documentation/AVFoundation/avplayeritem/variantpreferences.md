# variantPreferences

**Framework**: AVFoundation  
**Kind**: property

The preferences the player item uses when selecting variant playlists.

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
nonisolated
var variantPreferences: AVVariantPreferences { get set }
```

#### Discussion

The default value is [`AVVariantPreferenceNone`](avvariantpreferences/avvariantpreferencenone.md).

> **Note**:  Changing variant preferences during playback might result in a variant switch.

## See Also

- [struct AVVariantPreferences](avvariantpreferences.md)
  Defines the preferences the player item uses when selecting variant playlists.
- [var startsOnFirstEligibleVariant: Bool](avplayeritem/startsonfirsteligiblevariant.md)
  A Boolean value that indicates whether playback starts with the first eligible variant that appears in the stream’s main playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/variantpreferences)*