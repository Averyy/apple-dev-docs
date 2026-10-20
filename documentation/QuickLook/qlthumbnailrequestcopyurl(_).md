# QLThumbnailRequestCopyURL(_:)

**Framework**: Quick Look  
**Kind**: func  
**Role**: Function

Returns the URL of the document for which the thumbnail request is requested.

**Availability**:
- macOS 10.0+ - Deprecated in 12.0

> **Deprecated**: Use a QLFileThumbnailRequest in a Thumbnail Extension to provide thumbnails for your file types.

## Declaration

```swift
func QLThumbnailRequestCopyURL(_ thumbnail: QLThumbnailRequest!) -> Unmanaged<CFURL>!
```

```c
extern CFURLRefQLThumbnailRequestCopyURL(QLThumbnailRequestRef thumbnail);
```

#### Return Value

The URL identifying the document for which the thumbnail is requested. You should explicitly release the CFURL object when it is no longer needed.

#### Discussion

Thread-safety: This function should be called in the same thread as the thumbnail request is made in; generally, this is the same thread in which the `GenerateThumbnailForURL` callback was invoked.

## Parameters

- `thumbnail`: The thumbnail request object.

## See Also

### Handling thumbnail requests
- [func QLThumbnailRequestCopyContentUTI(QLThumbnailRequest!) -> Unmanaged<CFString>!](./qlthumbnailrequestcopycontentuti%28_%29.md)
  Returns the UTI for the thumbnail request.
- [func QLThumbnailRequestCopyOptions(QLThumbnailRequest!) -> Unmanaged<CFDictionary>!](./qlthumbnailrequestcopyoptions%28_%29.md)
  Returns the options specified for the thumbnail request.
- [func QLThumbnailRequestCreateContext(QLThumbnailRequest!, CGSize, Bool, CFDictionary!) -> Unmanaged<CGContext>!](./qlthumbnailrequestcreatecontext%28_,_,_,_%29.md)
  Creates a graphics context to draw the thumbnail in.
- [func QLThumbnailRequestFlushContext(QLThumbnailRequest!, CGContext!)](./qlthumbnailrequestflushcontext%28_,_%29.md)
  Flush the graphics context and sets the thumbnail response.
- [func QLThumbnailRequestGetDocumentObject(QLThumbnailRequest!) -> UnsafeRawPointer!](./qlthumbnailrequestgetdocumentobject%28_%29.md)
  Returns the object that’s stored as part of a thumbnail request.
- [func QLThumbnailRequestGetGeneratorBundle(QLThumbnailRequest!) -> Unmanaged<CFBundle>!](./qlthumbnailrequestgetgeneratorbundle%28_%29.md)
  Get the bundle of the generator receiving the thumbnail request.
- [func QLThumbnailRequestGetMaximumSize(QLThumbnailRequest!) -> CGSize](./qlthumbnailrequestgetmaximumsize%28_%29.md)
  Returns the maximum size (in points) specified for the thumbnail image.
- [func QLThumbnailRequestGetTypeID() -> CFTypeID](./qlthumbnailrequestgettypeid%28%29.md)
  Gets the type identifier for the `QLThumbnailRequest` opaque type.
- [func QLThumbnailRequestIsCancelled(QLThumbnailRequest!) -> Bool](./qlthumbnailrequestiscancelled%28_%29.md)
  Returns whether the thumbnail request has been cancelled by the client.
- [func QLThumbnailRequestSetDocumentObject(QLThumbnailRequest!, UnsafeRawPointer!, UnsafePointer<CFArrayCallBacks>!)](./qlthumbnailrequestsetdocumentobject%28_,_,_%29.md)
  Stores an object as part of a thumbnail request.
- [func QLThumbnailRequestSetImage(QLThumbnailRequest!, CGImage!, CFDictionary!)](./qlthumbnailrequestsetimage%28_,_,_%29.md)
  Sets the thumbnail request to a specified image.
- [func QLThumbnailRequestSetImageAtURL(QLThumbnailRequest!, CFURL!, CFDictionary!)](./qlthumbnailrequestsetimageaturl%28_,_,_%29.md)
  Sets the thumbnail request to contain the image at a given URL.
- [func QLThumbnailRequestSetImageWithData(QLThumbnailRequest!, CFData!, CFDictionary!)](./qlthumbnailrequestsetimagewithdata%28_,_,_%29.md)
  Sets the response to the thumbnail request to image data saved within the document.
- [func QLThumbnailRequestSetThumbnailWithDataRepresentation(QLThumbnailRequest!, CFData!, CFString!, CFDictionary!, CFDictionary!)](./qlthumbnailrequestsetthumbnailwithdatarepresentation%28_,_,_,_,_%29.md)
  Sets the default image representation for an item with the provided data and specified file type.
- [func QLThumbnailRequestSetThumbnailWithURLRepresentation(QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CFDictionary!)](./qlthumbnailrequestsetthumbnailwithurlrepresentation%28_,_,_,_,_%29.md)
  Sets the default image representation for an item of a given type at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlthumbnailrequestcopyurl(_:))*