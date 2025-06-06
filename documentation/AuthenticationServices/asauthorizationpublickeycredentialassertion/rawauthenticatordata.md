# rawAuthenticatorData

**Framework**: Authentication Services  
**Kind**: property  
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

#### Discussion

This authenticator data object contains additional information about the credential. To learn more, see the [`W3C Web Authentication specification`](https://developer.apple.comhttps://www.w3.org/TR/webauthn-2/#authenticator-data).

## See Also

- [var signature: Data!](asauthorizationpublickeycredentialassertion/signature.md)
  The signature for the assertion.
- [var userID: Data!](asauthorizationpublickeycredentialassertion/userid.md)
  A user identifier for the assertion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialassertion/rawauthenticatordata)*