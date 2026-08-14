# AVPlaybackUserInterfaceMediaSelectionOption

**Framework**: AVKit  
**Kind**: class

Represents a media selection option for audio tracks or subtitle tracks.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class AVPlaybackUserInterfaceMediaSelectionOption
```

#### Overview

This class represents individual media options (such as audio tracks or subtitle tracks) that can be selected by the user in media playback interfaces. Each option provides display information and metadata for user selection.

## Topics

### Initializers
- [init?(coder: NSCoder)](avplaybackuserinterfacemediaselectionoption/init(coder:).md)
- [convenience init(displayName: String, identifier: String, language: Locale.Language?, mediaCharacteristics: [AVMediaCharacteristic])](avplaybackuserinterfacemediaselectionoption/init(displayname:identifier:language:mediacharacteristics:).md)
  Creates a new media selection option.
### Instance Properties
- [var displayName: String](avplaybackuserinterfacemediaselectionoption/displayname.md)
  Human-readable name for this media option displayed in user interfaces (e.g., “English”, “Spanish (Latin America)”, “Director’s Commentary”).
- [var identifier: String](avplaybackuserinterfacemediaselectionoption/identifier.md)
  Unique system identifier for this media option, used for programmatic selection and persistence across sessions.
- [var language: Locale.Language?](avplaybackuserinterfacemediaselectionoption/language.md)
  The language of this media selection option.
- [var mediaCharacteristics: [AVMediaCharacteristic]](avplaybackuserinterfacemediaselectionoption/mediacharacteristics.md)
  The media characteristics describing accessibility features and content properties of this option. Common values include `AVMediaCharacteristicContainsOnlyForcedSubtitles`, `AVMediaCharacteristicTranscribesSpokenDialogForAccessibility`, and `AVMediaCharacteristicDescribesMusicAndSoundForAccessibility`. May be empty if no characteristics apply.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol AVPlaybackUserInterfaceMediaSelectionControllable](avplaybackuserinterfacemediaselectioncontrollable-8ee5z.md)
  Provides audio and subtitle selection capabilities for media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectionoption)*