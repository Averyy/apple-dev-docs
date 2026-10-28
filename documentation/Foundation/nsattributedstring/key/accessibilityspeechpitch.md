# accessibilitySpeechPitch

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A key that indicates the pitch to apply to spoken content.

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
static let accessibilitySpeechPitch: NSAttributedString.Key
```

## Discussion

The value of this key is an [`NSNumber`](../../nsnumber.md) object that contains a floating-point value in the range of `0.0` to `2.0`. The value indicates whether to speak the text with a higher or lower pitch than the default. The default value for this attribute is `1.0`, which indicates a normal pitch. Values between `0.0` and `1.0` result in a lower pitch, and values between `1.0` and `2.0` result in a higher pitch.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/accessibilityspeechpitch)*