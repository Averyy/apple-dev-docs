# accessibilityTextContentType(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets an accessibility text content type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityTextContentType(_ value: AccessibilityTextContentType) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this modifier to set the content type of this accessibility element. Assistive technologies can use this property to choose an appropriate way to output the text. For example, when encountering a source coding context, VoiceOver could choose to speak all punctuation.

The default content type [`plain`](accessibilitytextcontenttype/plain.md).

## Parameters

- `value`: The accessibility content type from the available    options.

## See Also

- [func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityheading(_:).md)
  Sets the accessibility level of this heading.
- [enum AccessibilityHeadingLevel](accessibilityheadinglevel.md)
  The hierarchy of a heading in relation to other headings.
- [struct AccessibilityTextContentType](accessibilitytextcontenttype.md)
  Textual context that assistive technologies can use to improve the presentation of spoken text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilitytextcontenttype(_:))*