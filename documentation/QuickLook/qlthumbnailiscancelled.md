# QLThumbnailIsCancelled(_:)

**Framework**: Quick Look  
**Kind**: func

Returns whether the creation of the thumbnail was canceled.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func QLThumbnailIsCancelled(_ thumbnail: QLThumbnail!) -> Bool
```

#### Return Value

A `Boolean` value that indicates whether the creation of the thumbnail was canceled.

## Parameters

- `thumbnail`: The thumbnail to create.

## See Also

- [func QLThumbnailImageCreate(CFAllocator!, CFURL!, CGSize, CFDictionary!) -> Unmanaged<CGImage>!](qlthumbnailimagecreate(_:_:_:_:).md)
  Creates a thumbnail image for the specified file.
- [func QLThumbnailCreate(CFAllocator!, CFURL!, CGSize, CFDictionary!) -> Unmanaged<QLThumbnail>!](qlthumbnailcreate(_:_:_:_:).md)
  Returns a thumbnail that’s generated in the background.
- [func QLThumbnailDispatchAsync(QLThumbnail!, dispatch_queue_t!, (() -> Void)!)](qlthumbnaildispatchasync(_:_:_:).md)
  Creates a thumbnail in the background on the provided background queue.
- [func QLThumbnailCancel(QLThumbnail!)](qlthumbnailcancel(_:).md)
  Cancels the computation of the thumbnail.
- [func QLThumbnailCopyDocumentURL(QLThumbnail!) -> Unmanaged<CFURL>!](qlthumbnailcopydocumenturl(_:).md)
  Returns the URL of the document that you’re requesting a thumbnail for.
- [func QLThumbnailCopyImage(QLThumbnail!) -> Unmanaged<CGImage>!](qlthumbnailcopyimage(_:).md)
  Returns a thumbnail image.
- [func QLThumbnailCopyOptions(QLThumbnail!) -> Unmanaged<CFDictionary>!](qlthumbnailcopyoptions(_:).md)
  Returns the options for the requested thumbnail.
- [func QLThumbnailGetContentRect(QLThumbnail!) -> CGRect](qlthumbnailgetcontentrect(_:).md)
  Returns the rectangle of the provided thumbnail image that represents the content of the document.
- [func QLThumbnailGetMaximumSize(QLThumbnail!) -> CGSize](qlthumbnailgetmaximumsize(_:).md)
  Returns the maximum allowed size for the provided thumbnail image.
- [func QLThumbnailGetTypeID() -> CFTypeID](qlthumbnailgettypeid().md)
  Returns the type identifier for the thumbnail’s opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlthumbnailiscancelled(_:))*