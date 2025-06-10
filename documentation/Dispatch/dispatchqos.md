# DispatchQoS

**Framework**: Dispatch  
**Kind**: struct

The quality of service, or the execution priority, to apply to tasks.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct DispatchQoS
```

#### Overview

A quality-of-service (QoS) class categorizes work to perform on a [`DispatchQueue`](dispatchqueue.md). By specifying the quality of a task, you indicate its importance to your app. When scheduling tasks, the system prioritizes those that have higher service classes.

Because higher priority work is performed more quickly and with more resources than lower priority work, it typically requires more energy than lower priority work. Accurately specifying appropriate QoS classes for the work your app performs ensures that your app is responsive and energy efficient.

## Topics

### Getting the Predefined QoS Objects
- [static let userInteractive: DispatchQoS](dispatchqos/userinteractive.md)
  The quality-of-service class for user-interactive tasks, such as animations, event handling, or updates to your app’s user interface.
- [static let userInitiated: DispatchQoS](dispatchqos/userinitiated.md)
  The quality-of-service class for tasks that prevent the user from actively using your app.
- [static let `default`: DispatchQoS](dispatchqos/default.md)
  The default quality-of-service class.
- [static let utility: DispatchQoS](dispatchqos/utility.md)
  The quality-of-service class for tasks that the user does not track actively.
- [static let background: DispatchQoS](dispatchqos/background.md)
  The quality-of-service class for maintenance or cleanup tasks that you create.
- [static let unspecified: DispatchQoS](dispatchqos/unspecified.md)
  The absence of a quality-of-service class.
### Creating a QoS Structure
- [init(qosClass: DispatchQoS.QoSClass, relativePriority: Int)](dispatchqos/init(qosclass:relativepriority:).md)
  Creates a new `DispatchQoS` object with the specified QoS class and relative priority.
- [DispatchQoS.QoSClass](dispatchqos/qosclass-swift.enum.md)
  Quality-of-service classes that specify the priorities for executing tasks.
### Getting the QoS Attributes
- [let qosClass: DispatchQoS.QoSClass](dispatchqos/qosclass-swift.property.md)
  The quality-of-service class.
- [let relativePriority: Int](dispatchqos/relativepriority.md)
  The priority of a quality of service relative to others with the same class.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqos)*