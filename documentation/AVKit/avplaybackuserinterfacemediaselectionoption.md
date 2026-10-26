# AVPlaybackUserInterfaceMediaSelectionOption

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

Represents a media selection option for audio tracks or subtitle tracks.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class AVPlaybackUserInterfaceMediaSelectionOption
```

```objc
@interface AVPlaybackUserInterfaceMediaSelectionOption : NSObject
```

#### Overview

This class represents individual media options (such as audio tracks or subtitle tracks) that can be selected by the user in media playback interfaces. Each option provides display information and metadata for user selection.

## Topics

### Initializers
- [init?(coder: NSCoder)](./avplaybackuserinterfacemediaselectionoption/init%28coder%29.md)
- [convenience init(displayName: String, identifier: String, language: Locale.Language?, mediaCharacteristics: [AVMediaCharacteristic])](./avplaybackuserinterfacemediaselectionoption/init%28displayname,identifier,language,mediacharacteristics%29.md)
  Creates a new media selection option.
### Instance Properties
- [var displayName: String](./avplaybackuserinterfacemediaselectionoption/displayname.md)
  Human-readable name for this media option displayed in user interfaces (e.g., “English”, “Spanish (Latin America)”, “Director’s Commentary”).
- [var identifier: String](./avplaybackuserinterfacemediaselectionoption/identifier.md)
  Unique system identifier for this media option, used for programmatic selection and persistence across sessions.
- [var language: Locale.Language?](./avplaybackuserinterfacemediaselectionoption/language.md)
  The language of this media selection option.
- [var mediaCharacteristics: [AVMediaCharacteristic]](./avplaybackuserinterfacemediaselectionoption/mediacharacteristics.md)
  The media characteristics describing accessibility features and content properties of this option. Common values include `AVMediaCharacteristicContainsOnlyForcedSubtitles`, `AVMediaCharacteristicTranscribesSpokenDialogForAccessibility`, and `AVMediaCharacteristicDescribesMusicAndSoundForAccessibility`. May be empty if no characteristics apply.
- [extendedLanguageTag](./avplaybackuserinterfacemediaselectionoption/extendedlanguagetag.md)
  IETF BCP 47 language identifier (e.g., “en-US”, “es-419”, “zh-Hans-CN”) indicating the primary language and locale of this option. This standardized tag provides detailed language information including region, script, and variants. May be empty for language-neutral content such as music-only audio tracks, sound effects, or visual-only subtitles without spoken content.
### Instance Methods
- [- initWithDisplayName:identifier:extendedLanguageTag:mediaCharacteristics:](./avplaybackuserinterfacemediaselectionoption/initwithdisplayname_identifier_extendedlanguagetag_mediacharacteristics_.md)
  Initializes a new media selection option with the specified attributes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Media selection
- [protocol AVPlaybackUserInterfaceMediaSelectionControllable](./avplaybackuserinterfacemediaselectioncontrollable-8ee5z.md)
  Provides audio and subtitle selection capabilities for media content.
- [AVPlaybackUserInterfaceMediaSelectionControllable](./avplaybackuserinterfacemediaselectioncontrollable-2fftn.md)
  Provides audio and subtitle selection capabilities for media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectionoption)*