# newDocument(_:)

**Framework**: AppKit  
**Kind**: method

An action method called by the New menu command, this method creates a new `NSDocument` object and adds it to the list of such objects managed by the document controller.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func newDocument(_ sender: Any?)
```

#### Discussion

This method calls [`openUntitledDocumentAndDisplay(_:)`](nsdocumentcontroller/openuntitleddocumentanddisplay(_:).md).

## See Also

- [func openDocument(Any?)](nsdocumentcontroller/opendocument(_:).md)
  An action method called by the Open menu command, it runs the modal Open panel and, based on the selected filenames, creates one or more `NSDocument` objects from the contents of the files.
- [func saveAllDocuments(Any?)](nsdocumentcontroller/savealldocuments(_:).md)
  As the action method called by the Save All command, saves all open documents of the application that need to be saved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/newdocument(_:))*