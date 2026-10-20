# EKAuthorizationStatus.fullAccess

**Framework**: EventKit  
**Kind**: case  
**Role**: Case

The app has both read and write access to the requested entity type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case fullAccess
```

```c
EKAuthorizationStatusFullAccess
```

## See Also

### Status
- [EKAuthorizationStatus.writeOnly](./writeonly.md)
  The app has write-only access to the requested entity type.
- [EKAuthorizationStatus.denied](./denied.md)
  The person explicitly denied access to the service for the app.
- [EKAuthorizationStatus.notDetermined](./notdetermined.md)
  The person hasn’t chosen whether the app may access the service.
- [EKAuthorizationStatus.restricted](./restricted.md)
  The app isn’t authorized to access the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/fullaccess)*