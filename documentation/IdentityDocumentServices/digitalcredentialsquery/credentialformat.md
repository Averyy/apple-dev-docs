# DigitalCredentialsQuery.CredentialFormat

**Framework**: IdentityDocumentServices  
**Kind**: enum  
**Role**: Enumeration

The format of a requested credential.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
enum CredentialFormat
```

## Topics

### Enumeration Cases
- [DigitalCredentialsQuery.CredentialFormat.dcSDJWT](./credentialformat/dcsdjwt.md)
  An IETF SD-JWT verifiable credential.
- [DigitalCredentialsQuery.CredentialFormat.msoMdoc](./credentialformat/msomdoc.md)
  An ISO 18013-5 mobile document.
- [DigitalCredentialsQuery.CredentialFormat.unknown](./credentialformat/unknown.md)
  A format the system doesn’t support.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Describing credentials
- [DigitalCredentialsQuery.CredentialQuery](./credentialquery.md)
  A request for a single credential.
- [DigitalCredentialsQuery.Metadata](./metadata.md)
  Format-specific constraints on a requested credential.
- [DigitalCredentialsQuery.CredentialSetQuery](./credentialsetquery.md)
  A grouping of credentials that satisfies part of a query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/digitalcredentialsquery/credentialformat)*