# ActivityAuthorizationError.unsupportedTarget

**Framework**: ActivityKit  
**Kind**: case

The app doesn’t have the required entitlement to start a Live Activities.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
case unsupportedTarget
```

## See Also

- [ActivityAuthorizationError.attributesTooLarge](activityauthorizationerror/attributestoolarge.md)
  The provided Live Activity attributes exceeded the maximum size of 4KB.
- [ActivityAuthorizationError.denied](activityauthorizationerror/denied.md)
  A person deactivated Live Activities in Settings.
- [ActivityAuthorizationError.globalMaximumExceeded](activityauthorizationerror/globalmaximumexceeded.md)
  The device reached the maximum number of ongoing Live Activities.
- [ActivityAuthorizationError.malformedActivityIdentifier](activityauthorizationerror/malformedactivityidentifier.md)
  The provided activity identifier is malformed.
- [ActivityAuthorizationError.missingProcessIdentifier](activityauthorizationerror/missingprocessidentifier.md)
  The process that tried to start the Live Activity is missing a process identifier.
- [ActivityAuthorizationError.persistenceFailure](activityauthorizationerror/persistencefailure.md)
  The system couldn’t persist the Live Activity.
- [ActivityAuthorizationError.reconnectNotPermitted](activityauthorizationerror/reconnectnotpermitted.md)
  The process that tried to recreate the Live Activity is not the process that originally created the Live Activity.
- [ActivityAuthorizationError.targetMaximumExceeded](activityauthorizationerror/targetmaximumexceeded.md)
  The app has already started the maximum number of concurrent Live Activities.
- [ActivityAuthorizationError.unentitled](activityauthorizationerror/unentitled.md)
  The app doesn’t have the required entitlement to start a Live Activity.
- [ActivityAuthorizationError.unsupported](activityauthorizationerror/unsupported.md)
  The device doesn’t support Live Activities.
- [ActivityAuthorizationError.visibility](activityauthorizationerror/visibility.md)
  The app tried to start the Live Activity while it was in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityauthorizationerror/unsupportedtarget)*