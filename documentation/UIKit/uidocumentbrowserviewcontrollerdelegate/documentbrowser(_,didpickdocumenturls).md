# documentBrowser(_:didPickDocumentURLs:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user has selected one or more documents.

**Availability**:
- iOS 11.0+ - Deprecated in 12.0
- iPadOS 11.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`documentPicker(_:didPickDocumentsAt:)`](../uidocumentpickerdelegate/documentpicker%28_,didpickdocumentsat%29.md) instead.

## Declaration

```swift
optional func documentBrowser(_ controller: UIDocumentBrowserViewController, didPickDocumentURLs documentURLs: [URL])
```

```objc
- (void) documentBrowser:(UIDocumentBrowserViewController *) controller didPickDocumentURLs:(NSArray<NSURL *> *) documentURLs;
```

## Mentions

- [Presenting selected documents](../presenting-selected-documents.md)

#### Discussion

Implement this method to process the documents selected by the user. Typically, you create a view controller to display the selected documents, then present that view modally, like in the following example.

```swift
// Did Select Documents
func documentBrowser(_ controller: UIDocumentBrowserViewController,
                     didPickDocumentURLs documentURLs: [URL]) {
    
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
- `documentURLs`: An array of URLs for the selected documents.

  If the document browser’s [`allowsPickingMultipleItems`](../uidocumentbrowserviewcontroller/allowspickingmultipleitems.md) property is [`true`](../../Swift/true.md), the array contains one or more URLs. If [`false`](../../Swift/false.md), it contains only a single URL.

## See Also

### Selecting documents
- [func documentBrowser(UIDocumentBrowserViewController, didPickDocumentsAt: [URL])](./documentbrowser%28_,didpickdocumentsat%29.md)
  Tells the delegate that the user has selected one or more documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didpickdocumenturls:))*