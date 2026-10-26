# UIAccessibilitySpeechAttributeQueueAnnouncement

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

A key that indicates whether to queue an announcement behind existing speech or to interrupt it.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+

## Declaration

```c
extern NSAttributedStringKey const UIAccessibilitySpeechAttributeQueueAnnouncement;
```

#### Overview

The value of this key is an [`NSNumber`](../Foundation/nsnumber.md) object that the system interprets as a Boolean value. When the value is `YES`, the system queues the announcement behind existing speech. When the value is `NO`, the announcement interrupts the existing speech. The default behavior is to interrupt existing speech.

## See Also

### Constants
- [UIAccessibilitySpeechAttributePunctuation](./uiaccessibilityspeechattributepunctuation.md)
  A key that indicates whether to speak punctuation.
- [UIAccessibilitySpeechAttributeLanguage](./uiaccessibilityspeechattributelanguage.md)
  A key that indicates the language to use when speaking a string.
- [UIAccessibilitySpeechAttributePitch](./uiaccessibilityspeechattributepitch.md)
  A key that indicates the pitch to apply to spoken content.
- [UIAccessibilitySpeechAttributeIPANotation](./uiaccessibilityspeechattributeipanotation.md)
  A key that indicates the pronunciation of a specific word or phrase, such as a proper name.
- [UIAccessibilitySpeechAttributeAnnouncementPriority](./uiaccessibilityspeechattributeannouncementpriority.md)
- [UIAccessibilitySpeechAttributeSpellOut](./uiaccessibilityspeechattributespellout.md)
- [struct UIAccessibilityPriority](./uiaccessibilitypriority.md)
  Constants that specify priorities for accessibility announcements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityspeechattributequeueannouncement)*