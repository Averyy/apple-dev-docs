# issuerKeyIdentifiers

**Framework**: IdentityDocumentServices  
**Kind**: property

A list of X.509 authority key identifiers corresponding to the issuer certificates accepted by the relying party.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)

## Declaration

```swift
var issuerKeyIdentifiers: [Data]
```

#### Discussion

An empty list means any document signer certificate is acceptable.

> ⚠️ **Warning**: The number of issuer key identifiers must not exceed 1,000 and the size of each identifier must not exceed 64 bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/iso18013mobiledocumentrequest/documentrequest/issuerkeyidentifiers)*