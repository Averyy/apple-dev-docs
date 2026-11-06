# init(type:values:)

**Framework**: IdentityDocumentServices  
**Kind**: init  
**Role**: Initializer

Initializes a trusted authorities query.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
init(type: DigitalCredentialsQuery.TrustedAuthoritiesQuery.AuthorityType, values: [String])
```

## Parameters

- `type`: The kind of authority information being matched.
- `values`: The accepted authority identifiers, interpreted according to `type`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/digitalcredentialsquery/trustedauthoritiesquery/init(type:values:))*