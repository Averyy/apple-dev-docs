# userInteractive

**Framework**: Dispatch  
**Kind**: property

The quality-of-service class for user-interactive tasks, such as animations, event handling, or updates to your app’s user interface.

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
static let userInteractive: DispatchQoS
```

#### Discussion

User-interactive tasks have the highest priority on the system. Use this class for tasks or queues that interact with the user or actively update your app’s user interface. For example, use this class for animations or for tracking events interactively.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqos/userinteractive)*