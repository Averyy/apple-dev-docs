# DispatchQoS.QoSClass.utility

**Framework**: Dispatch  
**Kind**: case

The quality-of-service class for tasks that the user does not track actively.

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
case utility
```

#### Discussion

Utility tasks have a lower priority than default, user-initiated, and user-interactive tasks, but a higher priority than background tasks. Assign this quality-of-service class to tasks that do not prevent the user from continuing to use your app. For example, you might assign this class to long-running tasks whose progress the user does not follow actively.

## See Also

- [DispatchQoS.QoSClass.userInteractive](dispatchqos/qosclass-swift.enum/userinteractive.md)
  The quality-of-service class for user-interactive tasks, such as animations, event handling, or updating your app’s user interface.
- [DispatchQoS.QoSClass.userInitiated](dispatchqos/qosclass-swift.enum/userinitiated.md)
  The quality-of-service class for tasks that prevent the user from actively using your app.
- [DispatchQoS.QoSClass.default](dispatchqos/qosclass-swift.enum/default.md)
  The default quality-of-service class.
- [DispatchQoS.QoSClass.background](dispatchqos/qosclass-swift.enum/background.md)
  The quality-of-service class for maintenance or cleanup tasks that you create.
- [DispatchQoS.QoSClass.unspecified](dispatchqos/qosclass-swift.enum/unspecified.md)
  The absence of a quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqos/qosclass-swift.enum/utility)*