# QLPreviewRequestCreateContext(_:_:_:_:)

**Framework**: Quick Look  
**Kind**: func

Creates a graphics context to draw the preview in.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func QLPreviewRequestCreateContext(_ preview: QLPreviewRequest!, _ size: CGSize, _ isBitmap: Bool, _ properties: CFDictionary!) -> Unmanaged<CGContext>!
```

#### Return Value

A Core Graphics graphics-context object that you can draw your preview image in. You should explicitly release this object when it is no longer needed.

#### Discussion

You can directly draw your preview data in the graphics-context object created by this function. After calling this function, you should flush the context with [`QLPreviewRequestFlushContext(_:_:)`](qlpreviewrequestflushcontext(_:_:).md). Also be sure to release the `CGContext` object.

Quick Look provides three types of graphics contexts for drawing previews: bitmap, single-page vector-based, and multi-page vector-based (for PDF previews). You use this function to acquire a context for bitmap and single-page vector drawing; the `isBitmap` parameter is used to distinguish between them. For multi-page contexts, use the [`QLPreviewRequestCreatePDFContext(_:_:_:_:)`](qlpreviewrequestcreatepdfcontext(_:_:_:_:).md) function.

If you prefer to work in Objective-C code, you can convert the created [`CGContext`](https://developer.apple.com/documentation/CoreGraphics/CGContext) to a [`NSGraphicsContext`](https://developer.apple.com/documentation/AppKit/NSGraphicsContext) object using [`init(graphicsPort:flipped:)`](https://developer.apple.com/documentation/AppKit/NSGraphicsContext/init(graphicsPort:flipped:)).

##### Special Considerations

Thread-safety: This function should be called in the same thread as the preview request is made in; generally, this is the same thread in which the `GeneratePreviewForURL` callback was invoked.

## Parameters

- `preview`: The preview request object.
- `size`: The size of the preview; if   is   the size is in pixels, otherwise it’s in points.
- `isBitmap`:   if the preview uses a bitmap-based graphics context,   otherwise. This value of this parameter affects the interpretation of the   parameter.
- `properties`: A dictionary containing properties for the preview response.   lists the current property keys and describes their values.

## See Also

- [func QLPreviewRequestCopyContentUTI(QLPreviewRequest!) -> Unmanaged<CFString>!](qlpreviewrequestcopycontentuti(_:).md)
  Returns the UTI for the preview request.
- [func QLPreviewRequestCopyOptions(QLPreviewRequest!) -> Unmanaged<CFDictionary>!](qlpreviewrequestcopyoptions(_:).md)
  Returns the options specified for the preview request.
- [func QLPreviewRequestCopyURL(QLPreviewRequest!) -> Unmanaged<CFURL>!](qlpreviewrequestcopyurl(_:).md)
  Returns the URL of the document for which a preview is requested.
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
- [func QLPreviewRequestSetURLRepresentation(QLPreviewRequest!, CFURL!, CFString!, CFDictionary!)](qlpreviewrequestseturlrepresentation(_:_:_:_:).md)
  Sets the contents of the file at the given URL as the response to the preview request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewrequestcreatecontext(_:_:_:_:))*