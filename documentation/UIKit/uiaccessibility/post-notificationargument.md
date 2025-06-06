# post(notification:argument:)

**Framework**: UIKit  
**Kind**: method

Posts a notification to assistive apps.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
static func post(notification: UIAccessibility.Notification, argument: Any?)
```

#### Discussion

Your application might need to post accessibility notifications if you have user interface components that change very frequently or that appear and disappear.

## Parameters

- `notification`: The notification to post (see “Notifications” in   for a list of notifications).
- `argument`: The argument specified by the notification. Pass   unless a notification specifies otherwise.

## See Also

- [Notification names](notification-names.md)
  The names of notifications that the accessibility system generates.
- [Notification dictionary keys](notification-dictionary-keys.md)
  Handle notifications with keys in the user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/post(notification:argument:))*