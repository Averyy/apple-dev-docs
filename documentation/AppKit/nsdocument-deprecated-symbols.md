# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated properties
- [var shouldRunSavePanelWithAccessoryView: Bool](./nsdocument/shouldrunsavepanelwithaccessoryview.md)
  A Boolean value that indicates whether the document’s Save panel displays a list of supported writable document types.
### Deprecated methods
- [- dataRepresentationOfType:](./nsdocument/datarepresentationoftype_.md)
  A primitive method to return a data object that represents the data of the receiver in a given type.
- [- fileAttributesToWriteToFile:ofType:saveOperation:](./nsdocument/fileattributestowritetofile_oftype_saveoperation_.md)
  Returns the file attributes that should be written to the named document file of the specified type.
- [- fileName](./nsdocument/filename.md)
  Returns the fully qualified pathname under which the receiver has been saved.
- [- fileWrapperRepresentationOfType:](./nsdocument/filewrapperrepresentationoftype_.md)
  Returns a file wrapper object that represents the data of the receiver in a given type.
- [- initWithContentsOfFile:ofType:](./nsdocument/initwithcontentsoffile_oftype_.md)
  Initializes and returns a document object.
- [- initWithContentsOfURL:ofType:](./nsdocument/initwithcontentsofurl_oftype_.md)
  Initializes and returns a document object of a given type.
- [- loadDataRepresentation:ofType:](./nsdocument/loaddatarepresentation_oftype_.md)
  Loads the document data.
- [- loadFileWrapperRepresentation:ofType:](./nsdocument/loadfilewrapperrepresentation_oftype_.md)
  Loads document data from a given file wrapper.
- [- printShowingPrintPanel:](./nsdocument/printshowingprintpanel_.md)
  Prints the current document’s data.
- [- readFromFile:ofType:](./nsdocument/readfromfile_oftype_.md)
  Reads and loads document data of the given type from the given file.
- [- readFromURL:ofType:](./nsdocument/readfromurl_oftype_.md)
  Reads and loads document data.
- [- revertToSavedFromFile:ofType:](./nsdocument/reverttosavedfromfile_oftype_.md)
  Reverts the receiver to the data stored in the file system.
- [- revertToSavedFromURL:ofType:](./nsdocument/reverttosavedfromurl_oftype_.md)
  Reverts the receiver.
- [- runModalPageLayoutWithPrintInfo:](./nsdocument/runmodalpagelayoutwithprintinfo_.md)
  Runs the page layout modal panel with the receiver’s printing information object.
- [- saveToFile:saveOperation:delegate:didSaveSelector:contextInfo:](./nsdocument/savetofile_saveoperation_delegate_didsaveselector_contextinfo_.md)
  Called after the user has been given the opportunity to select a destination through the modal Save panel.
- [- saveToURL:ofType:forSaveOperation:error:](./nsdocument/savetourl_oftype_forsaveoperation_error_.md)
  Saves the contents of the document to a file or file package located by a URL, formatted to a specified type, for a particular kind of save operation.
- [- setFileName:](./nsdocument/setfilename_.md)
  Sets the file (filename and directory path) under which document data is saved.
- [- writeToFile:ofType:](./nsdocument/writetofile_oftype_.md)
  Writes document data to a file.
- [- writeToFile:ofType:originalFile:saveOperation:](./nsdocument/writetofile_oftype_originalfile_saveoperation_.md)
  Writes the receiver document’s contents to a file.
- [- writeToURL:ofType:](./nsdocument/writetourl_oftype_.md)
  Writes document data to a URL.
- [- writeWithBackupToFile:ofType:saveOperation:](./nsdocument/writewithbackuptofile_oftype_saveoperation_.md)
  This method is called by action methods to save document contents to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument-deprecated-symbols)*