# AccessibilityHeadingLevel

**Framework**: SwiftUI  
**Kind**: enum

The hierarchy of a heading in relation to other headings.

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
@frozen
enum AccessibilityHeadingLevel
```

#### Overview

Assistive technologies can use this to improve a user’s navigation through multiple headings. When users navigate through top level headings they expect the content for each heading to be unrelated.

For example, you can categorize a list of available products into sections, like Fruits and Vegetables. With only top level headings, this list requires no heading hierarchy, and you use the [`AccessibilityHeadingLevel.unspecified`](accessibilityheadinglevel/unspecified.md) heading level. On the other hand, if sections contain subsections, like if the Fruits section has subsections for varieties of Apples, Pears, and so on, you apply the [`AccessibilityHeadingLevel.h1`](accessibilityheadinglevel/h1.md) level to Fruits and Vegetables, and the [`AccessibilityHeadingLevel.h2`](accessibilityheadinglevel/h2.md) level to Apples and Pears.

Except for [`AccessibilityHeadingLevel.h1`](accessibilityheadinglevel/h1.md), be sure to precede all leveled headings by another heading with a level that’s one less.

## Topics

### Getting the heading level
- [AccessibilityHeadingLevel.h1](accessibilityheadinglevel/h1.md)
  Level 1 heading.
- [AccessibilityHeadingLevel.h2](accessibilityheadinglevel/h2.md)
  Level 2 heading.
- [AccessibilityHeadingLevel.h3](accessibilityheadinglevel/h3.md)
  Level 3 heading.
- [AccessibilityHeadingLevel.h4](accessibilityheadinglevel/h4.md)
  Level 4 heading.
- [AccessibilityHeadingLevel.h5](accessibilityheadinglevel/h5.md)
  Level 5 heading.
- [AccessibilityHeadingLevel.h6](accessibilityheadinglevel/h6.md)
  Level 6 heading.
- [AccessibilityHeadingLevel.unspecified](accessibilityheadinglevel/unspecified.md)
  A heading without a hierarchy.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func accessibilityTextContentType(AccessibilityTextContentType) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilitytextcontenttype(_:).md)
  Sets an accessibility text content type.
- [func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityheading(_:).md)
  Sets the accessibility level of this heading.
- [struct AccessibilityTextContentType](accessibilitytextcontenttype.md)
  Textual context that assistive technologies can use to improve the presentation of spoken text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityheadinglevel)*