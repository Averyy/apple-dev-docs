# ISO18013MobileDocumentRequest.DocumentRequest

**Framework**: IdentityDocumentServices  
**Kind**: struct

A request that contains information for requesting a mobile document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
struct DocumentRequest
```

## Topics

### Initializers
- [init(documentType: String, namespaces: [String : [String : ISO18013MobileDocumentRequest.ElementInfo]])](iso18013mobiledocumentrequest/documentrequest/init(documenttype:namespaces:).md)
  Initializes a document request.
### Instance Properties
- [var documentType: String](iso18013mobiledocumentrequest/documentrequest/documenttype.md)
  The document type requested.
- [var namespaces: [String : [String : ISO18013MobileDocumentRequest.ElementInfo]]](iso18013mobiledocumentrequest/documentrequest/namespaces.md)
  The namespaces in the document to request.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/iso18013mobiledocumentrequest/documentrequest)*