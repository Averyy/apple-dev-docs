# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [- documentForFileName:](./nsdocumentcontroller/documentforfilename_.md)
  Returns the document object for the file in which the document data is stored.
- [- fileExtensionsFromType:](./nsdocumentcontroller/fileextensionsfromtype_.md)
  Returns the allowable file extensions for the given document type.
- [- fileNamesFromRunningOpenPanel](./nsdocumentcontroller/filenamesfromrunningopenpanel.md)
  Returns a selection of files chosen by the user in the Open panel.
- [- makeUntitledDocumentOfType:](./nsdocumentcontroller/makeuntitleddocumentoftype_.md)
  Creates and returns a document object for document type.
- [- makeDocumentWithContentsOfURL:ofType:](./nsdocumentcontroller/makedocumentwithcontentsofurl_oftype_.md)
  Creates and returns a document object for the given document type from the contents of a given URL.
- [- makeDocumentWithContentsOfFile:ofType:](./nsdocumentcontroller/makedocumentwithcontentsoffile_oftype_.md)
  Creates and returns a document object of a given document type from the contents of a file.
- [- openDocumentWithContentsOfFile:display:](./nsdocumentcontroller/opendocumentwithcontentsoffile_display_.md)
  Returns a document object created from the contents of a given file and optionally displays it.
- [- openDocumentWithContentsOfURL:display:](./nsdocumentcontroller/opendocumentwithcontentsofurl_display_.md)
  Returns a document object created from the contents of a given URL and optionally displays it.
- [- openDocumentWithContentsOfURL:display:error:](./nsdocumentcontroller/opendocumentwithcontentsofurl_display_error_.md)
  Opens a document located by the given URL presents its user interface if requested, and returns the document if successful.
- [- openUntitledDocumentOfType:display:](./nsdocumentcontroller/openuntitleddocumentoftype_display_.md)
  Returns a document object instantiated from the subclass of the given document type and optionally displays it.
- [- reopenDocumentForURL:withContentsOfURL:error:](./nsdocumentcontroller/reopendocumentforurl_withcontentsofurl_error_.md)
  Reopens an autosaved document located by a URL, by reading the contents for the document from another URL, presents its user interface, and returns `true` if successful.
- [- setShouldCreateUI:](./nsdocumentcontroller/setshouldcreateui_.md)
  Sets whether the window controllers of a document should be created when the document is created.
- [- shouldCreateUI](./nsdocumentcontroller/shouldcreateui.md)
  Returns a Boolean value that indicates whether the window controllers of a document should be created when the document is created.
- [- typeFromFileExtension:](./nsdocumentcontroller/typefromfileextension_.md)
  Returns the document type associated with files having extension `fileExtensionOrHFSFileType`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller-deprecated-symbols)*