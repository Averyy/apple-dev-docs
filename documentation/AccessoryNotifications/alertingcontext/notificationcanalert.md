# notificationCanAlert

**Framework**: Accessory Notifications  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the accessory can alert the person for the notification.

**Availability**:
- iOS 26.5+

## Declaration

```swift
var notificationCanAlert: Bool
```

## Discussion

A `true` value indicates that the notification includes sound and alert permissions, and the person allows alerts. The system might set this property to `false` if the notification already alerted on another device or if device settings disable alerting for the notification. This property doesn’t account for Focus state; see [`isSuppressedByFocus`](./issuppressedbyfocus.md) and [`shouldAlert`](./shouldalert.md).

## See Also

### Determining alerting behavior
- [var shouldAlert: Bool](./shouldalert.md)
  A Boolean value that indicates the recommended alerting behavior.
- [var isSuppressedByFocus: Bool](./issuppressedbyfocus.md)
  A Boolean value that indicates whether the device’s Focus state suppresses notification alerts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/alertingcontext/notificationcanalert)*