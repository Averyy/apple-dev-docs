# EKAuthorizationStatus.restricted

**Framework**: EventKit  
**Kind**: case  
**Role**: Case

The app isn’t authorized to access the service.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case restricted
```

```c
EKAuthorizationStatusRestricted
```

#### Discussion

The person can’t change your app’s authorization status, possibly due to active restrictions such as parental controls being in place.

## See Also

### Status
- [EKAuthorizationStatus.fullAccess](./fullaccess.md)
  The app has both read and write access to the requested entity type.
- [EKAuthorizationStatus.writeOnly](./writeonly.md)
  The app has write-only access to the requested entity type.
- [EKAuthorizationStatus.denied](./denied.md)
  The person explicitly denied access to the service for the app.
- [EKAuthorizationStatus.notDetermined](./notdetermined.md)
  The person hasn’t chosen whether the app may access the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/restricted)*