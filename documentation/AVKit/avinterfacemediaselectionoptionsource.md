# AVInterfaceMediaSelectionOptionSource

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

Represents a media selection option for audio tracks or subtitle tracks.

## Declaration

```objc
@interface AVInterfaceMediaSelectionOptionSource : NSObject
```

#### Overview

This class represents individual media options (such as audio tracks or subtitle tracks) that can be selected by the user in media playback interfaces. Each option provides display information and metadata for user selection.

## Topics

### Instance Properties
- [displayName](./avinterfacemediaselectionoptionsource/displayname.md)
  Human-readable name for this media option displayed in user interfaces (e.g., “English”, “Spanish (Latin America)”, “Director’s Commentary”).
- [extendedLanguageTag](./avinterfacemediaselectionoptionsource/extendedlanguagetag.md)
  IETF BCP 47 language identifier (e.g., “en-US”, “es-419”, “zh-Hans-CN”) indicating the primary language and locale of this option. This standardized tag provides detailed language information including region, script, and variants. May be empty for language-neutral content such as music-only audio tracks, sound effects, or visual-only subtitles without spoken content.
- [identifier](./avinterfacemediaselectionoptionsource/identifier.md)
  Unique system identifier for this media option, used for programmatic selection and persistence across sessions.
### Instance Methods
- [- initWithDisplayName:identifier:extendedLanguageTag:](./avinterfacemediaselectionoptionsource/initwithdisplayname_identifier_extendedlanguagetag_.md)
  Initializes a new media selection option with the specified attributes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemediaselectionoptionsource)*