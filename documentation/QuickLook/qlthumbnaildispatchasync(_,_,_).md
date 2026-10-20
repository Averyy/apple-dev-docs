# QLThumbnailDispatchAsync(_:_:_:)

**Framework**: Quick Look  
**Kind**: func  
**Role**: Function

Creates a thumbnail in the background on the provided background queue.

**Availability**:
- macOS 10.6+ - Deprecated in 15.0

> **Deprecated**: Use QLThumbnailGenerator in QuickLookThumbnailing to generate thumbnails.

## Declaration

```swift
func QLThumbnailDispatchAsync(_ thumbnail: QLThumbnail!, _ queue: dispatch_queue_t!, _ completion: (() -> Void)!)
```

```c
extern void QLThumbnailDispatchAsync(QLThumbnailRef thumbnail, dispatch_queue_t queue, dispatch_block_t completion);
```

## Parameters

- `thumbnail`: The thumbnail to compute.
- `queue`: The queue that’s used to create the thumbnail.
- `completion`: The completion block that’s called when the thumbnail is created. The completion block is always called, even if the thumbnail computation is canceled.

## See Also

### Creating thumbnails
- [func QLThumbnailImageCreate(CFAllocator!, CFURL!, CGSize, CFDictionary!) -> Unmanaged<CGImage>!](./qlthumbnailimagecreate%28_,_,_,_%29.md)
  Creates a thumbnail image for the specified file.
- [func QLThumbnailCreate(CFAllocator!, CFURL!, CGSize, CFDictionary!) -> Unmanaged<QLThumbnail>!](./qlthumbnailcreate%28_,_,_,_%29.md)
  Returns a thumbnail that’s generated in the background.
- [func QLThumbnailCancel(QLThumbnail!)](./qlthumbnailcancel%28_%29.md)
  Cancels the computation of the thumbnail.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlthumbnaildispatchasync(_:_:_:))*