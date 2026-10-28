# writeToFile:ofType:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Writes document data to a file.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`write(to:ofType:)`](./write%28to,oftype%29.md) instead.

## Declaration

```objc
- (BOOL) writeToFile:(NSString *) fileName ofType:(NSString *) type;
```

## Discussion

Writes document data of type `docType` to the file `fileName`, returning whether the operation was successful. This method invokes [`dataRepresentationOfType:`](./datarepresentationoftype_.md) and is indirectly invoked whenever the document file is saved. It uses the `NSData` method [`write(toFile:atomically:)`](../../Foundation/nsdata/write%28tofile,atomically%29.md) to write to the file.

This method is one of the location-based primitives. Subclasses can override this method instead of overriding `dataRepresentationOfType:` to write document data to the file system as an `NSData` object after creating that object from internal data structures. Subclasses that handle file packages such as RTFD or that treat locations of files as anything other than paths should override this method. Override implementations of this method should ensure that they filter document data appropriately using `NSPasteboard` filtering services.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/writetofile:oftype:)*