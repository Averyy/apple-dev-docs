# ENAuthorizationStatus

**Framework**: Exposure Notification  
**Kind**: enum

A set of cases that indicates the authorization status for the app.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
enum ENAuthorizationStatus
```

#### Overview

> ❗ **Important**:  This enumeration is available in iOS 12.5, and in iOS 13.5 and later.

## Topics

### Authorization States
- [ENAuthorizationStatus.authorized](enauthorizationstatus/authorized.md)
  Authorization is granted.
- [ENAuthorizationStatus.notAuthorized](enauthorizationstatus/notauthorized.md)
  Authorization is denied.
- [ENAuthorizationStatus.restricted](enauthorizationstatus/restricted.md)
  Authorization is restricted.
- [ENAuthorizationStatus.unknown](enauthorizationstatus/unknown.md)
  Authorization is not determined.
### Initializers
- [init?(rawValue: Int)](enauthorizationstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum ENStatus](enstatus.md)
  A set of cases that represents the overall status of exposure notification on the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enauthorizationstatus)*