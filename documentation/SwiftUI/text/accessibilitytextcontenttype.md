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
func accessibilityTextContentType(_ value: AccessibilityTextContentType) -> Text
```

#### Discussion

Use this modifier to set the content type of this accessibility element. Assistive technologies can use this property to choose an appropriate way to output the text. For example, when encountering a source coding context, VoiceOver could choose to speak all punctuation.

If you don’t set a value with this method, the default content type is [`plain`](accessibilitytextcontenttype/plain.md).

## Parameters

- `value`: The accessibility content type from the available    options.

## See Also

- [func accessibilityHeading(AccessibilityHeadingLevel) -> Text](text/accessibilityheading(_:).md)
  Sets the accessibility level of this heading.
- [func accessibilityLabel(_:)](text/accessibilitylabel(_:).md)
  Adds a label to the view that describes its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/accessibilitytextcontenttype(_:))*