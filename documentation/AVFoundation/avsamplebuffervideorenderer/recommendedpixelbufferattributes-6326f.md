# recommendedPixelBufferAttributes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Recommended pixel buffer attributes for optimal performance when using CMSampleBuffers containing CVPixelBuffers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@property (readonly, nonnull) NSDictionary<NSString *,id> * recommendedPixelBufferAttributes;
```

## Discussion

The returned dictionary does not contain all of the attributes needed for creating pixel buffers. Use `CVPixelBufferCreateResolvedAttributesDictionary()` to reconcile these attributes with the pixel buffer creation attributes.

## See Also

### Accessing the pixel buffer
- [func displayedPixelBuffer() -> CVPixelBuffer?](./displayedpixelbuffer%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/recommendedpixelbufferattributes-6326f)*