# DigitalCredentialsQuery.TrustedAuthoritiesQuery

**Framework**: IdentityDocumentServices  
**Kind**: struct  
**Role**: Structure

An issuer authority or trust framework that a relying party accepts.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
struct TrustedAuthoritiesQuery
```

## Topics

### Initializers
- [init(type: DigitalCredentialsQuery.TrustedAuthoritiesQuery.AuthorityType, values: [String])](./trustedauthoritiesquery/init%28type,values%29.md)
  Initializes a trusted authorities query.
### Instance Properties
- [var type: DigitalCredentialsQuery.TrustedAuthoritiesQuery.AuthorityType](./trustedauthoritiesquery/type.md)
  The kind of authority information being matched.
- [var values: [String]](./trustedauthoritiesquery/values.md)
  The accepted authority identifiers, interpreted according to type.
### Enumerations
- [DigitalCredentialsQuery.TrustedAuthoritiesQuery.AuthorityType](./trustedauthoritiesquery/authoritytype.md)
  The kind of authority information being matched.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/digitalcredentialsquery/trustedauthoritiesquery)*