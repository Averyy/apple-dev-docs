# UIDocumentBrowserViewController.ImportMode

**Framework**: UIKit  
**Kind**: enum

The document browser’s import modes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum ImportMode
```

## Mentions

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md)

## Topics

### Constants
- [UIDocumentBrowserViewController.ImportMode.copy](uidocumentbrowserviewcontroller/importmode/copy.md)
  A mode indicating that the file should be copied into its new location (the original file is left unchanged).
- [UIDocumentBrowserViewController.ImportMode.move](uidocumentbrowserviewcontroller/importmode/move.md)
  A mode indicating that the file should be moved to its new location (the original file should be deleted).
- [UIDocumentBrowserViewController.ImportMode.none](uidocumentbrowserviewcontroller/importmode/none.md)
  A mode indicating that the document can’t be imported.
### Initializers
- [init?(rawValue: UInt)](uidocumentbrowserviewcontroller/importmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func documentBrowser(UIDocumentBrowserViewController, didRequestDocumentCreationWithHandler: (URL?, UIDocumentBrowserViewController.ImportMode) -> Void)](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didrequestdocumentcreationwithhandler:).md)
  Asks the delegate to create a new document.
- [func documentBrowser(UIDocumentBrowserViewController, didImportDocumentAt: URL, toDestinationURL: URL)](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didimportdocumentat:todestinationurl:).md)
  Tells the delegate that a document has been successfully imported.
- [func documentBrowser(UIDocumentBrowserViewController, failedToImportDocumentAt: URL, error: (any Error)?)](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:failedtoimportdocumentat:error:).md)
  Tells the delegate that the document browser failed to import the specified document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/importmode)*