# QLPreviewRequestCreatePDFContext(_:_:_:_:)

**Framework**: Quick Look  
**Kind**: func

Creates a PDF context suitable to draw a multi-page preview.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func QLPreviewRequestCreatePDFContext(_ preview: QLPreviewRequest!, _ mediaBox: UnsafePointer<CGRect>!, _ auxiliaryInfo: CFDictionary!, _ properties: CFDictionary!) -> Unmanaged<CGContext>!
```

#### Return Value

A reference to a Core Graphics context object that is used to display a PDF version of the preview. You should explicitly release this object when it is no longer needed.

#### Discussion

Be sure to bracket each PDF page written to the context with [`beginPDFPage(_:)`](https://developer.apple.com/documentation/CoreGraphics/CGContext/beginPDFPage(_:)) and [`endPDFPage()`](https://developer.apple.com/documentation/CoreGraphics/CGContext/endPDFPage()) calls. After calling this function, you should flush the context with [`QLPreviewRequestFlushContext(_:_:)`](qlpreviewrequestflushcontext(_:_:).md).

##### Special Considerations

Thread-safety: This function should be called in the same thread as the preview request is made in; generally, this is the same thread in which the `GeneratePreviewForURL` callback was invoked.

## Parameters

- `preview`: The preview request object.
- `mediaBox`: A media box is a rectangle that defines the size and location of the PDF page. The origin of the rectangle should typically be (0,0). If you pass NULL, Quartz uses a default page size of 8.5 by 11 inches (612 by 792 points). For information see the description for  .
- `auxiliaryInfo`: A dictionary containing PDF auxiliary information. See the description of the auxiliary dictionary keys in  doc://com.apple.documentation/documentation/coregraphics/cgpdfcontext  for more information about the keys and values of this dictionary.
- `properties`: A dictionary containing additional properties for the preview response. For information on acceptable keys and values, see  .

## See Also

- [func QLPreviewRequestCopyContentUTI(QLPreviewRequest!) -> Unmanaged<CFString>!](qlpreviewrequestcopycontentuti(_:).md)
  Returns the UTI for the preview request.
- [func QLPreviewRequestCopyOptions(QLPreviewRequest!) -> Unmanaged<CFDictionary>!](qlpreviewrequestcopyoptions(_:).md)
  Returns the options specified for the preview request.
- [func QLPreviewRequestCopyURL(QLPreviewRequest!) -> Unmanaged<CFURL>!](qlpreviewrequestcopyurl(_:).md)
  Returns the URL of the document for which a preview is requested.
- [func QLPreviewRequestCreateContext(QLPreviewRequest!, CGSize, Bool, CFDictionary!) -> Unmanaged<CGContext>!](qlpreviewrequestcreatecontext(_:_:_:_:).md)
  Creates a graphics context to draw the preview in.
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
- [func QLPreviewRequestSetURLRepresentation(QLPreviewRequest!, CFURL!, CFString!, CFDictionary!)](qlpreviewrequestseturlrepresentation(_:_:_:_:).md)
  Sets the contents of the file at the given URL as the response to the preview request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewrequestcreatepdfcontext(_:_:_:_:))*