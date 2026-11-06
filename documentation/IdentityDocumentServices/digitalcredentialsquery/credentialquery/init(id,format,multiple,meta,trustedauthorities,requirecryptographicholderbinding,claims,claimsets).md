# init(id:format:multiple:meta:trustedAuthorities:requireCryptographicHolderBinding:claims:claimSets:)

**Framework**: IdentityDocumentServices  
**Kind**: init  
**Role**: Initializer

Initializes a credential query.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
init(id: String, format: DigitalCredentialsQuery.CredentialFormat, multiple: Bool = false, meta: DigitalCredentialsQuery.Metadata, trustedAuthorities: [DigitalCredentialsQuery.TrustedAuthoritiesQuery] = [], requireCryptographicHolderBinding: Bool = true, claims: [DigitalCredentialsQuery.ClaimsQuery] = [], claimSets: [Set<String>] = [])
```

## Parameters

- `id`: A property that identifies a query within the request.
- `format`: The format of the credential requested.
- `multiple`: A Boolean that specifies whether more than one matching credential may be returned.
- `meta`: Format-specific constraints on the credential.
- `trustedAuthorities`: Issuer authorities and trust frameworks the relying party accepts; empty if unspecified.
- `requireCryptographicHolderBinding`: A Boolean that specifies whether the relying party requires a cryptographic holder binding proof.
- `claims`: The claims requested; empty if unspecified.
- `claimSets`: Combinations of claim identifiers the relying party accepts, in order of preference; empty if unspecified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/digitalcredentialsquery/credentialquery/init(id:format:multiple:meta:trustedauthorities:requirecryptographicholderbinding:claims:claimsets:))*