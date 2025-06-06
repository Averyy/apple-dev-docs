# revealDocument(at:importIfNeeded:completion:)

**Framework**: UIKit  
**Kind**: method

Reveals, and optionally imports, the document at the provided URL.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func revealDocument(at url: URL, importIfNeeded: Bool) async throws -> URL
```

## Mentions

- [Enabling document sharing](enabling-document-sharing.md)

#### Discussion

Call this method to display a document in the document browser.

If `importIfNeeded` is [`true`](https://developer.apple.com/documentation/swift/true), the document browser calls its delegate’s [`documentBrowser(_:didImportDocumentAt:toDestinationURL:)`](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didimportdocumentat:todestinationurl:).md) method (or its [`documentBrowser(_:failedToImportDocumentAt:error:)`](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:failedtoimportdocumentat:error:).md) method, if an error occurred) before calling the completion handler.

## Parameters

- `url`: The URL of the document to reveal.
- `importIfNeeded`: A Boolean value that determines whether the document browser should import the document.
- `completion`: A completion block with the following parameters:

## See Also

- [var allowsDocumentCreation: Bool](uidocumentbrowserviewcontroller/allowsdocumentcreation.md)
  A Boolean value that determines whether the document browser can create new documents.
- [var allowsPickingMultipleItems: Bool](uidocumentbrowserviewcontroller/allowspickingmultipleitems.md)
  A Boolean value that determines whether the user can select and open more than one document at a time.
- [var contentTypesForRecentDocuments: [UTType]](uidocumentbrowserviewcontroller/contenttypesforrecentdocuments.md)
  Content types for browsing recent documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/revealdocument(at:importifneeded:completion:))*