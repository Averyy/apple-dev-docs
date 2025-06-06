# documentBrowser(_:failedToImportDocumentAt:error:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the document browser failed to import the specified document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentBrowser(_ controller: UIDocumentBrowserViewController, failedToImportDocumentAt documentURL: URL, error: (any Error)?)
```

## Parameters

- `controller`: The document browser that attempted the import action.
- `documentURL`: The document’s original URL.
- `error`: An object describing the error, or  .

## See Also

- [func documentBrowser(UIDocumentBrowserViewController, didRequestDocumentCreationWithHandler: (URL?, UIDocumentBrowserViewController.ImportMode) -> Void)](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didrequestdocumentcreationwithhandler:).md)
  Asks the delegate to create a new document.
- [UIDocumentBrowserViewController.ImportMode](uidocumentbrowserviewcontroller/importmode.md)
  The document browser’s import modes.
- [func documentBrowser(UIDocumentBrowserViewController, didImportDocumentAt: URL, toDestinationURL: URL)](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didimportdocumentat:todestinationurl:).md)
  Tells the delegate that a document has been successfully imported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:failedtoimportdocumentat:error:))*