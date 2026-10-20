# rawAuthenticatorData

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A byte sequence that contains additional information about the credential.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var rawAuthenticatorData: Data! { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * rawAuthenticatorData;
```

#### Discussion

This authenticator data object contains additional information about the credential. To learn more, see the [W3C Web Authentication specification](https://www.w3.org/TR/webauthn-2/#authenticator-data).

## See Also

### Getting the properties
- [var signature: Data!](./signature.md)
  The signature for the assertion.
- [var userID: Data!](./userid.md)
  A user identifier for the assertion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialassertion/rawauthenticatordata)*