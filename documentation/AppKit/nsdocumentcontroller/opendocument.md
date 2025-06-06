# openDocument(_:)

**Framework**: AppKit  
**Kind**: method

An action method called by the Open menu command, it runs the modal Open panel and, based on the selected filenames, creates one or more `NSDocument` objects from the contents of the files.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func openDocument(_ sender: Any?)
```

#### Discussion

The method adds the newly created objects to the list of `NSDocument` objects managed by the document controller. This method calls [`openDocument(withContentsOf:display:completionHandler:)`](nsdocumentcontroller/opendocument(withcontentsof:display:completionhandler:).md), which actually creates the `NSDocument` objects.

## See Also

- [func newDocument(Any?)](nsdocumentcontroller/newdocument(_:).md)
  An action method called by the New menu command, this method creates a new `NSDocument` object and adds it to the list of such objects managed by the document controller.
- [func saveAllDocuments(Any?)](nsdocumentcontroller/savealldocuments(_:).md)
  As the action method called by the Save All command, saves all open documents of the application that need to be saved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/opendocument(_:))*