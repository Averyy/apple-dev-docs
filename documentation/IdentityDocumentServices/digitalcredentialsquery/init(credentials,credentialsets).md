# init(credentials:credentialSets:)

**Framework**: IdentityDocumentServices  
**Kind**: init  
**Role**: Initializer

Initializes a query.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
init(credentials: [DigitalCredentialsQuery.CredentialQuery], credentialSets: [DigitalCredentialsQuery.CredentialSetQuery] = [])
```

## Parameters

- `credentials`: The credentials requested.
- `credentialSets`: Groupings of credentials that satisfy the query, empty if unspecified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/digitalcredentialsquery/init(credentials:credentialsets:))*