# verifiableCredentialTypes

**Framework**: IdentityDocumentServices  
**Kind**: property  
**Role**: Instance Property

The verifiable credential types that the registered credential can satisfy.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
var verifiableCredentialTypes: [String]
```

## See Also

### Inspecting a registration
- [var supportedIssuerKeyIdentifiers: [Data]](./supportedissuerkeyidentifiers.md)
  A list of X.509 authority key identifiers that correspond to the issuer certificate chain for the verifiable credential.
- [var supportedAuthorityKeyIdentifiers: [Data]](./supportedauthoritykeyidentifiers.md)
  A list of authority key identifiers that correspond to relying party authorizers that your app trusts.
- [var invalidationDate: Date?](./invalidationdate.md)
  A date that indicates when the registration should be invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/verifiablecredentialregistration/verifiablecredentialtypes)*