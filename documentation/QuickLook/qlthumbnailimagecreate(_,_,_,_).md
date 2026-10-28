# QLThumbnailImageCreate(_:_:_:_:)

**Framework**: Quick Look  
**Kind**: func  
**Role**: Function

Creates a thumbnail image for the specified file.

**Availability**:
- macOS 10.6+ - Deprecated in 15.0

> **Deprecated**: Use QuickLookThumbnailing to generate thumbnails for files.

## Declaration

```swift
func QLThumbnailImageCreate(_ allocator: CFAllocator!, _ url: CFURL!, _ maxThumbnailSize: CGSize, _ options: CFDictionary!) -> Unmanaged<CGImage>!
```

```c
extern CGImageRefQLThumbnailImageCreate(CFAllocatorRef allocator, CFURLRef url, CGSize maxThumbnailSize, CFDictionaryRef options);
```

## Return Value

The thumbnail image, or `NULL` if Quick Look doesn’t support this file type.

## Discussion

This function doesn’t supplant the use of Icon Services by apps to get generic file icons and custom icons stored in the metadata fork of files.

### Special Considerations

This function is thread-safe, so you can call it from any thread. However, because it’s synchronous, you should generally call it in a background thread.

## Parameters

- `allocator`: The allocator to use to create the thumbnail image.
- `url`: The URL of the file to create a thumbnail image for.
- `maxThumbnailSize`: The maximum desired size of the thumbnail image.
- `options`: A dictionary of options that affect the creation of the thumbnail image. You can use [`kQLThumbnailOptionIconModeKey`](./kqlthumbnailoptioniconmodekey.md) and [`kQLThumbnailOptionScaleFactorKey`](./kqlthumbnailoptionscalefactorkey.md) as options.

## See Also

### Creating thumbnails
- [func QLThumbnailCreate(CFAllocator!, CFURL!, CGSize, CFDictionary!) -> Unmanaged<QLThumbnail>!](./qlthumbnailcreate%28_,_,_,_%29.md)
  Returns a thumbnail that’s generated in the background.
- [func QLThumbnailDispatchAsync(QLThumbnail!, dispatch_queue_t!, (() -> Void)!)](./qlthumbnaildispatchasync%28_,_,_%29.md)
  Creates a thumbnail in the background on the provided background queue.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlthumbnailimagecreate(_:_:_:_:))*