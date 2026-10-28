# saveToFile:saveOperation:delegate:didSaveSelector:contextInfo:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called after the user has been given the opportunity to select a destination through the modal Save panel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`save(to:ofType:for:delegate:didSave:contextInfo:)`](./save%28to,oftype,for,delegate,didsave,contextinfo%29.md) instead.

## Declaration

```objc
- (void) saveToFile:(NSString *) fileName saveOperation:(NSSaveOperationType) saveOperation delegate:(id) delegate didSaveSelector:(SEL) didSaveSelector contextInfo:(void *) contextInfo;
```

## Discussion

Called after the user has been given the opportunity to select a destination through the modal Save panel presented by [`runModalSavePanel(for:delegate:didSave:contextInfo:)`](./runmodalsavepanel%28for,delegate,didsave,contextinfo%29.md). The `delegate` is assigned to the Save panel. If `fileName` is non-`nil`, this method writes the document to `fileName`, sets the document’s file location and document type (if a native type), and clears the document’s edited status. `didSaveSelector` gets called with [`true`](../../Swift/true.md) if the document is saved successfully, and [`false`](../../Swift/false.md) otherwise. The `saveOperation` is one of the constants in `Constants`. Pass `contextInfo` with the callback.

The `didSaveSelector` callback method should have the following signature:

```objc
- (void)document:(NSDocument *)doc didSave:(BOOL)didSave contextInfo:(void  *)contextInfo
```

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
- [- saveToURL:ofType:forSaveOperation:error:](./savetourl_oftype_forsaveoperation_error_.md)
  Saves the contents of the document to a file or file package located by a URL, formatted to a specified type, for a particular kind of save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/savetofile:saveoperation:delegate:didsaveselector:contextinfo:)*