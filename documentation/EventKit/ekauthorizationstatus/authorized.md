# authorized

**Framework**: EventKit  
**Kind**: property  
**Role**: Type Property

The app can access the service.

**Availability**:
- iOS 6.0+ - Deprecated in 17.0
- iPadOS 6.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 10.0

> **Deprecated**: This value is deprecated. Check for the level of access ([`EKAuthorizationStatus.writeOnly`](./writeonly.md) or [`EKAuthorizationStatus.fullAccess`](./fullaccess.md)) your app needs.

## Declaration

```swift
static var authorized: EKAuthorizationStatus { get }
```

```c
EKAuthorizationStatusAuthorized
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus/authorized)*