# init(prefix:identifier:certificateChain:)

**Framework**: IdentityDocumentServices  
**Kind**: init  
**Role**: Initializer

Initializes a request authentication.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
init(prefix: OpenID4VPRequest.ClientIdentifierPrefix?, identifier: String, certificateChain: [SecCertificate])
```

## Parameters

- `prefix`: The prefix that determines the method for establishing the relying party’s identity.
- `identifier`: The identifier for the relying party within the namespace of the prefix, when one is present.
- `certificateChain`: The certificate chain that the request presents for the identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/openid4vprequest/requestauthentication/init(prefix:identifier:certificatechain:))*