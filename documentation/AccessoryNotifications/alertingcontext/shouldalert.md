# shouldAlert

**Framework**: Accessory Notifications  
**Kind**: property

A Boolean value that indicates the recommended alerting behavior.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
var shouldAlert: Bool { get }
```

#### Discussion

Use this property to closely match the iPhone’s alerting behavior. The system sets this value based on notification settings, device Focus state, and other alerting factors.

## See Also

- [var notificationCanAlert: Bool](alertingcontext/notificationcanalert.md)
  A Boolean value that indicates whether the accessory can alert the person for the notification.
- [var isSuppressedByFocus: Bool](alertingcontext/issuppressedbyfocus.md)
  A Boolean value that indicates whether the device’s Focus state suppresses notification alerts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/alertingcontext/shouldalert)*