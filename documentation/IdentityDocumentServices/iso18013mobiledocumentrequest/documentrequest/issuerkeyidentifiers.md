# issuerKeyIdentifiers

**Framework**: IdentityDocumentServices  
**Kind**: property  
**Role**: Instance Property

A list of X.509 authority key identifiers corresponding to the issuer certificates accepted by the relying party.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst
- macOS 27.0+

## Declaration

```swift
var issuerKeyIdentifiers: [Data]
```

## Mentions

- [Implementing as an identity document provider](../../implementing-as-an-identity-document-provider.md)

## Discussion

An empty list means any document signer certificate is acceptable.

> **Note**: The number of issuer key identifiers can’t exceed 1,000, and the size of each identifier can’t exceed 64 bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/iso18013mobiledocumentrequest/documentrequest/issuerkeyidentifiers)*