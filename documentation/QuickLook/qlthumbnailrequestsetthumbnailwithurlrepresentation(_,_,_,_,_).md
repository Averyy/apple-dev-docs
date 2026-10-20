# QLThumbnailRequestSetThumbnailWithURLRepresentation(_:_:_:_:_:)

**Framework**: Quick Look  
**Kind**: func  
**Role**: Function

Sets the default image representation for an item of a given type at the specified URL.

**Availability**:
- macOS 10.6+ - Deprecated in 12.0

> **Deprecated**: Use a QLThumbnailReply in a Thumbnail Extension to provide thumbnails for your file types.

## Declaration

```swift
func QLThumbnailRequestSetThumbnailWithURLRepresentation(_ thumbnail: QLThumbnailRequest!, _ url: CFURL!, _ contentTypeUTI: CFString!, _ previewProperties: CFDictionary!, _ properties: CFDictionary!)
```

```c
extern void QLThumbnailRequestSetThumbnailWithURLRepresentation(QLThumbnailRequestRef thumbnail, CFURLRef url, CFStringRef contentTypeUTI, CFDictionaryRef previewProperties, CFDictionaryRef properties);
```

## Parameters

- `thumbnail`: The thumbnail request object.
- `url`: The url to the file of the preview response.
- `contentTypeUTI`: The UTI of the content for the preview representation.
- `previewProperties`: Additional properties for the preview response.
- `properties`: A dictionary of properties for the thumbnail. macOS doesn’t support any properties.

## See Also

### Handling thumbnail requests
- [func QLThumbnailRequestCopyContentUTI(QLThumbnailRequest!) -> Unmanaged<CFString>!](./qlthumbnailrequestcopycontentuti%28_%29.md)
  Returns the UTI for the thumbnail request.
- [func QLThumbnailRequestCopyOptions(QLThumbnailRequest!) -> Unmanaged<CFDictionary>!](./qlthumbnailrequestcopyoptions%28_%29.md)
  Returns the options specified for the thumbnail request.
- [func QLThumbnailRequestCopyURL(QLThumbnailRequest!) -> Unmanaged<CFURL>!](./qlthumbnailrequestcopyurl%28_%29.md)
  Returns the URL of the document for which the thumbnail request is requested.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlthumbnailrequestsetthumbnailwithurlrepresentation(_:_:_:_:_:))*