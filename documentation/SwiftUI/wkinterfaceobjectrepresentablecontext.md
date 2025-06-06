# WKInterfaceObjectRepresentableContext

**Framework**: SwiftUI  
**Kind**: struct

Contextual information about the state of the system that you use to create and update your WatchKit interface object.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency struct WKInterfaceObjectRepresentableContext<Representable> where Representable : WKInterfaceObjectRepresentable
```

#### Overview

A [`WKInterfaceObjectRepresentableContext`](wkinterfaceobjectrepresentablecontext.md) structure contains details about the current state of the system. When creating and updating your interface objects, the system creates one of these structures and passes it to the appropriate method of your custom [`WKInterfaceObjectRepresentable`](wkinterfaceobjectrepresentable.md) instance. Use the information in this structure to configure your object. Don’t create this structure yourself.

## Topics

### Coordinating interactions
- [let coordinator: Representable.Coordinator](wkinterfaceobjectrepresentablecontext/coordinator.md)
  The view’s associated coordinator.
- [var transaction: Transaction](wkinterfaceobjectrepresentablecontext/transaction.md)
  The current transaction.
### Getting the current environment data
- [var environment: EnvironmentValues](wkinterfaceobjectrepresentablecontext/environment.md)
  The current environment.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol WKInterfaceObjectRepresentable](wkinterfaceobjectrepresentable.md)
  A view that represents a WatchKit interface object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkinterfaceobjectrepresentablecontext)*