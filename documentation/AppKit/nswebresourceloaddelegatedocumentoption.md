# NSWebResourceLoadDelegateDocumentOption

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

An object to serve as the web resource loading delegate.

**Availability**:
- macOS

## Declaration

```c
extern NSAttributedStringDocumentReadingOptionKey NSWebResourceLoadDelegateDocumentOption;
```

## Discussion

For HTML only. The value is an [`NSObject`](../ObjectiveC/nsobject-swift.class.md).

If not present, a default delegate is used that permits the loading of subsidiary resources but does not respond to authentication challenges. The previous string constant was `@"WebResourceLoadDelegate"`.

## See Also

### Getting the document options
- [NSBaseURLDocumentOption](./nsbaseurldocumentoption.md)
  The base URL for HTML documents.
- [NSCharacterEncodingDocumentOption](./nscharacterencodingdocumentoption.md)
  The string encoding.
- [NSDefaultAttributesDocumentOption](./nsdefaultattributesdocumentoption.md)
  The default attributes to apply to plain files.
- [NSDocumentTypeDocumentOption](./nsdocumenttypedocumentoption.md)
  The document type.
- [NSFileTypeDocumentOption](./nsfiletypedocumentoption.md)
  The file type.
- [NSTextEncodingNameDocumentOption](./nstextencodingnamedocumentoption.md)
  The text encoding to use.
- [NSTextSizeMultiplierDocumentOption](./nstextsizemultiplierdocumentoption.md)
  The scale factor for font sizes.
- [NSTimeoutDocumentOption](./nstimeoutdocumentoption.md)
  The time, in seconds, to wait for a document to finish loading.
- [NSWebPreferencesDocumentOption](./nswebpreferencesdocumentoption.md)
  A WebPreferences object.
- [NSTextKit1ListMarkerFormatDocumentOption](./nstextkit1listmarkerformatdocumentoption.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswebresourceloaddelegatedocumentoption)*