# formStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style for forms in a view hierarchy.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func formStyle<S>(_ style: S) -> some View where S : FormStyle
```

#### Return Value

A view that uses the specified form style for itself and its child views.

## Parameters

- `style`: The form style to set.

## See Also

- [struct Form](form.md)
  A container for grouping controls used for data entry, such as in settings or inspectors.
- [struct LabeledContent](labeledcontent.md)
  A container for attaching a label to a value-bearing view.
- [func labeledContentStyle<S>(S) -> some View](view/labeledcontentstyle(_:).md)
  Sets a style for labeled content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/formstyle(_:))*