# NSViewControllerRepresentableContext

**Framework**: SwiftUI  
**Kind**: struct

Contextual information about the state of the system that you use to create and update your AppKit view controller.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency struct NSViewControllerRepresentableContext<ViewController> where ViewController : NSViewControllerRepresentable
```

#### Overview

An [`NSViewControllerRepresentableContext`](nsviewcontrollerrepresentablecontext.md) structure contains details about the current state of the system. When creating and updating your view controller, the system creates one of these structures and passes it to the appropriate method of your custom [`NSViewControllerRepresentable`](nsviewcontrollerrepresentable.md) instance. Use the information in this structure to configure your view controller. For example, use the provided environment values to configure the appearance of your view controller and views. Don’t create this structure yourself.

## Topics

### Coordinating view-related interactions
- [let coordinator: ViewController.Coordinator](nsviewcontrollerrepresentablecontext/coordinator.md)
  An object you use to communicate your AppKit view controller’s behavior and state out to SwiftUI objects.
- [var transaction: Transaction](nsviewcontrollerrepresentablecontext/transaction.md)
  The current transaction.
### Getting the current environment data
- [var environment: EnvironmentValues](nsviewcontrollerrepresentablecontext/environment.md)
  Environment data that describes the current state of the system.
### Instance Methods
- [func animate(changes: () -> Void, completion: (() -> Void)?)](nsviewcontrollerrepresentablecontext/animate(changes:completion:).md)
  Animates changes using the animation in the current transaction.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol NSViewRepresentable](nsviewrepresentable.md)
  A wrapper that you use to integrate an AppKit view into your SwiftUI view hierarchy.
- [struct NSViewRepresentableContext](nsviewrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update your AppKit view.
- [protocol NSViewControllerRepresentable](nsviewcontrollerrepresentable.md)
  A wrapper that you use to integrate an AppKit view controller into your SwiftUI interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentablecontext)*