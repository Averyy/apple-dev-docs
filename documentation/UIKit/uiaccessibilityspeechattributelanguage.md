# UIAccessibilitySpeechAttributeLanguage

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

A key that indicates the language to use when speaking a string.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern NSAttributedStringKey const UIAccessibilitySpeechAttributeLanguage;
```

## Discussion

The value of this key is an [`NSString`](../Foundation/nsstring.md) object that contains a BCP 47 language code. When applying it to text in a string, the rules for the specified language govern how to pronounce that string.

## See Also

### Constants
- [UIAccessibilitySpeechAttributePunctuation](./uiaccessibilityspeechattributepunctuation.md)
  A key that indicates whether to speak punctuation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityspeechattributelanguage)*