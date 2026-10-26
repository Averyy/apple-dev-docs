# loadDataRepresentation:ofType:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Loads the document data.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`read(from:ofType:)`](./read%28from,oftype%29-6g6ai.md) instead.

## Declaration

```objc
- (BOOL) loadDataRepresentation:(NSData *) data ofType:(NSString *) type;
```

#### Discussion

Overridden by subclasses to load document data (`docData`) of type `docType` into the receiver, display it in windows, and return whether the operation was successful. This method is typically invoked by [`loadFileWrapperRepresentation:ofType:`](./loadfilewrapperrepresentation_oftype_.md) after an `NSData` object is created from the contents of the file wrapper (which can include directories). The default implementation `raises` an `NSInternalInconsistencyException`. Subclasses must override this method unless they override [`readFromFile:ofType:`](./readfromfile_oftype_.md) or [`loadFileWrapperRepresentation:ofType:`](./loadfilewrapperrepresentation_oftype_.md) to do specialized reading and loading of document data.

The `docType` argument is the type name corresponding to the value of the `CFBundleTypeName` entry in the document type’s `Info.plist` dictionary.

Here is an example implementation:

```objc
//Document type name
NSString *MyDocumentType = @"Rich Text Format (RTF) document";
 
...
 
- (BOOL)loadDataRepresentation:(NSData *)data ofType:(NSString *)aType  {
    NSAssert([aType isEqualToString: MyDocumentType], @"Unknown  type");
    fileContents = [data copyWithZone:[self zone]];
    return YES;
}
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/loaddatarepresentation:oftype:)*