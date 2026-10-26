# openDocumentWithContentsOfURL:display:error:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Opens a document located by the given URL presents its user interface if requested, and returns the document if successful.

**Availability**:
- macOS 10.4+ - Deprecated in 10.7

> **Deprecated**: Use [`openDocument(withContentsOf:display:completionHandler:)`](./opendocument%28withcontentsof,display,completionhandler%29.md) instead.

## Declaration

```objc
- (id) openDocumentWithContentsOfURL:(NSURL *) url display:(BOOL) displayDocument error:(NSError **) outError;
```

#### Discussion

If not  successful, the method returns `nil` after setting `outError` to point to an `NSError` object that encapsulates the reason why the document could not be opened.

The default implementation of this method checks to see if the document is already open according to [`document(for:)`](./document%28for%29-i5zi.md), and if it is not open determines the type of the document, calls [`makeDocument(withContentsOf:ofType:)`](./makedocument%28withcontentsof,oftype%29.md) to instantiate it, then calls [`addDocument(_:)`](./adddocument%28_%29.md) to record its opening, and sends the document [`makeWindowControllers()`](../nsdocument/makewindowcontrollers%28%29.md) and [`showWindows()`](../nsdocument/showwindows%28%29.md) messages if `displayDocument` is [`true`](../../Swift/true.md). If the document is already open it is just sent a [`showWindows()`](../nsdocument/showwindows%28%29.md) message if `displayDocument` is [`true`](../../Swift/true.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/opendocumentwithcontentsofurl:display:error:)*