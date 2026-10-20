# QLThumbnailCopyImage(_:)

**Framework**: Quick Look  
**Kind**: func  
**Role**: Function

Returns a thumbnail image.

**Availability**:
- macOS 10.6+ - Deprecated in 15.0

> **Deprecated**: Use QuickLookThumbnailing for thumbnails.

## Declaration

```swift
func QLThumbnailCopyImage(_ thumbnail: QLThumbnail!) -> Unmanaged<CGImage>!
```

```c
extern CGImageRefQLThumbnailCopyImage(QLThumbnailRef thumbnail);
```

#### Return Value

A thumbnail image, or `NULL` if the Quick Look framework can’t create a thumbnail.

#### Discussion

If you call this function directly without using [`QLThumbnailDispatchAsync(_:_:_:)`](./qlthumbnaildispatchasync%28_,_,_%29.md), this function blocks the calling thread until it finishes computing the thumbnail.

## Parameters

- `thumbnail`: The thumbnail to compute.

## See Also

### Creating thumbnails
- [func QLThumbnailImageCreate(CFAllocator!, CFURL!, CGSize, CFDictionary!) -> Unmanaged<CGImage>!](./qlthumbnailimagecreate%28_,_,_,_%29.md)
  Creates a thumbnail image for the specified file.
- [func QLThumbnailCreate(CFAllocator!, CFURL!, CGSize, CFDictionary!) -> Unmanaged<QLThumbnail>!](./qlthumbnailcreate%28_,_,_,_%29.md)
  Returns a thumbnail that’s generated in the background.
- [func QLThumbnailDispatchAsync(QLThumbnail!, dispatch_queue_t!, (() -> Void)!)](./qlthumbnaildispatchasync%28_,_,_%29.md)
  Creates a thumbnail in the background on the provided background queue.
- [func QLThumbnailCancel(QLThumbnail!)](./qlthumbnailcancel%28_%29.md)
  Cancels the computation of the thumbnail.
- [func QLThumbnailCopyDocumentURL(QLThumbnail!) -> Unmanaged<CFURL>!](./qlthumbnailcopydocumenturl%28_%29.md)
  Returns the URL of the document that you’re requesting a thumbnail for.
- [func QLThumbnailCopyOptions(QLThumbnail!) -> Unmanaged<CFDictionary>!](./qlthumbnailcopyoptions%28_%29.md)
  Returns the options for the requested thumbnail.
- [func QLThumbnailGetContentRect(QLThumbnail!) -> CGRect](./qlthumbnailgetcontentrect%28_%29.md)
  Returns the rectangle of the provided thumbnail image that represents the content of the document.
- [func QLThumbnailGetMaximumSize(QLThumbnail!) -> CGSize](./qlthumbnailgetmaximumsize%28_%29.md)
  Returns the maximum allowed size for the provided thumbnail image.
- [func QLThumbnailGetTypeID() -> CFTypeID](./qlthumbnailgettypeid%28%29.md)
  Returns the type identifier for the thumbnail’s opaque type.
- [func QLThumbnailIsCancelled(QLThumbnail!) -> Bool](./qlthumbnailiscancelled%28_%29.md)
  Returns whether the creation of the thumbnail was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlthumbnailcopyimage(_:))*