# FocusInteractions

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [static var automatic: FocusInteractions](./focusinteractions/automatic.md)
  The view supports whatever focus-driven interactions are commonly expected for interactive content on the current platform.
- [static let activate: FocusInteractions](./focusinteractions/activate.md)
  The view has a primary action that can be activated via focus gestures.
- [static let edit: FocusInteractions](./focusinteractions/edit.md)
  The view captures input from non-spatial sources like a keyboard or Digital Crown.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Indicating that a view can receive focus
- [func focusable(Bool) -> some View](./view/focusable%28_%29.md)
  Specifies if the view is focusable.
- [func focusable(Bool, interactions: FocusInteractions) -> some View](./view/focusable%28_,interactions%29.md)
  Specifies if the view is focusable, and if so, what focus-driven interactions it supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusinteractions)*