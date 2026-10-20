# SAAuthorizationStatus.denied

**Framework**: SafetyKit  
**Kind**: case  
**Role**: Case

The system denies the app from receiving Crash Detection events because another app has authorization.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 10.1+

## Declaration

```swift
case denied
```

```c
SAAuthorizationStatusDenied
```

## See Also

### Obtaining status
- [SAAuthorizationStatus.authorized](./authorized.md)
  This is the designated app for receiving Crash Detection events.
- [SAAuthorizationStatus.notDetermined](./notdetermined.md)
  There isn’t a designated app for receiving Crash Detection events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/saauthorizationstatus/denied)*