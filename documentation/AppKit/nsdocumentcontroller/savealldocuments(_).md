# saveAllDocuments(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

As the action method called by the Save All command, saves all open documents of the application that need to be saved.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func saveAllDocuments(_ sender: Any?)
```

```objc
- (void) saveAllDocuments:(id) sender;
```

## See Also

### Related Documentation
- [func save(Any?)](../nsdocument/save%28_%29.md)
  The action method invoked in the receiver as first responder when the user chooses the Save menu command.
### Responding to Action Messages
- [func newDocument(Any?)](./newdocument%28_%29.md)
  An action method called by the New menu command, this method creates a new `NSDocument` object and adds it to the list of such objects managed by the document controller.
- [func openDocument(Any?)](./opendocument%28_%29.md)
  An action method called by the Open menu command, it runs the modal Open panel and, based on the selected filenames, creates one or more `NSDocument` objects from the contents of the files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/savealldocuments(_:))*