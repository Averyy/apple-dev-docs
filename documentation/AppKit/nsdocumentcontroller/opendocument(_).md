# openDocument(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

An action method called by the Open menu command, it runs the modal Open panel and, based on the selected filenames, creates one or more `NSDocument` objects from the contents of the files.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func openDocument(_ sender: Any?)
```

```objc
- (void) openDocument:(id) sender;
```

#### Discussion

The method adds the newly created objects to the list of `NSDocument` objects managed by the document controller. This method calls [`openDocument(withContentsOf:display:completionHandler:)`](./opendocument%28withcontentsof,display,completionhandler%29.md), which actually creates the `NSDocument` objects.

## See Also

### Responding to Action Messages
- [func newDocument(Any?)](./newdocument%28_%29.md)
  An action method called by the New menu command, this method creates a new `NSDocument` object and adds it to the list of such objects managed by the document controller.
- [func saveAllDocuments(Any?)](./savealldocuments%28_%29.md)
  As the action method called by the Save All command, saves all open documents of the application that need to be saved.
### Related Documentation
- [- fileNamesFromRunningOpenPanel](./filenamesfromrunningopenpanel.md)
  Returns a selection of files chosen by the user in the Open panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/opendocument(_:))*