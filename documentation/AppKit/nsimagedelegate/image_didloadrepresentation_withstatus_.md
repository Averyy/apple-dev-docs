# image:didLoadRepresentation:withStatus:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that an incrementally loaded image has been loaded and decompressed as completely as is possible.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

## Declaration

```objc
- (void) image:(NSImage *) image didLoadRepresentation:(NSImageRep *) rep withStatus:(NSImageLoadStatus) status;
```

#### Discussion

The delegate must implement this method if it wants to support the incremental loading of images. In that case, you must also set up the image object to be loaded lazily, by initializing it using the  [`init(byReferencingFile:)`](../nsimage/init%28byreferencingfile%29.md) or [`init(byReferencing:)`](../nsimage/init%28byreferencing%29.md) method.

If an error occurs during downloading or decompression, the `status` parameter is set to `NSImageLoadStatusInvalidData`, `NSImageLoadStatusUnexpectedEOF`, or `NSImageLoadStatusReadError`. If the download was cancelled, the `status` parameter is set to `NSImageLoadStatusCancelled`.

## Parameters

- `image`: The image object whose contents are being loaded.
- `rep`: The image representation object that loaded the image data.
- `status`: The status of the load operation. For a list of possible values, see [`NSImage.LoadStatus`](../nsimage/loadstatus.md) in [`NSImage`](../nsimage.md).

## See Also

### Deprecated
- [- image:didLoadPartOfRepresentation:withValidRows:](./image_didloadpartofrepresentation_withvalidrows_.md)
  Tells the delegate that part of the incrementally loaded image data is available.
- [- image:didLoadRepresentationHeader:](./image_didloadrepresentationheader_.md)
  Tells the delegate that enough data has been read to determine the size of the image.
- [- image:willLoadRepresentation:](./image_willloadrepresentation_.md)
  Tells the delegate that the image object is about to access its underlying bitmap data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagedelegate/image:didloadrepresentation:withstatus:)*