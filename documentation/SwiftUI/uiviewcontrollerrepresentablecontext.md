# UIViewControllerRepresentableContext

**Framework**: SwiftUI  
**Kind**: struct

Contextual information about the state of the system that you use to create and update your UIKit view controller.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct UIViewControllerRepresentableContext<Representable> where Representable : UIViewControllerRepresentable
```

#### Overview

A [`UIViewControllerRepresentableContext`](uiviewcontrollerrepresentablecontext.md) structure contains details about the current state of the system. When creating and updating your view controller, the system creates one of these structures and passes it to the appropriate method of your custom [`UIViewControllerRepresentable`](uiviewcontrollerrepresentable.md) instance. Use the information in this structure to configure your view controller. For example, use the provided environment values to configure the appearance of your view controller and views. Don’t create this structure yourself.

## Topics

### Coordinating view controller interactions
- [let coordinator: Representable.Coordinator](uiviewcontrollerrepresentablecontext/coordinator.md)
  The view’s associated coordinator.
- [var transaction: Transaction](uiviewcontrollerrepresentablecontext/transaction.md)
  The current transaction.
### Getting the environment data
- [var environment: EnvironmentValues](uiviewcontrollerrepresentablecontext/environment.md)
  Environment values that describe the current state of the system.
### Instance Methods
- [func animate(changes: () -> Void, completion: (() -> Void)?)](uiviewcontrollerrepresentablecontext/animate(changes:completion:).md)
  Animates changes using the animation in the current transaction.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol UIViewRepresentable](uiviewrepresentable.md)
  A wrapper for a UIKit view that you use to integrate that view into your SwiftUI view hierarchy.
- [struct UIViewRepresentableContext](uiviewrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update your UIKit view.
- [protocol UIViewControllerRepresentable](uiviewcontrollerrepresentable.md)
  A view that represents a UIKit view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentablecontext)*