# ISO18013MobileDocumentRequest.DocumentRequest

**Framework**: IdentityDocumentServices  
**Kind**: struct  
**Role**: Structure

A request that contains information for requesting a mobile document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst
- macOS 26.0+

## Declaration

```swift
struct DocumentRequest
```

## Topics

### Initializers
- [init(documentType: String, namespaces: [String : [String : ISO18013MobileDocumentRequest.ElementInfo]])](./documentrequest/init%28documenttype,namespaces%29.md)
  Initializes a document request.
- [init(documentType: String, namespaces: [String : [String : ISO18013MobileDocumentRequest.ElementInfo]], issuerKeyIdentifiers: [Data])](./documentrequest/init%28documenttype,namespaces,issuerkeyidentifiers%29.md)
  Initialize a document request.
### Instance Properties
- [var documentType: String](./documentrequest/documenttype.md)
  The document type requested.
- [var issuerKeyIdentifiers: [Data]](./documentrequest/issuerkeyidentifiers.md)
  A list of X.509 authority key identifiers corresponding to the issuer certificates accepted by the relying party.
- [var namespaces: [String : [String : ISO18013MobileDocumentRequest.ElementInfo]]](./documentrequest/namespaces.md)
  The namespaces in the document to request.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/iso18013mobiledocumentrequest/documentrequest)*