# setFileName:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the file (filename and directory path) under which document data is saved.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`NSDocument`](../nsdocument.md) instead.

## Declaration

```objc
- (void) setFileName:(NSString *) fileName;
```

#### Discussion

Sets the file (filename and directory path) under which document data is saved to `fileName`. As a side effect, synchronizes the titles of the document’s windows with the new name or location. A document’s filename is automatically set when it is saved as a new document (Save) and when an existing document is saved under a different filename or path (Save As). The Finder also keeps track of open documents and their associated files. When a user moves or renames a file in the Finder that corresponds to an open document, the Finder calls [`setFileName:`](./setfilename_.md) with the new filename.

## See Also

### Deprecated methods
- [- dataRepresentationOfType:](./datarepresentationoftype_.md)
  A primitive method to return a data object that represents the data of the receiver in a given type.
- [- fileAttributesToWriteToFile:ofType:saveOperation:](./fileattributestowritetofile_oftype_saveoperation_.md)
  Returns the file attributes that should be written to the named document file of the specified type.
- [- fileName](./filename.md)
  Returns the fully qualified pathname under which the receiver has been saved.
- [- fileWrapperRepresentationOfType:](./filewrapperrepresentationoftype_.md)
  Returns a file wrapper object that represents the data of the receiver in a given type.
- [- initWithContentsOfFile:ofType:](./initwithcontentsoffile_oftype_.md)
  Initializes and returns a document object.
- [- initWithContentsOfURL:ofType:](./initwithcontentsofurl_oftype_.md)
  Initializes and returns a document object of a given type.
- [- loadDataRepresentation:ofType:](./loaddatarepresentation_oftype_.md)
  Loads the document data.
- [- loadFileWrapperRepresentation:ofType:](./loadfilewrapperrepresentation_oftype_.md)
  Loads document data from a given file wrapper.
- [- printShowingPrintPanel:](./printshowingprintpanel_.md)
  Prints the current document’s data.
- [- readFromFile:ofType:](./readfromfile_oftype_.md)
  Reads and loads document data of the given type from the given file.
- [- readFromURL:ofType:](./readfromurl_oftype_.md)
  Reads and loads document data.
- [- revertToSavedFromFile:ofType:](./reverttosavedfromfile_oftype_.md)
  Reverts the receiver to the data stored in the file system.
- [- revertToSavedFromURL:ofType:](./reverttosavedfromurl_oftype_.md)
  Reverts the receiver.
- [- runModalPageLayoutWithPrintInfo:](./runmodalpagelayoutwithprintinfo_.md)
  Runs the page layout modal panel with the receiver’s printing information object.
- [- saveToFile:saveOperation:delegate:didSaveSelector:contextInfo:](./savetofile_saveoperation_delegate_didsaveselector_contextinfo_.md)
  Called after the user has been given the opportunity to select a destination through the modal Save panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/setfilename:)*