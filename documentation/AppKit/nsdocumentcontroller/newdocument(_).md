# newDocument(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

An action method called by the New menu command, this method creates a new `NSDocument` object and adds it to the list of such objects managed by the document controller.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func newDocument(_ sender: Any?)
```

```objc
- (void) newDocument:(id) sender;
```

## Discussion

This method calls [`openUntitledDocumentAndDisplay(_:)`](./openuntitleddocumentanddisplay%28_%29.md).

## See Also

### Responding to Action Messages
- [func openDocument(Any?)](./opendocument%28_%29.md)
  An action method called by the Open menu command, it runs the modal Open panel and, based on the selected filenames, creates one or more `NSDocument` objects from the contents of the files.
- [func saveAllDocuments(Any?)](./savealldocuments%28_%29.md)
  As the action method called by the Save All command, saves all open documents of the application that need to be saved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/newdocument(_:))*