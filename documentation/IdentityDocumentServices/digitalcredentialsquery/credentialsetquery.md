# DigitalCredentialsQuery.CredentialSetQuery

**Framework**: IdentityDocumentServices  
**Kind**: struct  
**Role**: Structure

A grouping of credentials that satisfies part of a query.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
struct CredentialSetQuery
```

## Topics

### Initializers
- [init(options: [Set<String>], isRequired: Bool)](./credentialsetquery/init%28options,isrequired%29.md)
  Initializes a credential set query.
### Instance Properties
- [var isRequired: Bool](./credentialsetquery/isrequired.md)
  A Boolean that specifies whether a grouping must be satisfied.
- [var options: [Set<String>]](./credentialsetquery/options.md)
  Sets of credential query identifiers, any one of which satisfies a grouping.

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
- [DigitalCredentialsQuery.Metadata](./metadata.md)
  Format-specific constraints on a requested credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/digitalcredentialsquery/credentialsetquery)*