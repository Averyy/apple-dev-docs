# INSiriAuthorizationStatus.restricted

**Framework**: Intents  
**Kind**: case  
**Role**: Case

Restricted. The app is not authorized to use Siri services. This status could be the result of active restrictions on Siri services rather than on the user denying access.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case restricted
```

```c
INSiriAuthorizationStatusRestricted
```

## See Also

### Constants
- [INSiriAuthorizationStatus.notDetermined](./notdetermined.md)
  Not yet determined. An authorization request has not yet been made or the user has not yet made a choice regarding the status of the app. Call the [`requestSiriAuthorization(_:)`](../inpreferences/requestsiriauthorization%28_%29.md) method to request authorization from the user.
- [INSiriAuthorizationStatus.denied](./denied.md)
  Not authorized. The user explicitly denied authorization for this app.
- [INSiriAuthorizationStatus.authorized](./authorized.md)
  Authorized. Siri is enabled and your app is authorized to interact with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insiriauthorizationstatus/restricted)*