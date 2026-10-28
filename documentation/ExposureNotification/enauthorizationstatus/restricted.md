# ENAuthorizationStatus.restricted

**Framework**: Exposure Notification  
**Kind**: case  
**Role**: Case

Authorization is restricted.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
case restricted
```

```c
ENAuthorizationStatusRestricted
```

## Discussion

The user cannot change the app’s authorization status. This status may be due to active restrictions, such as parental controls.

## See Also

### Authorization States
- [ENAuthorizationStatus.authorized](./authorized.md)
  Authorization is granted.
- [ENAuthorizationStatus.notAuthorized](./notauthorized.md)
  Authorization is denied.
- [ENAuthorizationStatus.unknown](./unknown.md)
  Authorization is not determined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enauthorizationstatus/restricted)*