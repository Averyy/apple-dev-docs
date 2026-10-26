# initWithContentsOfFile:ofType:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Initializes and returns a document object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`init(contentsOf:ofType:)`](./init%28contentsof,oftype%29.md) instead.

## Declaration

```objc
- (id) initWithContentsOfFile:(NSString *) absolutePath ofType:(NSString *) typeName;
```

#### Discussion

Initializes and returns an NSDocument object of document type `docType` containing data stored in the file `fileName`. In opening the file, invokes the [`readFromFile:ofType:`](./readfromfile_oftype_.md) method. If the document successfully opens the file, it updates [`fileURL`](./fileurl.md) and [`fileType`](./filetype.md). If the file cannot be opened, or the document is unable to load the contents of the file, this method returns `nil`. This initializer is typically invoked by the `NSDocumentController` method [`makeDocumentWithContentsOfFile:ofType:`](../nsdocumentcontroller/makedocumentwithcontentsoffile_oftype_.md).

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
- [- saveToURL:ofType:forSaveOperation:error:](./savetourl_oftype_forsaveoperation_error_.md)
  Saves the contents of the document to a file or file package located by a URL, formatted to a specified type, for a particular kind of save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/initwithcontentsoffile:oftype:)*