# fileNamesFromRunningOpenPanel

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a selection of files chosen by the user in the Open panel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`urlsFromRunningOpenPanel()`](./urlsfromrunningopenpanel%28%29.md) instead.

## Declaration

```objc
- (NSArray *) fileNamesFromRunningOpenPanel;
```

#### Discussion

Each file in the returned `NSArray` is a fully qualified path to the file’s location in the file system. This method is called by [`openDocument(_:)`](./opendocument%28_%29.md), and it calls [`runModalOpenPanel(_:forTypes:)`](./runmodalopenpanel%28_,fortypes%29.md) after initializing the Open panel (which includes getting the starting directory with [`currentDirectory`](./currentdirectory.md)). Returns `nil` if the user cancels the Open panel or makes no selection.

## See Also

### Deprecated methods
- [- documentForFileName:](./documentforfilename_.md)
  Returns the document object for the file in which the document data is stored.
- [- fileExtensionsFromType:](./fileextensionsfromtype_.md)
  Returns the allowable file extensions for the given document type.
- [- makeUntitledDocumentOfType:](./makeuntitleddocumentoftype_.md)
  Creates and returns a document object for document type.
- [- makeDocumentWithContentsOfURL:ofType:](./makedocumentwithcontentsofurl_oftype_.md)
  Creates and returns a document object for the given document type from the contents of a given URL.
- [- makeDocumentWithContentsOfFile:ofType:](./makedocumentwithcontentsoffile_oftype_.md)
  Creates and returns a document object of a given document type from the contents of a file.
- [- openDocumentWithContentsOfFile:display:](./opendocumentwithcontentsoffile_display_.md)
  Returns a document object created from the contents of a given file and optionally displays it.
- [- openDocumentWithContentsOfURL:display:](./opendocumentwithcontentsofurl_display_.md)
  Returns a document object created from the contents of a given URL and optionally displays it.
- [- openDocumentWithContentsOfURL:display:error:](./opendocumentwithcontentsofurl_display_error_.md)
  Opens a document located by the given URL presents its user interface if requested, and returns the document if successful.
- [- openUntitledDocumentOfType:display:](./openuntitleddocumentoftype_display_.md)
  Returns a document object instantiated from the subclass of the given document type and optionally displays it.
- [- reopenDocumentForURL:withContentsOfURL:error:](./reopendocumentforurl_withcontentsofurl_error_.md)
  Reopens an autosaved document located by a URL, by reading the contents for the document from another URL, presents its user interface, and returns `true` if successful.
- [- setShouldCreateUI:](./setshouldcreateui_.md)
  Sets whether the window controllers of a document should be created when the document is created.
- [- shouldCreateUI](./shouldcreateui.md)
  Returns a Boolean value that indicates whether the window controllers of a document should be created when the document is created.
- [- typeFromFileExtension:](./typefromfileextension_.md)
  Returns the document type associated with files having extension `fileExtensionOrHFSFileType`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/filenamesfromrunningopenpanel)*