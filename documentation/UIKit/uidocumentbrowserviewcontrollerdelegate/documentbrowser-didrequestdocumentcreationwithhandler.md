# documentBrowser(_:didRequestDocumentCreationWithHandler:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to create a new document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentBrowser(_ controller: UIDocumentBrowserViewController, didRequestDocumentCreationWithHandler importHandler: @escaping (URL?, UIDocumentBrowserViewController.ImportMode) -> Void)
```

## Mentions

- [Customizing the browser](customizing-the-browser.md)
- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md)

#### Discussion

Implement this method to create new documents for the user:

1. (Optional) Display any controls the user needs to configure the document.
2. Create a new document and save it to a temporary location. If you use a [`UIDocument`](uidocument.md) subclass to create the document, you must close it before calling the `importHandler` block. Always open a new document in your [`documentBrowser(_:didImportDocumentAt:toDestinationURL:)`](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didimportdocumentat:todestinationurl:).md) method.
3. Call the provided `importHandler` block. To confirm the request, pass in the document’s temporary URL and the import mode ([`UIDocumentBrowserViewController.ImportMode.copy`](uidocumentbrowserviewcontroller/importmode/copy.md) or [`UIDocumentBrowserViewController.ImportMode.move`](uidocumentbrowserviewcontroller/importmode/move.md)). To cancel the request, pass `nil` and [`UIDocumentBrowserViewController.ImportMode.none`](uidocumentbrowserviewcontroller/importmode/none.md).
4. Implement the [`documentBrowser(_:didImportDocumentAt:toDestinationURL:)`](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didimportdocumentat:todestinationurl:).md) method. In this method, open the document at the destination URL. You must use either a [`UIDocument`](uidocument.md) subclass, or a file presenter and file coordination.
5. Modally present this document to the user.

> ❗ **Important**:  You must always call the import handler. If you cannot create a new document, pass `nil` for the URL and [`UIDocumentBrowserViewController.ImportMode.none`](uidocumentbrowserviewcontroller/importmode/none.md) for the import mode.

 You must always call the import handler. If you cannot create a new document, pass `nil` for the URL and [`UIDocumentBrowserViewController.ImportMode.none`](uidocumentbrowserviewcontroller/importmode/none.md) for the import mode.

The following example shows a possible implementation of the  [`documentBrowser(_:didRequestDocumentCreationWithHandler:)`](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didrequestdocumentcreationwithhandler:).md) method.

```swift
// Create New Document
func documentBrowser(_ controller: UIDocumentBrowserViewController, didRequestDocumentCreationWithHandler importHandler: @escaping (URL?, UIDocumentBrowserViewController.ImportMode) -> Void) {
        
    let doc = // Create a new UIDocument... 
    let url = // Get a temporary URL...
    
    // Create a new document in a temporary location
    doc.save(to: url, for: .forCreating) { (saveSuccess) in
        
        // Make sure the document saved successfully
        guard saveSuccess else {            
            // Cancel document creation
            importHandler(nil, .none)
            return
        }
        
        // Close the document.
        doc.close(completionHandler: { (closeSuccess) in
            
            // Make sure the document closed successfully
            guard closeSuccess else {                
                // Cancel document creation
                importHandler(nil, .none)
                return
            }
            
            // Pass the document's temporary URL to the import handler.
            importHandler(url, .move)
        })
    }
}
```

After the `importHandler` block is called, the document browser asynchronously imports the document into its final destination. When possible, the document browser imports to the currently open directory. When there is no currently open directory (for example, when the Recents tab is open), it uses the default directory.

Users can set the default directory in Settings. For more information, see [`Setting up a document browser app`](setting-up-a-document-browser-app.md).

When the import is complete, the browser calls one of the following delegate methods:

-  [`documentBrowser(_:didImportDocumentAt:toDestinationURL:)`](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didimportdocumentat:todestinationurl:).md)
-  [`documentBrowser(_:failedToImportDocumentAt:error:)`](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:failedtoimportdocumentat:error:).md)

The document browser enables the Add button (+) only when both of the following are true:

- The [`allowsDocumentCreation`](uidocumentbrowserviewcontroller/allowsdocumentcreation.md) property is set to [`true`](https://developer.apple.com/documentation/swift/true) (the default value).
- The document browser delegate implements the [`documentBrowser(_:didRequestDocumentCreationWithHandler:)`](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didrequestdocumentcreationwithhandler:).md) method.

> **Note**:  The document browser cannot create new documents if you do not implement this delegate method.

 The document browser cannot create new documents if you do not implement this delegate method.

## Parameters

- `controller`: The current document browser.
- `importHandler`: A block that takes the following parameters:

## See Also

- [UIDocumentBrowserViewController.ImportMode](uidocumentbrowserviewcontroller/importmode.md)
  The document browser’s import modes.
- [func documentBrowser(UIDocumentBrowserViewController, didImportDocumentAt: URL, toDestinationURL: URL)](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didimportdocumentat:todestinationurl:).md)
  Tells the delegate that a document has been successfully imported.
- [func documentBrowser(UIDocumentBrowserViewController, failedToImportDocumentAt: URL, error: (any Error)?)](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:failedtoimportdocumentat:error:).md)
  Tells the delegate that the document browser failed to import the specified document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didrequestdocumentcreationwithhandler:))*