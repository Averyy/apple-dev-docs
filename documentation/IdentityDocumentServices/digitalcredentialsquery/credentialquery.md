# DigitalCredentialsQuery.CredentialQuery

**Framework**: IdentityDocumentServices  
**Kind**: struct  
**Role**: Structure

A request for a single credential.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
struct CredentialQuery
```

## Topics

### Creating a credential query
- [init(id: String, format: DigitalCredentialsQuery.CredentialFormat, multiple: Bool, meta: DigitalCredentialsQuery.Metadata, trustedAuthorities: [DigitalCredentialsQuery.TrustedAuthoritiesQuery], requireCryptographicHolderBinding: Bool, claims: [DigitalCredentialsQuery.ClaimsQuery], claimSets: [Set<String>])](./credentialquery/init%28id,format,multiple,meta,trustedauthorities,requirecryptographicholderbinding,claims,claimsets%29.md)
  Initializes a credential query.
### Inspecting a credential query
- [var id: String](./credentialquery/id.md)
  A property that identifies a query within the request.
- [var format: DigitalCredentialsQuery.CredentialFormat](./credentialquery/format.md)
  The format of the credential requested.
- [var multiple: Bool](./credentialquery/multiple.md)
  A Boolean that specifies whether more than one matching credential can be returned.
- [var meta: DigitalCredentialsQuery.Metadata](./credentialquery/meta.md)
  Format-specific constraints on the credential.
- [var trustedAuthorities: [DigitalCredentialsQuery.TrustedAuthoritiesQuery]](./credentialquery/trustedauthorities.md)
  Issuer authorities and trust frameworks the relying party accepts.
- [var requireCryptographicHolderBinding: Bool](./credentialquery/requirecryptographicholderbinding.md)
  A Boolean that specifies whether the relying party requires a cryptographic holder binding proof.
- [var claims: [DigitalCredentialsQuery.ClaimsQuery]](./credentialquery/claims.md)
  The claims being requested.
- [var claimSets: [Set<String>]](./credentialquery/claimsets.md)
  Combinations of claim identifiers.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Describing credentials
- [DigitalCredentialsQuery.CredentialFormat](./credentialformat.md)
  The format of a requested credential.
- [DigitalCredentialsQuery.Metadata](./metadata.md)
  Format-specific constraints on a requested credential.
- [DigitalCredentialsQuery.CredentialSetQuery](./credentialsetquery.md)
  A grouping of credentials that satisfies part of a query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/digitalcredentialsquery/credentialquery)*