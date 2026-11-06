# id

**Framework**: IdentityDocumentServices  
**Kind**: property  
**Role**: Instance Property

A property that identifies a query within the request.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
var id: String
```

## See Also

### Inspecting a credential query
- [var format: DigitalCredentialsQuery.CredentialFormat](./format.md)
  The format of the credential requested.
- [var multiple: Bool](./multiple.md)
  A Boolean that specifies whether more than one matching credential can be returned.
- [var meta: DigitalCredentialsQuery.Metadata](./meta.md)
  Format-specific constraints on the credential.
- [var trustedAuthorities: [DigitalCredentialsQuery.TrustedAuthoritiesQuery]](./trustedauthorities.md)
  Issuer authorities and trust frameworks the relying party accepts.
- [var requireCryptographicHolderBinding: Bool](./requirecryptographicholderbinding.md)
  A Boolean that specifies whether the relying party requires a cryptographic holder binding proof.
- [var claims: [DigitalCredentialsQuery.ClaimsQuery]](./claims.md)
  The claims being requested.
- [var claimSets: [Set<String>]](./claimsets.md)
  Combinations of claim identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/digitalcredentialsquery/credentialquery/id)*