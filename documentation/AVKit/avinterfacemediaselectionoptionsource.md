# AVInterfaceMediaSelectionOptionSource

**Framework**: AVKit  
**Kind**: class

Represents a media selection option for audio tracks or subtitle tracks.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class AVInterfaceMediaSelectionOptionSource
```

#### Overview

This class represents individual media options (such as audio tracks or subtitle tracks) that can be selected by the user in media playback interfaces. Each option provides display information and metadata for user selection.

## Topics

### Creating an option source
- [convenience init(displayName: String, identifier: String, extendedLanguageTag: String?)](avinterfacemediaselectionoptionsource/init(displayname:identifier:extendedlanguagetag:).md)
  Creates a new media selection option.
- [convenience init(displayName: String, identifier: String, language: Locale.Language?)](avinterfacemediaselectionoptionsource/init(displayname:identifier:language:).md)
  Creates a new media selection option.
### Inspecting the option source
- [var displayName: String](avinterfacemediaselectionoptionsource/displayname.md)
  Human-readable name for this media option displayed in user interfaces (e.g., “English”, “Spanish (Latin America)”, “Director’s Commentary”).
- [var identifier: String](avinterfacemediaselectionoptionsource/identifier.md)
  Unique system identifier for this media option, used for programmatic selection and persistence across sessions.
- [var language: Locale.Language?](avinterfacemediaselectionoptionsource/language.md)
  The language of this media selection option.
### Initializers
- [init?(coder: NSCoder)](avinterfacemediaselectionoptionsource/init(coder:).md)
- [convenience init(displayName: String, identifier: String, extendedLanguageTagTemp: Locale.Language?)](avinterfacemediaselectionoptionsource/init(displayname:identifier:extendedlanguagetagtemp:).md)
  Creates a new media selection option.
### Instance Properties
- [var extendedLanguageTagTemp: Locale.Language?](avinterfacemediaselectionoptionsource/extendedlanguagetagtemp.md)
  IETF BCP 47 language identifier represented as a `Locale.Language`.

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

- [protocol AVInterfaceMediaSelectionControllable](avinterfacemediaselectioncontrollable-6wn31.md)
  Provides audio and subtitle selection capabilities for media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemediaselectionoptionsource)*