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

### Operators
- [static func == (AuthorizationStatus, AuthorizationStatus) -> Bool](authorizationstatus/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [AuthorizationStatus.authorized](authorizationstatus/authorized.md)
  A person authorized the app to use FinanceKit services.
- [AuthorizationStatus.denied](authorizationstatus/denied.md)
  A person denied the use of FinanceKit services for the app.
- [AuthorizationStatus.notDetermined](authorizationstatus/notdetermined.md)
  A person has not chosen whether the app can use FinanceKit services.
### Initializers
- [init(from: any Decoder) throws](authorizationstatus/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](authorizationstatus/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](authorizationstatus/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](authorizationstatus/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](authorizationstatus/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func authorizationStatus() async throws -> AuthorizationStatus](financestore/authorizationstatus.md)
  Checks the authorization status for the calling application.
- [func requestAuthorization() async throws -> AuthorizationStatus](financestore/requestauthorization.md)
  Prompts a person to give FinanceKit authorization to access financial data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/authorizationstatus)*