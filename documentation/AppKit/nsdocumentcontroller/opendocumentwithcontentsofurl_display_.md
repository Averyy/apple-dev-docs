# openDocumentWithContentsOfURL:display:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a document object created from the contents of a given URL and optionally displays it.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`openDocument(withContentsOf:display:completionHandler:)`](./opendocument%28withcontentsof,display,completionhandler%29.md) instead.

## Declaration

```objc
- (id) openDocumentWithContentsOfURL:(NSURL *) url display:(BOOL) display;
```

## Discussion

Returns an `NSDocument` object created from the contents of `aURL` and displays it if `flag` is [`true`](../../Swift/true.md). The returned object is not retained, but is added to the receiver’s list of managed documents. Returns `nil` if the object could not be created, typically because `aURL` does not point to a valid location or because there is no `NSDocument` subclass for the document type. Even if `flag` is [`true`](../../Swift/true.md), the document is not displayed if [`shouldCreateUI`](./shouldcreateui.md) returns [`false`](../../Swift/false.md). This method calls [`makeDocumentWithContentsOfURL:ofType:`](./makedocumentwithcontentsofurl_oftype_.md) to obtain the created `NSDocument` object.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/opendocumentwithcontentsofurl:display:)*