# QLPreviewRequestSetURLRepresentation(_:_:_:_:)

**Framework**: Quick Look  
**Kind**: func

Sets the contents of the file at the given URL as the response to the preview request.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func QLPreviewRequestSetURLRepresentation(_ preview: QLPreviewRequest!, _ url: CFURL!, _ contentTypeUTI: CFString!, _ properties: CFDictionary!)
```

#### Discussion

This function returns preview data at the given URL to the client. How the Quick Look feature handles the data depends upon the value of the given content type UTI. The content data of the preview must be of a native Quick Look type. Quick Look supports the following UTIs:

- `kUTTypeImage`
- `kUTTypePDF`
- `kUTTypeHTML`
- `kUTTypeXML`
- `kUTTypePlainText`
- `kUTTypeRTF`
- `kUTTypeRTFD`
- `kUTTypeMovie`
- `kUTTypeAudio`

## Parameters

- `preview`: The preview request object.
- `url`: The URL of the file that’s returned as the response to the preview request. The file must be one of the supported file types.
- `contentTypeUTI`: The UTI specifying the content type of the preview.
- `properties`: Additional properties for the preview response.

## See Also

- [func QLPreviewRequestCopyContentUTI(QLPreviewRequest!) -> Unmanaged<CFString>!](qlpreviewrequestcopycontentuti(_:).md)
  Returns the UTI for the preview request.
- [func QLPreviewRequestCopyOptions(QLPreviewRequest!) -> Unmanaged<CFDictionary>!](qlpreviewrequestcopyoptions(_:).md)
  Returns the options specified for the preview request.
- [func QLPreviewRequestCopyURL(QLPreviewRequest!) -> Unmanaged<CFURL>!](qlpreviewrequestcopyurl(_:).md)
  Returns the URL of the document for which a preview is requested.
- [func QLPreviewRequestCreateContext(QLPreviewRequest!, CGSize, Bool, CFDictionary!) -> Unmanaged<CGContext>!](qlpreviewrequestcreatecontext(_:_:_:_:).md)
  Creates a graphics context to draw the preview in.
- [func QLPreviewRequestCreatePDFContext(QLPreviewRequest!, UnsafePointer<CGRect>!, CFDictionary!, CFDictionary!) -> Unmanaged<CGContext>!](qlpreviewrequestcreatepdfcontext(_:_:_:_:).md)
  Creates a PDF context suitable to draw a multi-page preview.
- [func QLPreviewRequestFlushContext(QLPreviewRequest!, CGContext!)](qlpreviewrequestflushcontext(_:_:).md)
  Flush the context and sets the preview response.
- [func QLPreviewRequestGetDocumentObject(QLPreviewRequest!) -> UnsafeRawPointer!](qlpreviewrequestgetdocumentobject(_:).md)
  Returns the object that’s stored as part of a preview request.
- [func QLPreviewRequestSetDocumentObject(QLPreviewRequest!, UnsafeRawPointer!, UnsafePointer<CFArrayCallBacks>!)](qlpreviewrequestsetdocumentobject(_:_:_:).md)
  Stores an object as part of a preview request.
- [func QLPreviewRequestGetGeneratorBundle(QLPreviewRequest!) -> Unmanaged<CFBundle>!](qlpreviewrequestgetgeneratorbundle(_:).md)
  Get the bundle of the generator receiving the preview request.
- [func QLPreviewRequestGetTypeID() -> CFTypeID](qlpreviewrequestgettypeid().md)
  Gets the type identifier for the `QLPreviewReqest` opaque type.
- [func QLPreviewRequestIsCancelled(QLPreviewRequest!) -> Bool](qlpreviewrequestiscancelled(_:).md)
  Returns whether the preview request has been cancelled by the client.
- [func QLPreviewRequestSetDataRepresentation(QLPreviewRequest!, CFData!, CFString!, CFDictionary!)](qlpreviewrequestsetdatarepresentation(_:_:_:_:).md)
  Sets the preview request to data saved within the document or to dynamically generated data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewrequestseturlrepresentation(_:_:_:_:))*