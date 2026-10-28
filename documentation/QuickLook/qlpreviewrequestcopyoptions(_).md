# QLPreviewRequestCopyOptions(_:)

**Framework**: Quick Look  
**Kind**: func  
**Role**: Function

Returns the options specified for the preview request.

**Availability**:
- macOS 10.0+ - Deprecated in 12.0

> **Deprecated**: Use a QLPreviewingController in a Preview Extension to provide previews for your file types.

## Declaration

```swift
func QLPreviewRequestCopyOptions(_ preview: QLPreviewRequest!) -> Unmanaged<CFDictionary>!
```

```c
extern CFDictionaryRefQLPreviewRequestCopyOptions(QLPreviewRequestRef preview);
```

## Return Value

A dictionary containing the properties specified for the preview request. See `Preview Properties` for supported options. You should explicitly release this object when it is no longer needed.

## Discussion

The client sets options in the preview request to give hints to the generator. For macOS 10.5, no options are supported.

### Special Considerations

Thread-safety: This function should be called in the same thread as the preview request is made in; generally, this is the same thread in which the `GeneratePreviewForURL` callback was invoked.

## Parameters

- `preview`: A preview request object.

## See Also

### Requesting previews
- [func QLPreviewRequestCopyContentUTI(QLPreviewRequest!) -> Unmanaged<CFString>!](./qlpreviewrequestcopycontentuti%28_%29.md)
  Returns the UTI for the preview request.
- [func QLPreviewRequestCopyURL(QLPreviewRequest!) -> Unmanaged<CFURL>!](./qlpreviewrequestcopyurl%28_%29.md)
  Returns the URL of the document for which a preview is requested.
- [func QLPreviewRequestCreateContext(QLPreviewRequest!, CGSize, Bool, CFDictionary!) -> Unmanaged<CGContext>!](./qlpreviewrequestcreatecontext%28_,_,_,_%29.md)
  Creates a graphics context to draw the preview in.
- [func QLPreviewRequestCreatePDFContext(QLPreviewRequest!, UnsafePointer<CGRect>!, CFDictionary!, CFDictionary!) -> Unmanaged<CGContext>!](./qlpreviewrequestcreatepdfcontext%28_,_,_,_%29.md)
  Creates a PDF context suitable to draw a multi-page preview.
- [func QLPreviewRequestFlushContext(QLPreviewRequest!, CGContext!)](./qlpreviewrequestflushcontext%28_,_%29.md)
  Flush the context and sets the preview response.
- [func QLPreviewRequestGetDocumentObject(QLPreviewRequest!) -> UnsafeRawPointer!](./qlpreviewrequestgetdocumentobject%28_%29.md)
  Returns the object that’s stored as part of a preview request.
- [func QLPreviewRequestSetDocumentObject(QLPreviewRequest!, UnsafeRawPointer!, UnsafePointer<CFArrayCallBacks>!)](./qlpreviewrequestsetdocumentobject%28_,_,_%29.md)
  Stores an object as part of a preview request.
- [func QLPreviewRequestGetGeneratorBundle(QLPreviewRequest!) -> Unmanaged<CFBundle>!](./qlpreviewrequestgetgeneratorbundle%28_%29.md)
  Get the bundle of the generator receiving the preview request.
- [func QLPreviewRequestGetTypeID() -> CFTypeID](./qlpreviewrequestgettypeid%28%29.md)
  Gets the type identifier for the `QLPreviewReqest` opaque type.
- [func QLPreviewRequestIsCancelled(QLPreviewRequest!) -> Bool](./qlpreviewrequestiscancelled%28_%29.md)
  Returns whether the preview request has been cancelled by the client.
- [func QLPreviewRequestSetDataRepresentation(QLPreviewRequest!, CFData!, CFString!, CFDictionary!)](./qlpreviewrequestsetdatarepresentation%28_,_,_,_%29.md)
  Sets the preview request to data saved within the document or to dynamically generated data.
- [func QLPreviewRequestSetURLRepresentation(QLPreviewRequest!, CFURL!, CFString!, CFDictionary!)](./qlpreviewrequestseturlrepresentation%28_,_,_,_%29.md)
  Sets the contents of the file at the given URL as the response to the preview request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewrequestcopyoptions(_:))*