# DigitalCredentialsQuery.Metadata

**Framework**: IdentityDocumentServices  
**Kind**: struct  
**Role**: Structure

Format-specific constraints on a requested credential.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
struct Metadata
```

## Topics

### Initializers
- [init(documentType: String?, verifiableCredentialTypes: [String])](./metadata/init%28documenttype,verifiablecredentialtypes%29.md)
  Initialize format-specific constraints.
### Instance Properties
- [var documentType: String?](./metadata/documenttype.md)
  The accepted document type, for mobile documents.
- [var verifiableCredentialTypes: [String]](./metadata/verifiablecredentialtypes.md)
  The accepted verifiable credential types, for SD-JWT VCs.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Describing credentials
- [DigitalCredentialsQuery.CredentialQuery](./credentialquery.md)
  A request for a single credential.
- [DigitalCredentialsQuery.CredentialFormat](./credentialformat.md)
  The format of a requested credential.
- [DigitalCredentialsQuery.CredentialSetQuery](./credentialsetquery.md)
  A grouping of credentials that satisfies part of a query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/digitalcredentialsquery/metadata)*