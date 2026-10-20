# authorized

**Framework**: HomeKit  
**Kind**: property  
**Role**: Type Property

The app has access to home data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static var authorized: HMHomeManagerAuthorizationStatus { get }
```

```c
HMHomeManagerAuthorizationStatusAuthorized
```

## See Also

### Recognizing Status Values
- [static var determined: HMHomeManagerAuthorizationStatus](./determined.md)
  The user has set the app’s level of access to home data.
- [static var restricted: HMHomeManagerAuthorizationStatus](./restricted.md)
  The app doesn’t have access to home data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanagerauthorizationstatus/authorized)*