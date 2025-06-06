# UIViewRepresentableContext

**Framework**: SwiftUI  
**Kind**: struct

Contextual information about the state of the system that you use to create and update your UIKit view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct UIViewRepresentableContext<Representable> where Representable : UIViewRepresentable
```

#### Overview

A [`UIViewRepresentableContext`](uiviewrepresentablecontext.md) structure contains details about the current state of the system. When creating and updating your view, the system creates one of these structures and passes it to the appropriate method of your custom [`UIViewRepresentable`](uiviewrepresentable.md) instance. Use the information in this structure to configure your view. For example, use the provided environment values to configure the appearance of your view. Don’t create this structure yourself.

## Topics

### Coordinating view-related interactions
- [let coordinator: Representable.Coordinator](uiviewrepresentablecontext/coordinator.md)
  The view’s associated coordinator.
- [var transaction: Transaction](uiviewrepresentablecontext/transaction.md)
  The current transaction.
### Getting the current environment data
- [var environment: EnvironmentValues](uiviewrepresentablecontext/environment.md)
  The current environment.
### Instance Methods
- [func animate(changes: () -> Void, completion: (() -> Void)?)](uiviewrepresentablecontext/animate(changes:completion:).md)
  Animates changes using the animation in the current transaction.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol UIViewRepresentable](uiviewrepresentable.md)
  A wrapper for a UIKit view that you use to integrate that view into your SwiftUI view hierarchy.
- [protocol UIViewControllerRepresentable](uiviewcontrollerrepresentable.md)
  A view that represents a UIKit view controller.
- [struct UIViewControllerRepresentableContext](uiviewcontrollerrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update your UIKit view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiviewrepresentablecontext)*