# accessibilitySpeechLanguage

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A key that indicates the language to use when speaking a string.

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
static let accessibilitySpeechLanguage: NSAttributedString.Key
```

## Discussion

The value of this key is an [`NSString`](../../nsstring.md) object that contains a BCP 47 language code. When applying it to text in a string, the rules for the specified language govern how to pronounce that string.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/accessibilityspeechlanguage)*