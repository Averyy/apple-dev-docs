# INSiriAuthorizationStatus

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the authorization status of your Intents extension.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INSiriAuthorizationStatus
```

```c
enum INSiriAuthorizationStatus : NSInteger;
```

## Topics

### Constants
- [INSiriAuthorizationStatus.notDetermined](./insiriauthorizationstatus/notdetermined.md)
  Not yet determined. An authorization request has not yet been made or the user has not yet made a choice regarding the status of the app. Call the [`requestSiriAuthorization(_:)`](./inpreferences/requestsiriauthorization%28_%29.md) method to request authorization from the user.
- [INSiriAuthorizationStatus.restricted](./insiriauthorizationstatus/restricted.md)
  Restricted. The app is not authorized to use Siri services. This status could be the result of active restrictions on Siri services rather than on the user denying access.
- [INSiriAuthorizationStatus.denied](./insiriauthorizationstatus/denied.md)
  Not authorized. The user explicitly denied authorization for this app.
- [INSiriAuthorizationStatus.authorized](./insiriauthorizationstatus/authorized.md)
  Authorized. Siri is enabled and your app is authorized to interact with it.
### Initializers
- [init?(rawValue: Int)](./insiriauthorizationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Authorization
- [Requesting Authorization to Use Siri](../SiriKit/requesting-authorization-to-use-siri.md)
  Request permission from the user for Siri and Maps to communicate with your app or Intents app extension.
- [Siri Entitlement](../BundleResources/entitlements/com.apple.developer.siri.md)
  A Boolean value that indicates whether the app handles Siri requests.
- [class INPreferences](./inpreferences.md)
  The preferences and authorization related to using SiriKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insiriauthorizationstatus)*