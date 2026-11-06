# supportedAuthorityKeyIdentifiers

**Framework**: IdentityDocumentServices  
**Kind**: property  
**Role**: Instance Property

A list of authority key identifiers that correspond to relying party authorizers that your app trusts.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
var supportedAuthorityKeyIdentifiers: [Data]
```

## Discussion

A relying party that’s authorized by an authority listed in your `supportedAuthorityKeyIdentifiers` can receive the credential during a presentment. An empty list applies no authority filtering, which is how an app serves relying parties whose identity isn’t established through an X.509 certificate chain.

## See Also

### Inspecting a registration
- [var verifiableCredentialTypes: [String]](./verifiablecredentialtypes.md)
  The verifiable credential types that the registered credential can satisfy.
- [var supportedIssuerKeyIdentifiers: [Data]](./supportedissuerkeyidentifiers.md)
  A list of X.509 authority key identifiers that correspond to the issuer certificate chain for the verifiable credential.
- [var invalidationDate: Date?](./invalidationdate.md)
  A date that indicates when the registration should be invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/verifiablecredentialregistration/supportedauthoritykeyidentifiers)*