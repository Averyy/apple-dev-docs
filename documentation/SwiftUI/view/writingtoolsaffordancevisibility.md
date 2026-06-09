# writingToolsAffordanceVisibility(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies whether the system should show the Writing Tools affordance for text input views affected by the environment.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
nonisolated
func writingToolsAffordanceVisibility(_ visibility: Visibility) -> some View
```

#### Return Value

A view with the specified Writing Tools affordance visibility.

#### Discussion

Use this view modifier to disable the Writing Tools affordance for [`TextField`](textfield.md) views when running on macOS or Mac Catalyst.

## Parameters

- `visibility`: Whether the affordance may be shown for text input views.

## See Also

- [func writingToolsBehavior(WritingToolsBehavior) -> some View](view/writingtoolsbehavior(_:).md)
  Specifies the Writing Tools behavior for text and text input in the environment.
- [struct WritingToolsBehavior](writingtoolsbehavior.md)
  The Writing Tools editing experience for text and text input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/writingtoolsaffordancevisibility(_:))*