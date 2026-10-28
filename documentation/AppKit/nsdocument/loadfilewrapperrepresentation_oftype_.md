# loadFileWrapperRepresentation:ofType:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Loads document data from a given file wrapper.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`read(from:ofType:)`](./read%28from,oftype%29-3rzsi.md) instead.

## Declaration

```objc
- (BOOL) loadFileWrapperRepresentation:(NSFileWrapper *) wrapper ofType:(NSString *) type;
```

## Discussion

Loads document data in file wrapper `wrapper` of type `docType` into the receiver, displays it in windows, and returns whether the operation was successful. If `wrapper` is a simple file, it invokes [`loadDataRepresentation:ofType:`](./loaddatarepresentation_oftype_.md) to load the data. If `wrapper` is a directory, it returns [`false`](../../Swift/false.md) by default; subclasses can override to handle file wrappers that are directories. This method is typically invoked by [`readFromFile:ofType:`](./readfromfile_oftype_.md) after it creates an NSData object from the contents of the file.

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
- [- saveToURL:ofType:forSaveOperation:error:](./savetourl_oftype_forsaveoperation_error_.md)
  Saves the contents of the document to a file or file package located by a URL, formatted to a specified type, for a particular kind of save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/loadfilewrapperrepresentation:oftype:)*