# AttributeScopes.AccessibilityAttributes

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct AccessibilityAttributes
```

## Topics

### Instance Properties
- [let accessibilityHeadingLevel: AttributeScopes.AccessibilityAttributes.HeadingLevelAttribute](./accessibilityattributes/accessibilityheadinglevel.md)
- [let accessibilitySpeechAdjustedPitch: AttributeScopes.AccessibilityAttributes.AdjustedPitchAttribute](./accessibilityattributes/accessibilityspeechadjustedpitch.md)
- [let accessibilitySpeechAnnouncementPriority: AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute](./accessibilityattributes/accessibilityspeechannouncementpriority.md)
- [let accessibilitySpeechAnnouncementsQueued: AttributeScopes.AccessibilityAttributes.QueueAnnouncementAttribute](./accessibilityattributes/accessibilityspeechannouncementsqueued.md)
- [let accessibilitySpeechIncludesPunctuation: AttributeScopes.AccessibilityAttributes.IncludesPunctuationAttribute](./accessibilityattributes/accessibilityspeechincludespunctuation.md)
- [let accessibilitySpeechPhoneticNotation: AttributeScopes.AccessibilityAttributes.IPANotationAttribute](./accessibilityattributes/accessibilityspeechphoneticnotation.md)
- [let accessibilitySpeechSSML: AttributeScopes.AccessibilityAttributes.SpeechSSMLAttribute](./accessibilityattributes/accessibilityspeechssml.md)
  An SSML fragment describing how the annotated range should be spoken.
- [let accessibilitySpeechSpellsOutCharacters: AttributeScopes.AccessibilityAttributes.SpellOutAttribute](./accessibilityattributes/accessibilityspeechspellsoutcharacters.md)
- [let accessibilityTextCustom: AttributeScopes.AccessibilityAttributes.TextCustomAttribute](./accessibilityattributes/accessibilitytextcustom.md)
- [let accessibilityTextualContext: AttributeScopes.AccessibilityAttributes.TextualContextAttribute](./accessibilityattributes/accessibilitytextualcontext.md)
### Enumerations
- [AttributeScopes.AccessibilityAttributes.AdjustedPitchAttribute](./accessibilityattributes/adjustedpitchattribute.md)
  An attribute to adjust the pitch the spoken speech.
- [AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute](./accessibilityattributes/announcementpriorityattribute.md)
  An attribute to define the urgency of the announcement.
- [AttributeScopes.AccessibilityAttributes.HeadingLevelAttribute](./accessibilityattributes/headinglevelattribute.md)
  An attribute for the level of this heading.
- [AttributeScopes.AccessibilityAttributes.IPANotationAttribute](./accessibilityattributes/ipanotationattribute.md)
  An attribute to define the International Phonetic Alphabet representation for speech.
- [AttributeScopes.AccessibilityAttributes.IncludesPunctuationAttribute](./accessibilityattributes/includespunctuationattribute.md)
  An attribute to define how punctuation should be spoken.
- [AttributeScopes.AccessibilityAttributes.QueueAnnouncementAttribute](./accessibilityattributes/queueannouncementattribute.md)
  An attribute to define if speech announcements spoken by VoiceOver should be queued behind existing speech rather than interrupting speech in progress.
- [AttributeScopes.AccessibilityAttributes.SpeechSSMLAttribute](./accessibilityattributes/speechssmlattribute.md)
  An attribute for an SSML fragment describing how the annotated range should be spoken.
- [AttributeScopes.AccessibilityAttributes.SpellOutAttribute](./accessibilityattributes/spelloutattribute.md)
  An attribute to define if each character should be spoken separately.
- [AttributeScopes.AccessibilityAttributes.TextCustomAttribute](./accessibilityattributes/textcustomattribute.md)
  An attribute for custom, localized text attributes.
- [AttributeScopes.AccessibilityAttributes.TextualContextAttribute](./accessibilityattributes/textualcontextattribute.md)
  An attribute for the textual context.

## Relationships

### Conforms To
- [AttributeScope](../attributescope.md)
- [DecodingConfigurationProviding](../decodingconfigurationproviding.md)
- [EncodingConfigurationProviding](../encodingconfigurationproviding.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes)*