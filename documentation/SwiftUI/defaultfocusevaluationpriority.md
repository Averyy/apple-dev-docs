# DefaultFocusEvaluationPriority

**Framework**: SwiftUI  
**Kind**: struct

Prioritizations for default focus preferences when evaluating where to move focus in different circumstances.

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
struct DefaultFocusEvaluationPriority
```

## Topics

### Getting the priorities
- [static let automatic: DefaultFocusEvaluationPriority](defaultfocusevaluationpriority/automatic.md)
  Use the default focus preference when focus moves into the affected branch automatically, but ignore it when the movement is driven by a user-initiated navigation command.
- [static let userInitiated: DefaultFocusEvaluationPriority](defaultfocusevaluationpriority/userinitiated.md)
  Always use the default focus preference when focus moves into the affected branch.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func prefersDefaultFocus(Bool, in: Namespace.ID) -> some View](view/prefersdefaultfocus(_:in:).md)
  Indicates that the view should receive focus by default for a given namespace.
- [func defaultFocus<V>(FocusState<V>.Binding, V, priority: DefaultFocusEvaluationPriority) -> some View](view/defaultfocus(_:_:priority:).md)
  Defines a region of the window in which default focus is evaluated by assigning a value to a given focus state binding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/defaultfocusevaluationpriority)*