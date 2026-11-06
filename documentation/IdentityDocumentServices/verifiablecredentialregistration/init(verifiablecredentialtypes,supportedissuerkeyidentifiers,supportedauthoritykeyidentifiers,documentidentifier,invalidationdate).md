# init(verifiableCredentialTypes:supportedIssuerKeyIdentifiers:supportedAuthorityKeyIdentifiers:documentIdentifier:invalidationDate:)

**Framework**: IdentityDocumentServices  
**Kind**: init  
**Role**: Initializer

Initializes a verifiable credential registration.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
init(verifiableCredentialTypes: [String], supportedIssuerKeyIdentifiers: [Data] = [], supportedAuthorityKeyIdentifiers: [Data], documentIdentifier: String = UUID().uuidString, invalidationDate: Date? = nil)
```

## Parameters

- `verifiableCredentialTypes`: The verifiable credential types that the registered credential can satisfy.
- `supportedIssuerKeyIdentifiers`: A list of X.509 authority key identifiers that correspond to the issuer certificate chain for the verifiable credential.
- `supportedAuthorityKeyIdentifiers`: A list of authority key identifiers that correspond to relying party authorizers that your app trusts.
- `documentIdentifier`: An identifier that uniquely refers to the registered credential.
- `invalidationDate`: A date that indicates when the registration should be invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/verifiablecredentialregistration/init(verifiablecredentialtypes:supportedissuerkeyidentifiers:supportedauthoritykeyidentifiers:documentidentifier:invalidationdate:))*