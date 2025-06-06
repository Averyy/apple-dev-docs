# QLThumbnailRequestSetImageWithData(_:_:_:)

**Framework**: Quick Look  
**Kind**: func

Sets the response to the thumbnail request to image data saved within the document.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func QLThumbnailRequestSetImageWithData(_ thumbnail: QLThumbnailRequest!, _ data: CFData!, _ properties: CFDictionary!)
```

#### Discussion

This function returns the thumbnail as a `CFData` object containing image data. The document’s application must save this data as part of the document’s data; the generator retrieves it and uses this function to return it to the client. Before you call this function, call [`QLThumbnailRequestGetMaximumSize(_:)`](qlthumbnailrequestgetmaximumsize(_:).md) to obtain the maximum allowed size for the thumbnail and resize the image if necessary.

##### Special Considerations

Thread-safety: This function should be called in the same thread as the thumbnail request is made in; generally, this is the same thread in which the `GenerateThumbnailForURL` callback was invoked.

## Parameters

- `thumbnail`: The thumbnail request object.
- `data`: The image data, which must be in a format supported by the Image I/O framework (JPG, PNG, and so on). In other words, a content type of   is assumed. (  is a subframework of the umbrella Application Services framework.)
- `properties`: A dictionary of properties. The only property that you can currently specify is kCGImageSourceTypeIdentifierHint; see   for information about this property.

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
- [func QLThumbnailRequestSetDocumentObject(QLThumbnailRequest!, UnsafeRawPointer!, UnsafePointer<CFArrayCallBacks>!)](qlthumbnailrequestsetdocumentobject(_:_:_:).md)
  Stores an object as part of a thumbnail request.
- [func QLThumbnailRequestSetImage(QLThumbnailRequest!, CGImage!, CFDictionary!)](qlthumbnailrequestsetimage(_:_:_:).md)
  Sets the thumbnail request to a specified image.
- [func QLThumbnailRequestSetImageAtURL(QLThumbnailRequest!, CFURL!, CFDictionary!)](qlthumbnailrequestsetimageaturl(_:_:_:).md)
  Sets the thumbnail request to contain the image at a given URL.
- [func QLThumbnailRequestSetThumbnailWithDataRepresentation(QLThumbnailRequest!, CFData!, CFString!, CFDictionary!, CFDictionary!)](qlthumbnailrequestsetthumbnailwithdatarepresentation(_:_:_:_:_:).md)
  Sets the default image representation for an item with the provided data and specified file type.
- [func QLThumbnailRequestSetThumbnailWithURLRepresentation(QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CFDictionary!)](qlthumbnailrequestsetthumbnailwithurlrepresentation(_:_:_:_:_:).md)
  Sets the default image representation for an item of a given type at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlthumbnailrequestsetimagewithdata(_:_:_:))*