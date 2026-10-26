# readFromFile:ofType:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Reads and loads document data of the given type from the given file.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`read(from:ofType:)`](./read%28from,oftype%29-1vttv.md) instead.

## Declaration

```objc
- (BOOL) readFromFile:(NSString *) fileName ofType:(NSString *) type;
```

#### Discussion

Reads and loads document data of type `docType` from the file `fileName`, returning whether the operation was successful. This method invokes `loadDataRepresentation:ofType:` and is invoked when the receiver is first created and initialized by `initWithContentsOfFile:ofType:`. It uses `NSData` [`init(contentsOfFile:)`](../../Foundation/nsdata/init%28contentsoffile%29.md) to get the document data.

This method is one of the location-based primitives. Subclasses can override this method instead of overriding `loadDataRepresentation:ofType:` to read and load document data. Subclasses that handle file packages such as RTFD or that treat locations of files as anything other than paths should override this method. Override implementations of this method can filter the document data using `NSPasteboard` or other filtering services.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/readfromfile:oftype:)*