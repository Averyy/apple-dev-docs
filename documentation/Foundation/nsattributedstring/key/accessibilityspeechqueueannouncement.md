# accessibilitySpeechQueueAnnouncement

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A key that indicates whether to queue an announcement behind existing speech or to interrupt it.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+ - Deprecated in 1.0 (renamed: NSAttributedString.Key.accessibilitySpeechAnnouncementPriority)
- watchOS 4.0+

## Declaration

```swift
nonisolated
static let accessibilitySpeechQueueAnnouncement: NSAttributedString.Key
```

## Discussion

The value of this key is an [`NSNumber`](../../nsnumber.md) object that the system interprets as a Boolean value. When the value is [`true`](../../../Swift/true.md), the system queues the announcement behind existing speech. When the value is [`false`](../../../Swift/false.md), the announcement interrupts the existing speech. The default behavior is to interrupt existing speech.

## See Also

### Getting accessibility attribute keys
- [static let accessibilityAlignment: NSAttributedString.Key](./accessibilityalignment.md)
- [static let accessibilityAnnotationTextAttribute: NSAttributedString.Key](./accessibilityannotationtextattribute.md)
- [static let accessibilityAttachment: NSAttributedString.Key](./accessibilityattachment.md)
  Text attachment (`id`).
- [static let accessibilityAutocorrected: NSAttributedString.Key](./accessibilityautocorrected.md)
  Autocorrected text (`NSNumber` as a Boolean value).
- [static let accessibilityBackgroundColor: NSAttributedString.Key](./accessibilitybackgroundcolor.md)
  Text background color (`CGColorRef`).
- [static let accessibilityCustomText: NSAttributedString.Key](./accessibilitycustomtext.md)
- [static let accessibilityFont: NSAttributedString.Key](./accessibilityfont.md)
  Font keys (`NSDictionary`).
- [static let accessibilityFontBoldAttribute: NSAttributedString.Key](./accessibilityfontboldattribute.md)
- [static let accessibilityFontItalicAttribute: NSAttributedString.Key](./accessibilityfontitalicattribute.md)
- [static let accessibilityForegroundColor: NSAttributedString.Key](./accessibilityforegroundcolor.md)
  Text foreground color (`CGColorRef`).
- [static let accessibilityLanguage: NSAttributedString.Key](./accessibilitylanguage.md)
- [static let accessibilityLink: NSAttributedString.Key](./accessibilitylink.md)
  Text link (`id`).
- [static let accessibilityListItemIndex: NSAttributedString.Key](./accessibilitylistitemindex.md)
- [static let accessibilityListItemLevel: NSAttributedString.Key](./accessibilitylistitemlevel.md)
- [static let accessibilityListItemPrefix: NSAttributedString.Key](./accessibilitylistitemprefix.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/accessibilityspeechqueueannouncement)*