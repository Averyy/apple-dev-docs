# invalidationDate

**Framework**: IdentityDocumentServices  
**Kind**: property  
**Role**: Instance Property

A date that indicates when the registration should be invalidated.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
var invalidationDate: Date?
```

## Discussion

Use this date in scenarios in which the expiration time period of a credential is known. If the value is `nil`, the registration doesn’t expire.

## See Also

### Inspecting a registration
- [var verifiableCredentialTypes: [String]](./verifiablecredentialtypes.md)
  The verifiable credential types that the registered credential can satisfy.
- [var supportedIssuerKeyIdentifiers: [Data]](./supportedissuerkeyidentifiers.md)
  A list of X.509 authority key identifiers that correspond to the issuer certificate chain for the verifiable credential.
- [var supportedAuthorityKeyIdentifiers: [Data]](./supportedauthoritykeyidentifiers.md)
  A list of authority key identifiers that correspond to relying party authorizers that your app trusts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/verifiablecredentialregistration/invalidationdate)*