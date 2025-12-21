# UIAccessibilityPriority

**Framework**: UIKit  
**Kind**: struct

Constants that specify priorities for accessibility announcements.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct UIAccessibilityPriority
```

#### Overview

Use these constants either with the [`accessibilitySpeechAnnouncementPriority`](https://developer.apple.com/documentation/Foundation/AttributeScopes/AccessibilityAttributes/accessibilitySpeechAnnouncementPriority) property of [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString), or with the [`UIAccessibilitySpeechAttributeAnnouncementPriority`](uiaccessibilityspeechattributeannouncementpriority.md) attributed key. For example, the following code shows how to create an announcement with a [`high`](uiaccessibilitypriority/high.md) announcement priority:

```swift
let highPriorityAnnouncement = NSAttributedString(string: "Camera active", attributes:
[NSAttributedString.Key.accessibilitySpeechAnnouncementPriority: UIAccessibilityPriority.high])
```

## Topics

### Choosing a priority
- [static let high: UIAccessibilityPriority](uiaccessibilitypriority/high.md)
  A high-priority announcement that interrupts other speech and isn’t interruptible after it starts.
- [static let `default`: UIAccessibilityPriority](uiaccessibilitypriority/default.md)
  A default-priority announcement that interrupts existing speech, but is interruptible if a new speech utterance starts.
- [static let low: UIAccessibilityPriority](uiaccessibilitypriority/low.md)
  A low-priority announcement that the system queues and speaks after other speech utterances are complete.
### Creating a priority
- [init(rawValue: String)](uiaccessibilitypriority/init(rawvalue:).md)
  Creates a priority structure with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static let accessibilitySpeechPunctuation: NSAttributedString.Key](../Foundation/NSAttributedString/Key/accessibilitySpeechPunctuation.md)
  A key that indicates whether to speak punctuation.
- [static let accessibilitySpeechLanguage: NSAttributedString.Key](../Foundation/NSAttributedString/Key/accessibilitySpeechLanguage.md)
  A key that indicates the language to use when speaking a string.
- [static let accessibilitySpeechPitch: NSAttributedString.Key](../Foundation/NSAttributedString/Key/accessibilitySpeechPitch.md)
  A key that indicates the pitch to apply to spoken content.
- [static let accessibilitySpeechQueueAnnouncement: NSAttributedString.Key](../Foundation/NSAttributedString/Key/accessibilitySpeechQueueAnnouncement.md)
  A key that indicates whether to queue an announcement behind existing speech or to interrupt it.
- [static let accessibilitySpeechIPANotation: NSAttributedString.Key](../Foundation/NSAttributedString/Key/accessibilitySpeechIPANotation.md)
  A key that indicates the pronunciation of a specific word or phrase, such as a proper name.
- [static let accessibilitySpeechAnnouncementPriority: NSAttributedString.Key](../Foundation/NSAttributedString/Key/accessibilitySpeechAnnouncementPriority.md)
- [static let accessibilitySpeechSpellOut: NSAttributedString.Key](../Foundation/NSAttributedString/Key/accessibilitySpeechSpellOut.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitypriority)*