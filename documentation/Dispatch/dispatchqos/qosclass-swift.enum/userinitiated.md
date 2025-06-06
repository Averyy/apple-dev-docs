# DispatchQoS.QoSClass.userInitiated

**Framework**: Dispatch  
**Kind**: case

The quality-of-service class for tasks that prevent the user from actively using your app.

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
case userInitiated
```

#### Discussion

User-initiated tasks are second only to user-interactive tasks in their priority on the system. Assign this class to tasks that provide immediate results for something the user is doing, or that would prevent the user from using your app. For example, you might use this quality-of-service class to load the content of an email that you want to display to the user.

## See Also

- [DispatchQoS.QoSClass.userInteractive](dispatchqos/qosclass-swift.enum/userinteractive.md)
  The quality-of-service class for user-interactive tasks, such as animations, event handling, or updating your app’s user interface.
- [DispatchQoS.QoSClass.default](dispatchqos/qosclass-swift.enum/default.md)
  The default quality-of-service class.
- [DispatchQoS.QoSClass.utility](dispatchqos/qosclass-swift.enum/utility.md)
  The quality-of-service class for tasks that the user does not track actively.
- [DispatchQoS.QoSClass.background](dispatchqos/qosclass-swift.enum/background.md)
  The quality-of-service class for maintenance or cleanup tasks that you create.
- [DispatchQoS.QoSClass.unspecified](dispatchqos/qosclass-swift.enum/unspecified.md)
  The absence of a quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqos/qosclass-swift.enum/userinitiated)*