# ENAuthorizationStatus

**Framework**: Exposure Notification  
**Kind**: enum  
**Role**: Enumeration

A set of cases that indicates the authorization status for the app.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
enum ENAuthorizationStatus
```

```c
enum ENAuthorizationStatus : NSInteger;
```

## Overview

> ❗ **Important**:  This enumeration is available in iOS 12.5, and in iOS 13.5 and later.

## Topics

### Authorization States
- [ENAuthorizationStatus.authorized](./enauthorizationstatus/authorized.md)
  Authorization is granted.
- [ENAuthorizationStatus.notAuthorized](./enauthorizationstatus/notauthorized.md)
  Authorization is denied.
- [ENAuthorizationStatus.restricted](./enauthorizationstatus/restricted.md)
  Authorization is restricted.
- [ENAuthorizationStatus.unknown](./enauthorizationstatus/unknown.md)
  Authorization is not determined.
### Initializers
- [init?(rawValue: Int)](./enauthorizationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Status
- [enum ENStatus](./enstatus.md)
  A set of cases that represents the overall status of exposure notification on the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enauthorizationstatus)*