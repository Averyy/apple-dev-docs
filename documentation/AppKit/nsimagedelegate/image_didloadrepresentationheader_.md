# image:didLoadRepresentationHeader:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that enough data has been read to determine the size of the image.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

## Declaration

```objc
- (void) image:(NSImage *) image didLoadRepresentationHeader:(NSImageRep *) rep;
```

## Discussion

By the time this method is called, the `NSBitmapImageRep` object specified in the `rep` parameter is valid and has allocated the memory needed to store the bitmap. The bitmap itself is filled with the image’s background color. This method is optional; incremental loading will continue if the delegate does not implement it.

## Parameters

- `image`: The image object whose contents are being loaded.
- `rep`: The image representation object that is receiving and processing the image data.

## See Also

### Deprecated
- [- image:didLoadPartOfRepresentation:withValidRows:](./image_didloadpartofrepresentation_withvalidrows_.md)
  Tells the delegate that part of the incrementally loaded image data is available.
- [- image:didLoadRepresentation:withStatus:](./image_didloadrepresentation_withstatus_.md)
  Tells the delegate that an incrementally loaded image has been loaded and decompressed as completely as is possible.
- [- image:willLoadRepresentation:](./image_willloadrepresentation_.md)
  Tells the delegate that the image object is about to access its underlying bitmap data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagedelegate/image:didloadrepresentationheader:)*