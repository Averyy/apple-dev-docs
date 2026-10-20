# QLPreviewRequestCopyURL(_:)

**Framework**: Quick Look  
**Kind**: func  
**Role**: Function

Returns the URL of the document for which a preview is requested.

**Availability**:
- macOS 10.0+ - Deprecated in 12.0

> **Deprecated**: Use a QLPreviewingController in a Preview Extension to provide previews for your file types.

## Declaration

```swift
func QLPreviewRequestCopyURL(_ preview: QLPreviewRequest!) -> Unmanaged<CFURL>!
```

```c
extern CFURLRefQLPreviewRequestCopyURL(QLPreviewRequestRef preview);
```

#### Return Value

The URL identifying the file for which the preview is requested.

#### Discussion

This function is thread safe.

## Parameters

- `preview`: The preview request object.

## See Also

### Requesting previews
- [func QLPreviewRequestCopyContentUTI(QLPreviewRequest!) -> Unmanaged<CFString>!](./qlpreviewrequestcopycontentuti%28_%29.md)
  Returns the UTI for the preview request.
- [func QLPreviewRequestCopyOptions(QLPreviewRequest!) -> Unmanaged<CFDictionary>!](./qlpreviewrequestcopyoptions%28_%29.md)
  Returns the options specified for the preview request.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewrequestcopyurl(_:))*