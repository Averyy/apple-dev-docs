# UIAccessibilitySpeechAttributePitch

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

A key that indicates the pitch to apply to spoken content.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern NSAttributedStringKey const UIAccessibilitySpeechAttributePitch;
```

## Overview

The value of this key is an [`NSNumber`](../Foundation/nsnumber.md) object that contains a floating-point value in the range of `0.0` to `2.0`. The value indicates whether to speak the text with a higher or lower pitch than the default. The default value for this attribute is `1.0`, which indicates a normal pitch. Values between `0.0` and `1.0` result in a lower pitch, and values between `1.0` and `2.0` result in a higher pitch.

## See Also

### Constants
- [UIAccessibilitySpeechAttributePunctuation](./uiaccessibilityspeechattributepunctuation.md)
  A key that indicates whether to speak punctuation.
- [UIAccessibilitySpeechAttributeLanguage](./uiaccessibilityspeechattributelanguage.md)
  A key that indicates the language to use when speaking a string.
- [UIAccessibilitySpeechAttributeQueueAnnouncement](./uiaccessibilityspeechattributequeueannouncement.md)
  A key that indicates whether to queue an announcement behind existing speech or to interrupt it.
- [UIAccessibilitySpeechAttributeIPANotation](./uiaccessibilityspeechattributeipanotation.md)
  A key that indicates the pronunciation of a specific word or phrase, such as a proper name.
- [UIAccessibilitySpeechAttributeAnnouncementPriority](./uiaccessibilityspeechattributeannouncementpriority.md)
- [UIAccessibilitySpeechAttributeSpellOut](./uiaccessibilityspeechattributespellout.md)
- [struct UIAccessibilityPriority](./uiaccessibilitypriority.md)
  Constants that specify priorities for accessibility announcements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityspeechattributepitch)*