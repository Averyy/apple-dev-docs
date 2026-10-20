# background

**Framework**: Dispatch  
**Kind**: property  
**Role**: Type Property

The quality-of-service class for maintenance or cleanup tasks that you create.

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
static let background: DispatchQoS
```

#### Discussion

Background tasks have the lowest priority of all tasks. Assign this class to tasks or dispatch queues that you use to perform work while your app is running in the background.

## See Also

### Getting the Predefined QoS Objects
- [static let userInteractive: DispatchQoS](./userinteractive.md)
  The quality-of-service class for user-interactive tasks, such as animations, event handling, or updates to your app’s user interface.
- [static let userInitiated: DispatchQoS](./userinitiated.md)
  The quality-of-service class for tasks that prevent the user from actively using your app.
- [static let `default`: DispatchQoS](./default.md)
  The default quality-of-service class.
- [static let utility: DispatchQoS](./utility.md)
  The quality-of-service class for tasks that the user does not track actively.
- [static let unspecified: DispatchQoS](./unspecified.md)
  The absence of a quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqos/background)*