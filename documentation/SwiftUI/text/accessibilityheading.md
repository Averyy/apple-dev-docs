# accessibilityHeading(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the accessibility level of this heading.

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
func accessibilityHeading(_ level: AccessibilityHeadingLevel) -> Text
```

#### Discussion

Use this modifier to set the level of this heading in relation to other headings. The system speaks the level number of levels [`AccessibilityHeadingLevel.h1`](accessibilityheadinglevel/h1.md) through [`AccessibilityHeadingLevel.h6`](accessibilityheadinglevel/h6.md) alongside the text.

The default heading level if you don’t use this modifier is [`AccessibilityHeadingLevel.unspecified`](accessibilityheadinglevel/unspecified.md).

## Parameters

- `level`: The heading level to associate with this element   from the available   levels.

## See Also

- [func accessibilityLabel(_:)](text/accessibilitylabel(_:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityTextContentType(AccessibilityTextContentType) -> Text](text/accessibilitytextcontenttype(_:).md)
  Sets an accessibility text content type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/accessibilityheading(_:))*