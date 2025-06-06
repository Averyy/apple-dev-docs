# DispatchQoS.QoSClass.userInteractive

**Framework**: Dispatch  
**Kind**: case

The quality-of-service class for user-interactive tasks, such as animations, event handling, or updating your app’s user interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case userInteractive
```

#### Discussion

User-interactive tasks have the highest priority on the system. Use this class for tasks or queues that interact with the user or actively update your app’s user interface. For example, use this for class for animations or for tracking events interactively.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqos/qosclass-swift.enum/userinteractive)*