# QLThumbnailImageCreate(_:_:_:_:)

**Framework**: Quick Look  
**Kind**: func

Creates a thumbnail image for the specified file.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func QLThumbnailImageCreate(_ allocator: CFAllocator!, _ url: CFURL!, _ maxThumbnailSize: CGSize, _ options: CFDictionary!) -> Unmanaged<CGImage>!
```

#### Return Value

The thumbnail image, or `NULL` if Quick Look doesn’t support this file type.

#### Discussion

This function doesn’t supplant the use of Icon Services by apps to get generic file icons and custom icons stored in the metadata fork of files.

##### Special Considerations

This function is thread-safe, so you can call it from any thread. However, because it’s synchronous, you should generally call it in a background thread.

## Parameters

- `allocator`: The allocator to use to create the thumbnail image.
- `url`: The URL of the file to create a thumbnail image for.
- `maxThumbnailSize`: The maximum desired size of the thumbnail image.
- `options`: A dictionary of options that affect the creation of the thumbnail image. You can use   and   as options.

## See Also

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
- [func QLThumbnailIsCancelled(QLThumbnail!) -> Bool](qlthumbnailiscancelled(_:).md)
  Returns whether the creation of the thumbnail was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlthumbnailimagecreate(_:_:_:_:))*