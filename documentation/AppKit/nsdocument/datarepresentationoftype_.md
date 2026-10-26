# dataRepresentationOfType:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

A primitive method to return a data object that represents the data of the receiver in a given type.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`data(ofType:)`](./data%28oftype%29.md) instead.

## Declaration

```objc
- (NSData *) dataRepresentationOfType:(NSString *) type;
```

#### Discussion

A primitive method overridden by subclasses to return a data object that represents the data of the receiver in a given type (`aType`). The default implementation `raises` an `NSInternalInconsistencyException`. This method is invoked by the default implementation of `fileWrapperRepresentationOfType:.`

`aType` is the type name corresponding to the value of the `CFBundleTypeName` entry in the document type’s `Info.plist` dictionary.

Here is a typical implementation:

```objc
//Document type name
NSString *MyDocumentType = @"Rich Text Format (RTF) document";
 
...
 
- (NSData *)dataRepresentationOfType:(NSString *)aType {
    NSAssert([aType isEqualToString:MyDocumentType], @"Unknown  type");
    return [textView RTFFromRange:NSMakeRange(0, [[textView textStorage]  length])];
}
```

## See Also

### Deprecated methods
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
- [- saveToURL:ofType:forSaveOperation:error:](./savetourl_oftype_forsaveoperation_error_.md)
  Saves the contents of the document to a file or file package located by a URL, formatted to a specified type, for a particular kind of save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/datarepresentationoftype:)*