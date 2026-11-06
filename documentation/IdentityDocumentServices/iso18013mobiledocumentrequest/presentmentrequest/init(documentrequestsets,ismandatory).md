# init(documentRequestSets:isMandatory:)

**Framework**: IdentityDocumentServices  
**Kind**: init  
**Role**: Initializer

Initializes a presentment request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst
- macOS 26.0+

## Declaration

```swift
init(documentRequestSets: [ISO18013MobileDocumentRequest.DocumentRequestSet], isMandatory: Bool)
```

## Parameters

- `documentRequestSets`: An array of the document request sets that can be used to satisfy the presentment request.
- `isMandatory`: A Boolean value that represents whether the presentment request must be satisfied in order to complete the `ISO18013MobileDocumentRequest`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/iso18013mobiledocumentrequest/presentmentrequest/init(documentrequestsets:ismandatory:))*