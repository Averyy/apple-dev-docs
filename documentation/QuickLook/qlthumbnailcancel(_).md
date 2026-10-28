# QLThumbnailCancel(_:)

**Framework**: Quick Look  
**Kind**: func  
**Role**: Function

Cancels the computation of the thumbnail.

**Availability**:
- macOS 10.6+ - Deprecated in 15.0

> **Deprecated**: Use [QLThumbnailGenerator cancelRequest:] in QuickLookThumbnailing.

## Declaration

```swift
func QLThumbnailCancel(_ thumbnail: QLThumbnail!)
```

```c
extern void QLThumbnailCancel(QLThumbnailRef thumbnail);
```

## Discussion

If you use [`QLThumbnailDispatchAsync(_:_:_:)`](./qlthumbnaildispatchasync%28_,_,_%29.md) to request the thumbnail, calling this function invokes the completion callback of [`QLThumbnailDispatchAsync(_:_:_:)`](./qlthumbnaildispatchasync%28_,_,_%29.md). If you use synchronous mode, [`QLThumbnailCopyImage(_:)`](./qlthumbnailcopyimage%28_%29.md) returns `NULL` immediately.

## Parameters

- `thumbnail`: The thumbnail to cancel.

## See Also

### Creating thumbnails
- [func QLThumbnailImageCreate(CFAllocator!, CFURL!, CGSize, CFDictionary!) -> Unmanaged<CGImage>!](./qlthumbnailimagecreate%28_,_,_,_%29.md)
  Creates a thumbnail image for the specified file.
- [func QLThumbnailCreate(CFAllocator!, CFURL!, CGSize, CFDictionary!) -> Unmanaged<QLThumbnail>!](./qlthumbnailcreate%28_,_,_,_%29.md)
  Returns a thumbnail that’s generated in the background.
- [func QLThumbnailDispatchAsync(QLThumbnail!, dispatch_queue_t!, (() -> Void)!)](./qlthumbnaildispatchasync%28_,_,_%29.md)
  Creates a thumbnail in the background on the provided background queue.
- [func QLThumbnailCopyDocumentURL(QLThumbnail!) -> Unmanaged<CFURL>!](./qlthumbnailcopydocumenturl%28_%29.md)
  Returns the URL of the document that you’re requesting a thumbnail for.
- [func QLThumbnailCopyImage(QLThumbnail!) -> Unmanaged<CGImage>!](./qlthumbnailcopyimage%28_%29.md)
  Returns a thumbnail image.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlthumbnailcancel(_:))*