# saveAllDocuments(_:)

**Framework**: AppKit  
**Kind**: method

As the action method called by the Save All command, saves all open documents of the application that need to be saved.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func saveAllDocuments(_ sender: Any?)
```

## See Also

- [func save(Any?)](nsdocument/save(_:).md)
  The action method invoked in the receiver as first responder when the user chooses the Save menu command.
- [func newDocument(Any?)](nsdocumentcontroller/newdocument(_:).md)
  An action method called by the New menu command, this method creates a new `NSDocument` object and adds it to the list of such objects managed by the document controller.
- [func openDocument(Any?)](nsdocumentcontroller/opendocument(_:).md)
  An action method called by the Open menu command, it runs the modal Open panel and, based on the selected filenames, creates one or more `NSDocument` objects from the contents of the files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/savealldocuments(_:))*