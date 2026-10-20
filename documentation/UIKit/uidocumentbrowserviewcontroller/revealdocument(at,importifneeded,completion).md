# revealDocument(at:importIfNeeded:completion:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Reveals, and optionally imports, the document at the provided URL.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func revealDocument(at url: URL, importIfNeeded: Bool, completion: ((URL?, (any Error)?) -> Void)? = nil)
```

```swift
func revealDocument(at url: URL, importIfNeeded: Bool) async throws -> URL
```

```objc
- (void) revealDocumentAtURL:(NSURL *) url importIfNeeded:(BOOL) importIfNeeded completion:(void (^)(NSURL *revealedDocumentURL, NSError *error)) completion;
```

## Mentions

- [Enabling document sharing](../enabling-document-sharing.md)

#### Discussion

Call this method to display a document in the document browser.

If `importIfNeeded` is [`true`](../../Swift/true.md), the document browser calls its delegate’s [`documentBrowser(_:didImportDocumentAt:toDestinationURL:)`](../uidocumentbrowserviewcontrollerdelegate/documentbrowser%28_,didimportdocumentat,todestinationurl%29.md) method (or its [`documentBrowser(_:failedToImportDocumentAt:error:)`](../uidocumentbrowserviewcontrollerdelegate/documentbrowser%28_,failedtoimportdocumentat,error%29.md) method, if an error occurred) before calling the completion handler.

## Parameters

- `url`: The URL of the document to reveal.
- `importIfNeeded`: A Boolean value that determines whether the document browser should import the document.
- `completion`: A completion block with the following parameters:

  - **url**: The new URL of an imported document. Set to `nil` if `shouldImport` is [`false`](../../Swift/false.md), or if an error occurs.
  - **error**: If an error occurs, this parameter contains the error information; otherwise, set to `nil`.

## See Also

### Configuring a document browser
- [var allowsDocumentCreation: Bool](./allowsdocumentcreation.md)
  A Boolean value that determines whether the document browser can create new documents.
- [var allowsPickingMultipleItems: Bool](./allowspickingmultipleitems.md)
  A Boolean value that determines whether the user can select and open more than one document at a time.
- [var contentTypesForRecentDocuments: [UTType]](./contenttypesforrecentdocuments.md)
  Content types for browsing recent documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/revealdocument(at:importifneeded:completion:))*