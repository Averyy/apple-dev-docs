# init(id:path:values:intentToRetain:)

**Framework**: IdentityDocumentServices  
**Kind**: init  
**Role**: Initializer

Initializes a claims query.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
init(id: String? = nil, path: DigitalCredentialsQuery.ClaimsQuery.ClaimPath, values: [DigitalCredentialsQuery.ClaimsQuery.AcceptedValue] = [], intentToRetain: Bool? = nil)
```

## Parameters

- `id`: Identifies a claim within the credential query.
- `path`: The path to the claim within the credential.
- `values`: The values the relying party accepts for the claim; empty if unspecified.
- `intentToRetain`: A Boolean value that indicates whether the relying party intends to retain the claim.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/digitalcredentialsquery/claimsquery/init(id:path:values:intenttoretain:))*