# accessibilityHeading(_:)

**Framework**: SwiftUI  
**Kind**: method

Set the level of this heading.

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
func accessibilityHeading(_ level: AccessibilityHeadingLevel) -> ModifiedContent<Content, Modifier>
```

#### Discussion

Use this modifier to set the level of this heading in relation to other headings. The system speaks the level number of levels [`AccessibilityHeadingLevel.h1`](accessibilityheadinglevel/h1.md) through [`AccessibilityHeadingLevel.h6`](accessibilityheadinglevel/h6.md) alongside the text.

The default heading level if you don’t use this modifier is [`AccessibilityHeadingLevel.unspecified`](accessibilityheadinglevel/unspecified.md).

## Parameters

- `level`: The heading level to associate with this element   from the available   levels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityheading(_:))*