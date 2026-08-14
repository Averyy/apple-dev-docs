# accessibilitySpeechPunctuation

**Framework**: Foundation  
**Kind**: property

A key that indicates whether to speak punctuation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
nonisolated
static let accessibilitySpeechPunctuation: NSAttributedString.Key
```

#### Discussion

The value of this key is an [`NSNumber`](nsnumber.md) object that the system interprets as a Boolean value. When the value is [`true`](https://developer.apple.com/documentation/swift/true), the assistive app speaks all punctuation in the text. You might use this for code or other text where the punctuation is relevant.

## See Also

- [static let accessibilityAlignment: NSAttributedString.Key](nsattributedstring/key/accessibilityalignment.md)
- [static let accessibilityAnnotationTextAttribute: NSAttributedString.Key](nsattributedstring/key/accessibilityannotationtextattribute.md)
- [static let accessibilityAttachment: NSAttributedString.Key](nsattributedstring/key/accessibilityattachment.md)
  Text attachment (`id`).
- [static let accessibilityAutocorrected: NSAttributedString.Key](nsattributedstring/key/accessibilityautocorrected.md)
  Autocorrected text (`NSNumber` as a Boolean value).
- [static let accessibilityBackgroundColor: NSAttributedString.Key](nsattributedstring/key/accessibilitybackgroundcolor.md)
  Text background color (`CGColorRef`).
- [static let accessibilityCustomText: NSAttributedString.Key](nsattributedstring/key/accessibilitycustomtext.md)
- [static let accessibilityFont: NSAttributedString.Key](nsattributedstring/key/accessibilityfont.md)
  Font keys (`NSDictionary`).
- [static let accessibilityFontBoldAttribute: NSAttributedString.Key](nsattributedstring/key/accessibilityfontboldattribute.md)
- [static let accessibilityFontItalicAttribute: NSAttributedString.Key](nsattributedstring/key/accessibilityfontitalicattribute.md)
- [static let accessibilityForegroundColor: NSAttributedString.Key](nsattributedstring/key/accessibilityforegroundcolor.md)
  Text foreground color (`CGColorRef`).
- [static let accessibilityLanguage: NSAttributedString.Key](nsattributedstring/key/accessibilitylanguage.md)
- [static let accessibilityLink: NSAttributedString.Key](nsattributedstring/key/accessibilitylink.md)
  Text link (`id`).
- [static let accessibilityListItemIndex: NSAttributedString.Key](nsattributedstring/key/accessibilitylistitemindex.md)
- [static let accessibilityListItemLevel: NSAttributedString.Key](nsattributedstring/key/accessibilitylistitemlevel.md)
- [static let accessibilityListItemPrefix: NSAttributedString.Key](nsattributedstring/key/accessibilitylistitemprefix.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/accessibilityspeechpunctuation)*