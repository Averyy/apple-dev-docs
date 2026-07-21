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
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AVPlaybackUserInterfaceMediaSelectionControllable](avplaybackuserinterfacemediaselectioncontrollable-8ee5z.md)
  Provides audio and subtitle selection capabilities for media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectionoption)*