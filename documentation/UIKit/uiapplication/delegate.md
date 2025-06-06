# delegate

**Framework**: UIKit  
**Kind**: property

The delegate of the app object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
unowned(unsafe) var delegate: (any UIApplicationDelegate)? { get set }
```

#### Discussion

Every app must have an app delegate object to respond to app-related messages. For example, the app notifies its delegate when the app finishes launching and when its foreground or background execution status changes. Similarly, app-related messages coming from the system are often routed to the app delegate for handling. Xcode provides an initial app delegate for every app and you should not need to change this delegate later.

The delegate must adopt the [`UIApplicationDelegate`](uiapplicationdelegate.md) formal protocol.

## See Also

- [protocol UIApplicationDelegate](uiapplicationdelegate.md)
  A set of methods to manage shared behaviors for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/delegate)*