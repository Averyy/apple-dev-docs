# FocusInteractions

**Framework**: SwiftUI  
**Kind**: struct

Values describe different focus interactions that a view can support.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct FocusInteractions
```

## Topics

### Creating the interaction types
- [static var automatic: FocusInteractions](focusinteractions/automatic.md)
  The view supports whatever focus-driven interactions are commonly expected for interactive content on the current platform.
- [static let activate: FocusInteractions](focusinteractions/activate.md)
  The view has a primary action that can be activated via focus gestures.
- [static let edit: FocusInteractions](focusinteractions/edit.md)
  The view captures input from non-spatial sources like a keyboard or Digital Crown.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func focusable(Bool) -> some View](view/focusable(_:).md)
  Specifies if the view is focusable.
- [func focusable(Bool, interactions: FocusInteractions) -> some View](view/focusable(_:interactions:).md)
  Specifies if the view is focusable, and if so, what focus-driven interactions it supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusinteractions)*