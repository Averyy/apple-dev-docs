# isSuppressedByFocus

**Framework**: Accessory Notifications  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the device’s Focus state suppresses notification alerts.

**Availability**:
- iOS 26.5+

## Declaration

```swift
var isSuppressedByFocus: Bool { get }
```

## Discussion

A `true` value indicates that the notification attempts to alert the person, but the device’s active Focus state suppresses it.

## See Also

### Determining alerting behavior
- [var shouldAlert: Bool](./shouldalert.md)
  A Boolean value that indicates the recommended alerting behavior.
- [var notificationCanAlert: Bool](./notificationcanalert.md)
  A Boolean value that indicates whether the accessory can alert the person for the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/alertingcontext/issuppressedbyfocus)*