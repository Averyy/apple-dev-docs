# writeToFile:ofType:originalFile:saveOperation:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Writes the receiver document’s contents to a file.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`write(to:ofType:for:originalContentsURL:)`](./write%28to,oftype,for,originalcontentsurl%29.md) instead.

## Declaration

```objc
- (BOOL) writeToFile:(NSString *) fullDocumentPath ofType:(NSString *) documentTypeName originalFile:(NSString *) fullOriginalDocumentPath saveOperation:(NSSaveOperationType) saveOperationType;
```

## Discussion

This method is called from [`writeWithBackupToFile:ofType:saveOperation:`](./writewithbackuptofile_oftype_saveoperation_.md) to actually write the file of type `docType` to `fullDocumentPath`. `fullOriginalDocumentPath` is the path to the original file if there is one and `nil` otherwise. The default implementation simply calls [`writeToFile:ofType:`](./writetofile_oftype_.md). You should not need to call this method directly, but subclasses that need access to the previously saved copy of their document while saving the new one can override this method. The `saveOperationType` argument is one of the constants listed in `Constants`.

See [Document Saving Behavior](../nsdocument.md#Document-Saving-Behavior) for additional information about saving documents.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/writetofile:oftype:originalfile:saveoperation:)*