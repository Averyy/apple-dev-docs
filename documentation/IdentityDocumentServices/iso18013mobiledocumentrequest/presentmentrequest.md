# ISO18013MobileDocumentRequest.PresentmentRequest

**Framework**: IdentityDocumentServices  
**Kind**: struct  
**Role**: Structure

A type that represents an individual presentment request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst
- macOS 26.0+

## Declaration

```swift
struct PresentmentRequest
```

#### Discussion

One or more of these make up an `ISO18013MobileDocumentRequest`.

## Topics

### Initializers
- [init(documentRequestSets: [ISO18013MobileDocumentRequest.DocumentRequestSet], isMandatory: Bool)](./presentmentrequest/init%28documentrequestsets,ismandatory%29.md)
  Initializes a presentment request.
### Instance Properties
- [var documentRequestSets: [ISO18013MobileDocumentRequest.DocumentRequestSet]](./presentmentrequest/documentrequestsets.md)
  An array of the document request sets that you can use to complete this presentment request.
- [var isMandatory: Bool](./presentmentrequest/ismandatory.md)
  Whether this presentment request is required in order to complete the `ISO18013MobileDocumentRequest`.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/iso18013mobiledocumentrequest/presentmentrequest)*