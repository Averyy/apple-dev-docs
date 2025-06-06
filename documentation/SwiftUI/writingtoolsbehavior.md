# WritingToolsBehavior

**Framework**: SwiftUI  
**Kind**: struct

The Writing Tools editing experience for text and text input.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.4+

## Declaration

```swift
struct WritingToolsBehavior
```

## Topics

### Type Properties
- [static let automatic: WritingToolsBehavior](writingtoolsbehavior/automatic.md)
  An appropriate editing experience will be provided based on context, which may include disabling the writing tools.
- [static let complete: WritingToolsBehavior](writingtoolsbehavior/complete.md)
  The complete inline-editing experience is provided if possible.
- [static let disabled: WritingToolsBehavior](writingtoolsbehavior/disabled.md)
  The writing tools are disabled.
- [static let limited: WritingToolsBehavior](writingtoolsbehavior/limited.md)
  The limited, overlay-panel experience is provided if possible.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func writingToolsBehavior(WritingToolsBehavior) -> some View](view/writingtoolsbehavior(_:).md)
  Specifies the Writing Tools behavior for text and text input in the environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/writingtoolsbehavior)*