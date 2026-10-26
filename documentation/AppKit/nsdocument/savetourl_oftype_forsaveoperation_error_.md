# saveToURL:ofType:forSaveOperation:error:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Saves the contents of the document to a file or file package located by a URL, formatted to a specified type, for a particular kind of save operation.

**Availability**:
- macOS 10.4+ - Deprecated in 10.6

> **Deprecated**: Use [`save(to:ofType:for:completionHandler:)`](./save%28to,oftype,for,completionhandler%29.md) instead.

## Declaration

```objc
- (BOOL) saveToURL:(NSURL *) url ofType:(NSString *) typeName forSaveOperation:(NSSaveOperationType) saveOperation error:(NSError **) outError;
```

#### Return Value

[`true`](../../Swift/true.md) if the document contents were successfully saved; otherwise, [`false`](../../Swift/false.md).

#### Discussion

You can override this method to do things that need to be done before or after any save operation. If you override this method, you must call `super` at some point in your implementation.

## Parameters

- `url`: The location of the file or file package to which the document contents are saved.
- `typeName`: The string that identifies the document type.
- `saveOperation`: The type of save operation.
- `outError`: On return, if the document contents could not be saved, a pointer to an error object that encapsulates the reason they could not be saved.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/savetourl:oftype:forsaveoperation:error:)*