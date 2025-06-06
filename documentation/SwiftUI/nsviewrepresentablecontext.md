# NSViewRepresentableContext

**Framework**: SwiftUI  
**Kind**: struct

Contextual information about the state of the system that you use to create and update your AppKit view.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency struct NSViewRepresentableContext<View> where View : NSViewRepresentable
```

#### Overview

An [`NSViewRepresentableContext`](nsviewrepresentablecontext.md) structure contains details about the current state of the system. When creating and updating your view, the system creates one of these structures and passes it to the appropriate method of your custom [`NSViewRepresentable`](nsviewrepresentable.md) instance. Use the information in this structure to configure your view. For example, use the provided environment values to configure the appearance of your view. Don’t create this structure yourself.

## Topics

### Coordinating view-related interactions
- [let coordinator: View.Coordinator](nsviewrepresentablecontext/coordinator.md)
  An instance you use to communicate your AppKit view’s behavior and state out to SwiftUI objects.
- [var transaction: Transaction](nsviewrepresentablecontext/transaction.md)
  The current transaction.
### Getting the current environment data
- [var environment: EnvironmentValues](nsviewrepresentablecontext/environment.md)
  Environment data that describes the current state of the system.
### Instance Methods
- [func animate(changes: () -> Void, completion: (() -> Void)?)](nsviewrepresentablecontext/animate(changes:completion:).md)
  Animates changes using the animation in the current transaction.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol NSViewRepresentable](nsviewrepresentable.md)
  A wrapper that you use to integrate an AppKit view into your SwiftUI view hierarchy.
- [protocol NSViewControllerRepresentable](nsviewcontrollerrepresentable.md)
  A wrapper that you use to integrate an AppKit view controller into your SwiftUI interface.
- [struct NSViewControllerRepresentableContext](nsviewcontrollerrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update your AppKit view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewrepresentablecontext)*