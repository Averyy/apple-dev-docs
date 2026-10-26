# UIAccessibilitySpeechAttributePunctuation

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

A key that indicates whether to speak punctuation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern NSAttributedStringKey const UIAccessibilitySpeechAttributePunctuation;
```

#### Overview

The value of this key is an [`NSNumber`](../Foundation/nsnumber.md) object that the system interprets as a Boolean value. When the value is `YES`, the assistive app speaks all punctuation in the text. You might use this for code or other text where the punctuation is relevant.

## See Also

### Constants
- [UIAccessibilitySpeechAttributeLanguage](./uiaccessibilityspeechattributelanguage.md)
  A key that indicates the language to use when speaking a string.
- [UIAccessibilitySpeechAttributePitch](./uiaccessibilityspeechattributepitch.md)
  A key that indicates the pitch to apply to spoken content.
- [UIAccessibilitySpeechAttributeQueueAnnouncement](./uiaccessibilityspeechattributequeueannouncement.md)
  A key that indicates whether to queue an announcement behind existing speech or to interrupt it.
- [UIAccessibilitySpeechAttributeIPANotation](./uiaccessibilityspeechattributeipanotation.md)
  A key that indicates the pronunciation of a specific word or phrase, such as a proper name.
- [UIAccessibilitySpeechAttributeAnnouncementPriority](./uiaccessibilityspeechattributeannouncementpriority.md)
- [UIAccessibilitySpeechAttributeSpellOut](./uiaccessibilityspeechattributespellout.md)
- [struct UIAccessibilityPriority](./uiaccessibilitypriority.md)
  Constants that specify priorities for accessibility announcements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityspeechattributepunctuation)*