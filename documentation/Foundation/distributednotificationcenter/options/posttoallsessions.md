# postToAllSessions

**Framework**: Foundation  
**Kind**: property

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var postToAllSessions: DistributedNotificationCenter.Options { get }
```

## See Also

- [let NSNotificationDeliverImmediately: DistributedNotificationCenter.Options](nsnotificationdeliverimmediately.md)
  When set, the notification is delivered immediately to all observers, regardless of their suspension behavior or suspension state. When not set, allows the normal suspension behavior of notification observers to take place.
- [static var deliverImmediately: DistributedNotificationCenter.Options](distributednotificationcenter/options/deliverimmediately.md)
- [let NSNotificationPostToAllSessions: DistributedNotificationCenter.Options](nsnotificationposttoallsessions.md)
  When set, the notification is posted to all sessions. When not set, the notification is sent only to applications within the same login session as the posting task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/options/posttoallsessions)*