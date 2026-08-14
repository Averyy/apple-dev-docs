# AuthorizationStatus

**Framework**: FinanceKit  
**Kind**: enum

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum AuthorizationStatus
```

## Topics

### Enumeration Cases
- [AuthorizationStatus.authorized](authorizationstatus/authorized.md)
  A person authorized the app to use FinanceKit services.
- [AuthorizationStatus.denied](authorizationstatus/denied.md)
  A person denied the use of FinanceKit services for the app.
- [AuthorizationStatus.notDetermined](authorizationstatus/notdetermined.md)
  A person has not chosen whether the app can use FinanceKit services.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func authorizationStatus() async throws -> AuthorizationStatus](financestore/authorizationstatus.md)
  Checks the authorization status for the calling application.
- [func requestAuthorization() async throws -> AuthorizationStatus](financestore/requestauthorization.md)
  Prompts a person to give FinanceKit authorization to access financial data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/authorizationstatus)*