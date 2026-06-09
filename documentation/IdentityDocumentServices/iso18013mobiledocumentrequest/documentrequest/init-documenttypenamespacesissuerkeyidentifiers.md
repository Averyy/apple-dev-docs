# init(documentType:namespaces:issuerKeyIdentifiers:)

**Framework**: IdentityDocumentServices  
**Kind**: init

Initialize a document request.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)

## Declaration

```swift
init(documentType: String, namespaces: [String : [String : ISO18013MobileDocumentRequest.ElementInfo]], issuerKeyIdentifiers: [Data])
```

## Parameters

- `documentType`: The document type being requested.
- `namespaces`: The namespaces in the document to request.
- `issuerKeyIdentifiers`: A list of X.509 authority key identifiers corresponding to the issuer certificates accepted by the relying party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/iso18013mobiledocumentrequest/documentrequest/init(documenttype:namespaces:issuerkeyidentifiers:))*