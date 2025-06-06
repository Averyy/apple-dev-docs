# documentBrowser(_:didPickDocumentsAt:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the user has selected one or more documents.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentBrowser(_ controller: UIDocumentBrowserViewController, didPickDocumentsAt documentURLs: [URL])
```

#### Discussion

Implement this method to process the documents selected by the user. Typically, you create a view controller to display the selected documents, then present that view modally, like in the following code.

```swift
// Did Select Documents
func documentBrowser(_ controller: UIDocumentBrowserViewController,
    didPickDocumentsAt documentURLs: [URL]) {
    
    assert(controller.allowsPickingMultipleItems == false)
    
    assert(documentURLs.count > 0,
           "*** We received an empty array of documents ***")
    
    assert(documentURLs.count <= 1,
           "*** We received more than one document ***")
    
    guard let url = documentURLs.first else {
        fatalError("*** No URL Found! ***")
    }
    
    openDocument(controller, forFileURL: url)
}

private func openDocument(_ controller: UIDocumentBrowserViewController,
                          forFileURL url: URL) {
    
    let doc = // Create a UIDocument subclass for the selected URL.

    let editor = // Create a view controller to edit the document.

    // Optionally, set up a transition controller here...
        
    doc.open { (success) in
        guard success else {
            // Handle the error here...
        }
        
        // Present the document
        controller.present(editor, animated: true, completion: nil)
    }
}
```

## Parameters

- `controller`: The current document browser.
- `documentURLs`: If the document browser’s   property is  , the array contains one or more URLs. If  , it contains only a single URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didpickdocumentsat:))*