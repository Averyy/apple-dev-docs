# requestAuthorization()

**Framework**: AlarmKit  
**Kind**: method

Requests permission to use the alarm system if it hasn’t been requested before.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func requestAuthorization() async throws -> AlarmManager.AuthorizationState
```

#### Discussion

If a person using your app denies authorization, all attempts to schedule alarms fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/requestauthorization())*