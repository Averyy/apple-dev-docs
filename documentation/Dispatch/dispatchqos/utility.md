# utility

**Framework**: Dispatch  
**Kind**: property

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
static let utility: DispatchQoS
```

#### Discussion

Utility tasks have a lower priority than default, user-initiated, and user-interactive tasks, but a higher priority than background tasks. Assign this quality-of-service class to tasks that do not prevent the user from continuing to use your app. For example, you might assign this class to long-running tasks whose progress the user does not follow actively.

## See Also

- [static let userInteractive: DispatchQoS](dispatchqos/userinteractive.md)
  The quality-of-service class for user-interactive tasks, such as animations, event handling, or updates to your app’s user interface.
- [static let userInitiated: DispatchQoS](dispatchqos/userinitiated.md)
  The quality-of-service class for tasks that prevent the user from actively using your app.
- [static let `default`: DispatchQoS](dispatchqos/default.md)
  The default quality-of-service class.
- [static let background: DispatchQoS](dispatchqos/background.md)
  The quality-of-service class for maintenance or cleanup tasks that you create.
- [static let unspecified: DispatchQoS](dispatchqos/unspecified.md)
  The absence of a quality-of-service class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqos/utility)*