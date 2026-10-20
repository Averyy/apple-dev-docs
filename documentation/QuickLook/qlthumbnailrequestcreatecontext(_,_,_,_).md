# QLThumbnailRequestCreateContext(_:_:_:_:)

**Framework**: Quick Look  
**Kind**: func  
**Role**: Function

Creates a graphics context to draw the thumbnail in.

**Availability**:
- macOS 10.0+ - Deprecated in 12.0

> **Deprecated**: Use a QLThumbnailReply in a Thumbnail Extension to provide thumbnails for your file types.

## Declaration

```swift
func QLThumbnailRequestCreateContext(_ thumbnail: QLThumbnailRequest!, _ size: CGSize, _ isBitmap: Bool, _ properties: CFDictionary!) -> Unmanaged<CGContext>!
```

```c
extern CGContextRefQLThumbnailRequestCreateContext(QLThumbnailRequestRef thumbnail, CGSize size, Boolean isBitmap, CFDictionaryRef properties);
```

#### Return Value

A Core Graphics graphics-context object that you can draw your thumbnail image in. You should explicitly release this object when it is no longer needed.

#### Discussion

You can directly draw your thumbnail data in the graphics-context object created by this function. After calling this function, you should flush the context with [`QLThumbnailRequestFlushContext(_:_:)`](./qlthumbnailrequestflushcontext%28_,_%29.md). Also be sure to release the `CGContext` object.

With this function you can create two types of graphics contexts for drawing thumbnails: bitmap and single-page vector-based; you use the `isBitmap` flag to distinguish between the two. Quick Look handles bitmap thumbnail context differently than non-bitmap contexts; in the latter case, Quick Look might scale the drawing up or down if necessary, and it respects the scale factor (for HiDPI support).

If you prefer to work in Objective-C code, you can convert the created [`CGContext`](../CoreGraphics/cgcontext.md) to a [`NSGraphicsContext`](../AppKit/nsgraphicscontext.md) object using [`init(graphicsPort:flipped:)`](../AppKit/nsgraphicscontext/init%28graphicsport,flipped%29.md).

##### Special Considerations

Thread-safety: This function should be called in the same thread as the thumbnail request is made in; generally, this is the same thread in which the `GenerateThumbnailForURL` callback was invoked.

## Parameters

- `size`: The size of the thumbnail; if `isBitmap` is `true` the size is in pixels, otherwise it’s in points.
- `isBitmap`: `true` if the thumbnail data is bitmap-based, `false` if vector-based. This value of this parameter affects the interpretation of the `size` parameter.
- `properties`: A dictionary containing properties for the thumbnail response. For macOS 10.5, no properties have been defined.

## See Also

### Handling thumbnail requests
- [func QLThumbnailRequestCopyContentUTI(QLThumbnailRequest!) -> Unmanaged<CFString>!](./qlthumbnailrequestcopycontentuti%28_%29.md)
  Returns the UTI for the thumbnail request.
- [func QLThumbnailRequestCopyOptions(QLThumbnailRequest!) -> Unmanaged<CFDictionary>!](./qlthumbnailrequestcopyoptions%28_%29.md)
  Returns the options specified for the thumbnail request.
- [func QLThumbnailRequestCopyURL(QLThumbnailRequest!) -> Unmanaged<CFURL>!](./qlthumbnailrequestcopyurl%28_%29.md)
  Returns the URL of the document for which the thumbnail request is requested.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlthumbnailrequestcreatecontext(_:_:_:_:))*