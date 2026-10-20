# SAAuthorizationStatus.notDetermined

**Framework**: SafetyKit  
**Kind**: case  
**Role**: Case

There isn’t a designated app for receiving Crash Detection events.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 10.1+

## Declaration

```swift
case notDetermined
```

```c
SAAuthorizationStatusNotDetermined
```

## See Also

### Obtaining status
- [SAAuthorizationStatus.authorized](./authorized.md)
  This is the designated app for receiving Crash Detection events.
- [SAAuthorizationStatus.denied](./denied.md)
  The system denies the app from receiving Crash Detection events because another app has authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/saauthorizationstatus/notdetermined)*