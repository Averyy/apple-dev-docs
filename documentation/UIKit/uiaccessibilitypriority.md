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

Use these constants either with the [`accessibilitySpeechAnnouncementPriority`](https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/4183580-accessibilityspeechannouncementp) property of [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString), or with the [`accessibilitySpeechAnnouncementPriority`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/4168159-accessibilityspeechannouncementp) (Swift) or [`UIAccessibilitySpeechAttributeAnnouncementPriority`](uiaccessibilityspeechattributeannouncementpriority.md) (Objective-C) attributed key. For example, the following code shows how to create an announcement with a [`high`](uiaccessibilitypriority/high.md) announcement priority:

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

## See Also

- [static let accessibilitySpeechPunctuation: NSAttributedString.Key](../foundation/nsattributedstring/key/1620201-accessibilityspeechpunctuation.md)
  A key that indicates whether to speak punctuation. 
- [static let accessibilitySpeechLanguage: NSAttributedString.Key](../foundation/nsattributedstring/key/1620188-accessibilityspeechlanguage.md)
  A key that indicates the language to use when speaking a string. 
- [static let accessibilitySpeechPitch: NSAttributedString.Key](../foundation/nsattributedstring/key/1620195-accessibilityspeechpitch.md)
  A key that indicates the pitch to apply to spoken content. 
- [static let accessibilitySpeechQueueAnnouncement: NSAttributedString.Key](../foundation/nsattributedstring/key/2865770-accessibilityspeechqueueannounce.md)
  A key that indicates whether to queue an announcement behind existing speech or to interrupt it.
- [static let accessibilitySpeechIPANotation: NSAttributedString.Key](../foundation/nsattributedstring/key/2890748-accessibilityspeechipanotation.md)
  A key that indicates the pronunciation of a specific word or phrase, such as a proper name.
- [static let accessibilitySpeechAnnouncementPriority: NSAttributedString.Key](../foundation/nsattributedstring/key/4168159-accessibilityspeechannouncementp.md)
- [static let accessibilitySpeechSpellOut: NSAttributedString.Key](../foundation/nsattributedstring/key/3333285-accessibilityspeechspellout.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitypriority)*