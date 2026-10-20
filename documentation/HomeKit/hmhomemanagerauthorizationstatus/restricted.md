# restricted

**Framework**: HomeKit  
**Kind**: property  
**Role**: Type Property

The app doesn’t have access to home data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static var restricted: HMHomeManagerAuthorizationStatus { get }
```

```c
HMHomeManagerAuthorizationStatusRestricted
```

## See Also

### Recognizing Status Values
- [static var determined: HMHomeManagerAuthorizationStatus](./determined.md)
  The user has set the app’s level of access to home data.
- [static var authorized: HMHomeManagerAuthorizationStatus](./authorized.md)
  The app has access to home data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanagerauthorizationstatus/restricted)*