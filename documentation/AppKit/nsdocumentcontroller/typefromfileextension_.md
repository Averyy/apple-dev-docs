# typeFromFileExtension:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the document type associated with files having extension `fileExtensionOrHFSFileType`.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Use [`typeForContents(of:)`](./typeforcontents%28of%29.md) instead.

## Declaration

```objc
- (NSString *) typeFromFileExtension:(NSString *) fileNameExtensionOrHFSFileType;
```

#### Discussion

The  `fileExtensionOrHFSFileType` parameter may also be an encoded HFS file type, as well as a filename extension.

This method only works when passed a file name extension used in a `CFBundleDocumentTypes` entry that does not have an `LSItemContentTypes` subentry.

## See Also

### Deprecated methods
- [- documentForFileName:](./documentforfilename_.md)
  Returns the document object for the file in which the document data is stored.
- [- fileExtensionsFromType:](./fileextensionsfromtype_.md)
  Returns the allowable file extensions for the given document type.
- [- fileNamesFromRunningOpenPanel](./filenamesfromrunningopenpanel.md)
  Returns a selection of files chosen by the user in the Open panel.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/typefromfileextension:)*