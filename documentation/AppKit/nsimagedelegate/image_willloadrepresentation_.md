# image:willLoadRepresentation:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the image object is about to access its underlying bitmap data.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

## Declaration

```objc
- (void) image:(NSImage *) image willLoadRepresentation:(NSImageRep *) rep;
```

## Discussion

For incremental loading, this method is called when you first attempt to draw the image or otherwise access the bitmap data. Downloading of the image begins immediately after this method returns. This method is optional; incremental loading will continue if the delegate does not implement it.

## Parameters

- `image`: The image object whose contents need to be loaded.
- `rep`: The image representation object that was accessed.

## See Also

### Deprecated
- [- image:didLoadPartOfRepresentation:withValidRows:](./image_didloadpartofrepresentation_withvalidrows_.md)
  Tells the delegate that part of the incrementally loaded image data is available.
- [- image:didLoadRepresentation:withStatus:](./image_didloadrepresentation_withstatus_.md)
  Tells the delegate that an incrementally loaded image has been loaded and decompressed as completely as is possible.
- [- image:didLoadRepresentationHeader:](./image_didloadrepresentationheader_.md)
  Tells the delegate that enough data has been read to determine the size of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagedelegate/image:willloadrepresentation:)*