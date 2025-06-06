# QLThumbnailRequestCopyOptions(_:)

**Framework**: Quick Look  
**Kind**: func

Returns the options specified for the thumbnail request.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func QLThumbnailRequestCopyOptions(_ thumbnail: QLThumbnailRequest!) -> Unmanaged<CFDictionary>!
```

#### Return Value

A dictionary containing the options that the client specified for the thumbnail request. See `General Thumbnail Options` for supported options. You should explicitly release the dictionary when it is no longer needed.

#### Discussion

The client sets options in the thumbnail request to give hints to the generator. For macOS 10.5, no options are supported. You should explicitly release the dictionary when it’s no longer needed.

##### Special Considerations

Thread-safety: This function should be called in the same thread as the thumbnail request is made in; generally, this is the same thread in which the `GenerateThumbnailForURL` callback was invoked.

## Parameters

- `thumbnail`: A thumbnail request object.

## See Also

- [func QLThumbnailRequestCopyContentUTI(QLThumbnailRequest!) -> Unmanaged<CFString>!](qlthumbnailrequestcopycontentuti(_:).md)
  Returns the UTI for the thumbnail request.
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
- [func QLThumbnailRequestSetImageWithData(QLThumbnailRequest!, CFData!, CFDictionary!)](qlthumbnailrequestsetimagewithdata(_:_:_:).md)
  Sets the response to the thumbnail request to image data saved within the document.
- [func QLThumbnailRequestSetThumbnailWithDataRepresentation(QLThumbnailRequest!, CFData!, CFString!, CFDictionary!, CFDictionary!)](qlthumbnailrequestsetthumbnailwithdatarepresentation(_:_:_:_:_:).md)
  Sets the default image representation for an item with the provided data and specified file type.
- [func QLThumbnailRequestSetThumbnailWithURLRepresentation(QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CFDictionary!)](qlthumbnailrequestsetthumbnailwithurlrepresentation(_:_:_:_:_:).md)
  Sets the default image representation for an item of a given type at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlthumbnailrequestcopyoptions(_:))*