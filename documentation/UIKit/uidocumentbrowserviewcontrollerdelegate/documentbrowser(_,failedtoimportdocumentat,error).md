# documentBrowser(_:failedToImportDocumentAt:error:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) documentBrowser:(UIDocumentBrowserViewController *) controller failedToImportDocumentAtURL:(NSURL *) documentURL error:(NSError *) error;
```

## Parameters

- `controller`: The document browser that attempted the import action.
- `documentURL`: The document’s original URL.
- `error`: An object describing the error, or `nil`.

## See Also

### Creating new documents
- [func documentBrowser(UIDocumentBrowserViewController, didRequestDocumentCreationWithHandler: (URL?, UIDocumentBrowserViewController.ImportMode) -> Void)](./documentbrowser%28_,didrequestdocumentcreationwithhandler%29.md)
  Asks the delegate to create a new document.
- [UIDocumentBrowserViewController.ImportMode](../uidocumentbrowserviewcontroller/importmode.md)
  The document browser’s import modes.
- [func documentBrowser(UIDocumentBrowserViewController, didImportDocumentAt: URL, toDestinationURL: URL)](./documentbrowser%28_,didimportdocumentat,todestinationurl%29.md)
  Tells the delegate that a document has been successfully imported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:failedtoimportdocumentat:error:))*