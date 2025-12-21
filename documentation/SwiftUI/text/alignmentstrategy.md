# Text.AlignmentStrategy

**Framework**: SwiftUI  
**Kind**: struct

The way SwiftUI infers the appropriate text alignment if no value is explicitly provided.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct AlignmentStrategy
```

#### Overview

> **Note**: [`Text`](text.md) tightly wraps its content, so text alignment only affects how lines are positioned relative to each other. The text as a whole needs to be positioned at the view level using [`Alignment`](alignment.md).

## Topics

### Type Properties
- [static let `default`: Text.AlignmentStrategy](text/alignmentstrategy/default.md)
  The default strategy based on the context it is used in.
- [static let layoutBased: Text.AlignmentStrategy](text/alignmentstrategy/layoutbased.md)
  The alignment following the environment setting.
- [static let writingDirectionBased: Text.AlignmentStrategy](text/alignmentstrategy/writingdirectionbased.md)
  The alignment following the writing direction of the same paragraph.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/alignmentstrategy)*