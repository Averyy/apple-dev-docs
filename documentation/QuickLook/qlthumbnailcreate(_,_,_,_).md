# QLThumbnailCreate(_:_:_:_:)

**Framework**: Quick Look  
**Kind**: func  
**Role**: Function

Returns a thumbnail that’s generated in the background.

**Availability**:
- macOS 10.6+ - Deprecated in 15.0

> **Deprecated**: Use QLThumbnailGenerationRequest in QuickLookThumbnailing to generate thumbnails.

## Declaration

```swift
func QLThumbnailCreate(_ allocator: CFAllocator!, _ url: CFURL!, _ maxThumbnailSize: CGSize, _ options: CFDictionary!) -> Unmanaged<QLThumbnail>!
```

```c
extern QLThumbnailRefQLThumbnailCreate(CFAllocatorRef allocator, CFURLRef url, CGSize maxThumbnailSize, CFDictionaryRef options);
```

#### Return Value

A generated thumbnail of the file at the provided `url`.

## Parameters

- `allocator`: The allocator to use to create the thumbnail.
- `url`: The URL of the document that you want to request a thumbnail for.
- `maxThumbnailSize`: The maximum size in points for the thumbnail image.
- `options`: Optional hints for creating a thumbnail image. Available options are [`kQLThumbnailOptionScaleFactorKey`](./kqlthumbnailoptionscalefactorkey.md) and [`kQLThumbnailOptionIconModeKey`](./kqlthumbnailoptioniconmodekey.md).

## See Also

### Creating thumbnails
- [func QLThumbnailImageCreate(CFAllocator!, CFURL!, CGSize, CFDictionary!) -> Unmanaged<CGImage>!](./qlthumbnailimagecreate%28_,_,_,_%29.md)
  Creates a thumbnail image for the specified file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlthumbnailcreate(_:_:_:_:))*