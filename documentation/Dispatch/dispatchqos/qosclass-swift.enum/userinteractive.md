# DispatchQoS.QoSClass.userInteractive

**Framework**: Dispatch  
**Kind**: case  
**Role**: Case

The quality-of-service class for user-interactive tasks, such as animations, event handling, or updating your app’s user interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case userInteractive
```

#### Discussion

User-interactive tasks have the highest priority on the system. Use this class for tasks or queues that interact with the user or actively update your app’s user interface. For example, use this for class for animations or for tracking events interactively.

## See Also

### Getting the Quality-of-Service Class
- [DispatchQoS.QoSClass.userInitiated](./userinitiated.md)
  The quality-of-service class for tasks that prevent the user from actively using your app.
- [DispatchQoS.QoSClass.default](./default.md)
  The default quality-of-service class.
- [DispatchQoS.QoSClass.utility](./utility.md)
  The quality-of-service class for tasks that the user does not track actively.
- [DispatchQoS.QoSClass.background](./background.md)
  The quality-of-service class for maintenance or cleanup tasks that you create.
- [DispatchQoS.QoSClass.unspecified](./unspecified.md)
  The absence of a quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqos/qosclass-swift.enum/userinteractive)*