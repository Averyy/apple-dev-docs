# default

**Framework**: Dispatch  
**Kind**: property  
**Role**: Type Property

The default quality-of-service class.

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
static let `default`: DispatchQoS
```

## Discussion

Default tasks have a lower priority than user-initiated and user-interactive tasks, but a higher priority than utility and background tasks. Assign this class to tasks or queues that your app initiates or uses to perform active work on the user’s behalf.

## See Also

### Getting the Predefined QoS Objects
- [static let userInteractive: DispatchQoS](./userinteractive.md)
  The quality-of-service class for user-interactive tasks, such as animations, event handling, or updates to your app’s user interface.
- [static let userInitiated: DispatchQoS](./userinitiated.md)
  The quality-of-service class for tasks that prevent the user from actively using your app.
- [static let utility: DispatchQoS](./utility.md)
  The quality-of-service class for tasks that the user does not track actively.
- [static let background: DispatchQoS](./background.md)
  The quality-of-service class for maintenance or cleanup tasks that you create.
- [static let unspecified: DispatchQoS](./unspecified.md)
  The absence of a quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqos/default)*