# importDocument(at:nextToDocumentAt:mode:completionHandler:)

**Framework**: UIKit  
**Kind**: method

Imports a document into the same location as an existing document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func importDocument(at documentURL: URL, nextToDocumentAt neighbourURL: URL, mode importMode: UIDocumentBrowserViewController.ImportMode) async throws -> URL
```

#### Discussion

Use this method to import a document into the same file provider and directory as an existing document.

For example, to duplicate a document that’s already managed by a file provider:

1. Create a duplicate of the original file in the user’s temporary directory. Be sure to give it a unique name.
2. Call [`importDocument(at:nextToDocumentAt:mode:completionHandler:)`](uidocumentbrowserviewcontroller/importdocument(at:nexttodocumentat:mode:completionhandler:).md), passing in the temporary file’s URL as the `documentURL` parameter and the original file’s URL as the `neighbourURL` parameter.

The system imports the duplicate into the same file provider (the local file provider, the iCloud file provider, or a third-party file provider) and the same directory as the original file.

## Parameters

- `documentURL`: The URL of the document’s initial location.
- `neighbourURL`: The URL of a document that’s already managed by a file provider (the local file provider, the iCloud file provider, or a third-party file provider). The system imports the document into the same file provider and directory as this URL.
- `importMode`: The mode used when importing the document. For a list of import modes, see  .
- `completion`: 

## See Also

- [var delegate: (any UIDocumentBrowserViewControllerDelegate)?](uidocumentbrowserviewcontroller/delegate.md)
  The document browser’s delegate.
- [protocol UIDocumentBrowserViewControllerDelegate](uidocumentbrowserviewcontrollerdelegate.md)
  The protocol you implement to respond as the user interacts with the document browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/importdocument(at:nexttodocumentat:mode:completionhandler:))*