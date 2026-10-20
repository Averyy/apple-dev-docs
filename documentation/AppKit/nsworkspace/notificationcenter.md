# notificationCenter

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The notification center for workspace notifications.

**Availability**:
- macOS

## Declaration

```swift
var notificationCenter: NotificationCenter { get }
```

```objc
@property (strong, readonly) NSNotificationCenter * notificationCenter;
```

#### Return Value

The notification center object associated with the workspace

#### Discussion

This notification center object delivers the workspace-related notifications described in Responding to Environment Notifications.

You can access this object safely from any thread in your app in macOS 10.6 and later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/notificationcenter)*