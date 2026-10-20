# EKAuthorizationStatus.notDetermined

**Framework**: EventKit  
**Kind**: case  
**Role**: Case

The person hasn’t chosen whether the app may access the service.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case notDetermined
```

```c
EKAuthorizationStatusNotDetermined
```

## See Also

### Status
- [EKAuthorizationStatus.fullAccess](./fullaccess.md)
  The app has both read and write access to the requested entity type.
- [EKAuthorizationStatus.writeOnly](./writeonly.md)
  The app has write-only access to the requested entity type.
- [EKAuthorizationStatus.denied](./denied.md)
  The person explicitly denied access to the service for the app.
- [EKAuthorizationStatus.restricted](./restricted.md)
  The app isn’t authorized to access the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/notdetermined)*