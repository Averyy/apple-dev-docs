# supportedIssuerKeyIdentifiers

**Framework**: IdentityDocumentServices  
**Kind**: property  
**Role**: Instance Property

A list of X.509 authority key identifiers that correspond to the issuer certificate chain for the verifiable credential.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
var supportedIssuerKeyIdentifiers: [Data]
```

## Discussion

The number of issuer key identifiers must not exceed 1,000, and the size of each identifier must not exceed 64 bytes.

## See Also

### Inspecting a registration
- [var verifiableCredentialTypes: [String]](./verifiablecredentialtypes.md)
  The verifiable credential types that the registered credential can satisfy.
- [var supportedAuthorityKeyIdentifiers: [Data]](./supportedauthoritykeyidentifiers.md)
  A list of authority key identifiers that correspond to relying party authorizers that your app trusts.
- [var invalidationDate: Date?](./invalidationdate.md)
  A date that indicates when the registration should be invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/verifiablecredentialregistration/supportedissuerkeyidentifiers)*