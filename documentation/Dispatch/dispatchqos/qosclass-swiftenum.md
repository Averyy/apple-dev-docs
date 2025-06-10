# DispatchQoS.QoSClass

**Framework**: Dispatch  
**Kind**: enum

Quality-of-service classes that specify the priorities for executing tasks.

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
enum QoSClass
```

#### Overview

Use quality-of-service classes to communicate the intent behind the work that your app performs. The system uses those intentions to determine the best way to execute your tasks given the available resources. For example, the system gives higher priority to threads that contain user-interactive tasks to ensure that those tasks are executed quickly. Conversely, it gives lower priority to background tasks, and may attempt to save power by executing them on more power-efficient CPU cores. The system determines how to execute your tasks dynamically based on system conditions and the tasks you schedule.

## Topics

### Getting the Quality-of-Service Class
- [DispatchQoS.QoSClass.userInteractive](dispatchqos/qosclass-swift.enum/userinteractive.md)
  The quality-of-service class for user-interactive tasks, such as animations, event handling, or updating your app’s user interface.
- [DispatchQoS.QoSClass.userInitiated](dispatchqos/qosclass-swift.enum/userinitiated.md)
  The quality-of-service class for tasks that prevent the user from actively using your app.
- [DispatchQoS.QoSClass.default](dispatchqos/qosclass-swift.enum/default.md)
  The default quality-of-service class.
- [DispatchQoS.QoSClass.utility](dispatchqos/qosclass-swift.enum/utility.md)
  The quality-of-service class for tasks that the user does not track actively.
- [DispatchQoS.QoSClass.background](dispatchqos/qosclass-swift.enum/background.md)
  The quality-of-service class for maintenance or cleanup tasks that you create.
- [DispatchQoS.QoSClass.unspecified](dispatchqos/qosclass-swift.enum/unspecified.md)
  The absence of a quality-of-service class.
### Initializing the Type
- [init?(rawValue: qos_class_t)](dispatchqos/qosclass-swift.enum/init(rawvalue:).md)
  Initializes the type with a raw value.
- [var rawValue: qos_class_t](dispatchqos/qosclass-swift.enum/rawvalue.md)
  The value of the raw type.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(qosClass: DispatchQoS.QoSClass, relativePriority: Int)](dispatchqos/init(qosclass:relativepriority:).md)
  Creates a new `DispatchQoS` object with the specified QoS class and relative priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqos/qosclass-swift.enum)*