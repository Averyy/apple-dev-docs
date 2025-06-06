# DispatchQoS.QoSClass.default

**Framework**: Dispatch  
**Kind**: case

The default quality-of-service class.

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
case `default`
```

#### Discussion

Default tasks have a lower priority than user-initiated and user-interactive tasks, but a higher priority than utility and background tasks. Assign this class to tasks or queues that your app initiates or uses to perform active work on the user’s behalf.

## See Also

- [DispatchQoS.QoSClass.userInteractive](dispatchqos/qosclass-swift.enum/userinteractive.md)
  The quality-of-service class for user-interactive tasks, such as animations, event handling, or updating your app’s user interface.
- [DispatchQoS.QoSClass.userInitiated](dispatchqos/qosclass-swift.enum/userinitiated.md)
  The quality-of-service class for tasks that prevent the user from actively using your app.
- [DispatchQoS.QoSClass.utility](dispatchqos/qosclass-swift.enum/utility.md)
  The quality-of-service class for tasks that the user does not track actively.
- [DispatchQoS.QoSClass.background](dispatchqos/qosclass-swift.enum/background.md)
  The quality-of-service class for maintenance or cleanup tasks that you create.
- [DispatchQoS.QoSClass.unspecified](dispatchqos/qosclass-swift.enum/unspecified.md)
  The absence of a quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqos/qosclass-swift.enum/default)*