# supportedIssuerKeyIdentifiers

**Framework**: IdentityDocumentServices  
**Kind**: property

A list of X.509 authority key identifiers that correspond to the document signer certificate chain for the mobile document.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
var supportedIssuerKeyIdentifiers: [Data]
```

#### Discussion

An issuer key identifier is an authority key identifier from the document signer certificate chain.

> ⚠️ **Warning**: The number of issuer key identifiers must not exceed 1,000 and the size of each identifier must not exceed 64 bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/mobiledocumentregistration/supportedissuerkeyidentifiers)*