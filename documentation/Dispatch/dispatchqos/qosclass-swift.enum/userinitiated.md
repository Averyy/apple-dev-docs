# DispatchQoS.QoSClass.userInitiated

**Framework**: Dispatch  
**Kind**: case  
**Role**: Case

The quality-of-service class for tasks that prevent the user from actively using your app.

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
case userInitiated
```

## Discussion

User-initiated tasks are second only to user-interactive tasks in their priority on the system. Assign this class to tasks that provide immediate results for something the user is doing, or that would prevent the user from using your app. For example, you might use this quality-of-service class to load the content of an email that you want to display to the user.

## See Also

### Getting the Quality-of-Service Class
- [DispatchQoS.QoSClass.userInteractive](./userinteractive.md)
  The quality-of-service class for user-interactive tasks, such as animations, event handling, or updating your app’s user interface.
- [DispatchQoS.QoSClass.default](./default.md)
  The default quality-of-service class.
- [DispatchQoS.QoSClass.utility](./utility.md)
  The quality-of-service class for tasks that the user does not track actively.
- [DispatchQoS.QoSClass.background](./background.md)
  The quality-of-service class for maintenance or cleanup tasks that you create.
- [DispatchQoS.QoSClass.unspecified](./unspecified.md)
  The absence of a quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqos/qosclass-swift.enum/userinitiated)*