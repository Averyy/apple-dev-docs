# writingToolsBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies the Writing Tools behavior for text and text input in the environment.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency func writingToolsBehavior(_ behavior: WritingToolsBehavior) -> some View
```

#### Return Value

A view preferring the specified Writing Tools behavior.

#### Discussion

Use this view modifier to customize or disable the Writing Tools editing experience for [`Text`](text.md) (when selectable), [`TextField`](textfield.md), and [`TextEditor`](texteditor.md) views.

## Parameters

- `behavior`: The Writing Tools behavior for text and text input in the   environment.

## See Also

- [struct WritingToolsBehavior](writingtoolsbehavior.md)
  The Writing Tools editing experience for text and text input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/writingtoolsbehavior(_:))*