# init(documentType:verifiableCredentialTypes:)

**Framework**: IdentityDocumentServices  
**Kind**: init  
**Role**: Initializer

Initialize format-specific constraints.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
init(documentType: String? = nil, verifiableCredentialTypes: [String] = [])
```

## Parameters

- `documentType`: The accepted document type, for mobile documents.
- `verifiableCredentialTypes`: The accepted verifiable credential types, for SD-JWT VCs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/digitalcredentialsquery/metadata/init(documenttype:verifiablecredentialtypes:))*