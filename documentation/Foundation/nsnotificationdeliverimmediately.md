# NSNotificationDeliverImmediately

**Framework**: Foundation  
**Kind**: var

When set, the notification is delivered immediately to all observers, regardless of their suspension behavior or suspension state. When not set, allows the normal suspension behavior of notification observers to take place.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let NSNotificationDeliverImmediately: DistributedNotificationCenter.Options
```

## See Also

- [static var deliverImmediately: DistributedNotificationCenter.Options](distributednotificationcenter/options/deliverimmediately.md)
- [let NSNotificationPostToAllSessions: DistributedNotificationCenter.Options](nsnotificationposttoallsessions.md)
  When set, the notification is posted to all sessions. When not set, the notification is sent only to applications within the same login session as the posting task.
- [static var postToAllSessions: DistributedNotificationCenter.Options](distributednotificationcenter/options/posttoallsessions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotificationdeliverimmediately)*