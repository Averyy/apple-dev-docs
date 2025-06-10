# supportedAuthorityKeyIdentifiers

**Framework**: IdentityDocumentServices  
**Kind**: property

A list of authority key identifiers that correspond to relying party authorizers that are trusted by the document provider app.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
var supportedAuthorityKeyIdentifiers: [Data]
```

#### Discussion

A relying party that’s authorized by an authority in this list of key identifiers can receive this document during a presentment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/mobiledocumentregistration/supportedauthoritykeyidentifiers)*