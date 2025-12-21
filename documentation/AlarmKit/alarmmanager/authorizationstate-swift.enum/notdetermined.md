# AlarmManager.AuthorizationState.notDetermined

**Framework**: AlarmKit  
**Kind**: case

The client hasn’t requested authorization from a person.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
case notDetermined
```

#### Discussion

If you attempt to schedule an alarm when the authorization system is in this state, the system prompts the person to allow or deny the alarm.

## See Also

- [AlarmManager.AuthorizationState.authorized](alarmmanager/authorizationstate-swift.enum/authorized.md)
  The person authorized the client to use alarms and timers.
- [AlarmManager.AuthorizationState.denied](alarmmanager/authorizationstate-swift.enum/denied.md)
  The client previously requested authorization from the person, but they declined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/authorizationstate-swift.enum/notdetermined)*