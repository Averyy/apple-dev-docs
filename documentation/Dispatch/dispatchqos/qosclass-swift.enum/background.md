# DispatchQoS.QoSClass.background

**Framework**: Dispatch  
**Kind**: case

The quality-of-service class for maintenance or cleanup tasks that you create.

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
case background
```

#### Discussion

Background tasks have the lowest priority of all tasks. Assign this class to tasks or dispatch queues that you use to perform work while your app is running in the background.

## See Also

- [DispatchQoS.QoSClass.userInteractive](dispatchqos/qosclass-swift.enum/userinteractive.md)
  The quality-of-service class for user-interactive tasks, such as animations, event handling, or updating your app’s user interface.
- [DispatchQoS.QoSClass.userInitiated](dispatchqos/qosclass-swift.enum/userinitiated.md)
  The quality-of-service class for tasks that prevent the user from actively using your app.
- [DispatchQoS.QoSClass.default](dispatchqos/qosclass-swift.enum/default.md)
  The default quality-of-service class.
- [DispatchQoS.QoSClass.utility](dispatchqos/qosclass-swift.enum/utility.md)
  The quality-of-service class for tasks that the user does not track actively.
- [DispatchQoS.QoSClass.unspecified](dispatchqos/qosclass-swift.enum/unspecified.md)
  The absence of a quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqos/qosclass-swift.enum/background)*