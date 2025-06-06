# QLThumbnailRequestSetDocumentObject(_:_:_:)

**Framework**: Quick Look  
**Kind**: func

Stores an object as part of a thumbnail request.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func QLThumbnailRequestSetDocumentObject(_ thumbnail: QLThumbnailRequest!, _ object: UnsafeRawPointer!, _ callbacks: UnsafePointer<CFArrayCallBacks>!)
```

## Parameters

- `thumbnail`: The thumbnail request.
- `object`: The object that you want to associate with the thumbnail request.
- `callbacks`: Callbacks for retaining or releasing the object that you want to store as part of the thumbnail request.

## See Also

- [func QLThumbnailRequestCopyContentUTI(QLThumbnailRequest!) -> Unmanaged<CFString>!](qlthumbnailrequestcopycontentuti(_:).md)
  Returns the UTI for the thumbnail request.
- [func QLThumbnailRequestCopyOptions(QLThumbnailRequest!) -> Unmanaged<CFDictionary>!](qlthumbnailrequestcopyoptions(_:).md)
  Returns the options specified for the thumbnail request.
- [func QLThumbnailRequestCopyURL(QLThumbnailRequest!) -> Unmanaged<CFURL>!](qlthumbnailrequestcopyurl(_:).md)
  Returns the URL of the document for which the thumbnail request is requested.
- [func QLThumbnailRequestCreateContext(QLThumbnailRequest!, CGSize, Bool, CFDictionary!) -> Unmanaged<CGContext>!](qlthumbnailrequestcreatecontext(_:_:_:_:).md)
  Creates a graphics context to draw the thumbnail in.
- [func QLThumbnailRequestFlushContext(QLThumbnailRequest!, CGContext!)](qlthumbnailrequestflushcontext(_:_:).md)
  Flush the graphics context and sets the thumbnail response.
- [func QLThumbnailRequestGetDocumentObject(QLThumbnailRequest!) -> UnsafeRawPointer!](qlthumbnailrequestgetdocumentobject(_:).md)
  Returns the object that’s stored as part of a thumbnail request.
- [func QLThumbnailRequestGetGeneratorBundle(QLThumbnailRequest!) -> Unmanaged<CFBundle>!](qlthumbnailrequestgetgeneratorbundle(_:).md)
  Get the bundle of the generator receiving the thumbnail request.
- [func QLThumbnailRequestGetMaximumSize(QLThumbnailRequest!) -> CGSize](qlthumbnailrequestgetmaximumsize(_:).md)
  Returns the maximum size (in points) specified for the thumbnail image.
- [func QLThumbnailRequestGetTypeID() -> CFTypeID](qlthumbnailrequestgettypeid().md)
  Gets the type identifier for the `QLThumbnailRequest` opaque type.
- [func QLThumbnailRequestIsCancelled(QLThumbnailRequest!) -> Bool](qlthumbnailrequestiscancelled(_:).md)
  Returns whether the thumbnail request has been cancelled by the client.
- [func QLThumbnailRequestSetImage(QLThumbnailRequest!, CGImage!, CFDictionary!)](qlthumbnailrequestsetimage(_:_:_:).md)
  Sets the thumbnail request to a specified image.
- [func QLThumbnailRequestSetImageAtURL(QLThumbnailRequest!, CFURL!, CFDictionary!)](qlthumbnailrequestsetimageaturl(_:_:_:).md)
  Sets the thumbnail request to contain the image at a given URL.
- [func QLThumbnailRequestSetImageWithData(QLThumbnailRequest!, CFData!, CFDictionary!)](qlthumbnailrequestsetimagewithdata(_:_:_:).md)
  Sets the response to the thumbnail request to image data saved within the document.
- [func QLThumbnailRequestSetThumbnailWithDataRepresentation(QLThumbnailRequest!, CFData!, CFString!, CFDictionary!, CFDictionary!)](qlthumbnailrequestsetthumbnailwithdatarepresentation(_:_:_:_:_:).md)
  Sets the default image representation for an item with the provided data and specified file type.
- [func QLThumbnailRequestSetThumbnailWithURLRepresentation(QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CFDictionary!)](qlthumbnailrequestsetthumbnailwithurlrepresentation(_:_:_:_:_:).md)
  Sets the default image representation for an item of a given type at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlthumbnailrequestsetdocumentobject(_:_:_:))*