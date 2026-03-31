# isSuppressedByFocus

**Framework**: Accessory Notifications  
**Kind**: property

A Boolean value that indicates whether the device’s Focus state suppresses notification alerts.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
var isSuppressedByFocus: Bool
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Discussion

A `true` value indicates that the notification attempts to alert the person, but the device’s active Focus state suppresses it.

## See Also

- [var shouldAlert: Bool](alertingcontext/shouldalert.md)
  A Boolean value that indicates the recommended alerting behavior.
- [var notificationCanAlert: Bool](alertingcontext/notificationcanalert.md)
  A Boolean value that indicates whether the accessory can alert the person for the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/alertingcontext/issuppressedbyfocus)*