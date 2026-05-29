# init(notificationCanAlert:suppressedByFocus:kind:sound:)

**Framework**: Accessory Notifications  
**Kind**: init

Initializes an alerting context with notification alert conditions.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
init(notificationCanAlert: Bool = false, suppressedByFocus: Bool = false, kind: AlertingContext.Kind = .notification, sound: AlertingContext.Sound? = nil)
```

## Parameters

- `notificationCanAlert`: A Boolean value that indicates whether the notification can alert.
- `suppressedByFocus`: A Boolean value that indicates whether Focus suppresses the alert.
- `kind`: The classification for the notification type.
- `sound`: An optional sound configuration for the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/alertingcontext/init(notificationcanalert:suppressedbyfocus:kind:sound:))*