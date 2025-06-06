# pixelBufferPool

**Framework**: AVFoundation  
**Kind**: property

A pixel buffer pool that vends and efficiently recycles the pixel buffers of tagged buffer groups.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var pixelBufferPool: CVPixelBufferPool? { get }
```

#### Discussion

For maximum efficiency, create the pixel buffers of tagged buffer groups using this pool with the [`CVPixelBufferPoolCreatePixelBuffer(_:_:_:)`](https://developer.apple.com/documentation/CoreVideo/CVPixelBufferPoolCreatePixelBuffer(_:_:_:)) function.

The value of this property is `nil` before you call [`startWriting()`](avassetwriter/startwriting().md) on the associated [`AVAssetWriter`](avassetwriter.md) object. Query this property after writing starts to retrieve a `non-nil` value.

This property is not key value observable.

## See Also

- [var sourcePixelBufferAttributes: [String : Any]?](avassetwriterinputtaggedpixelbuffergroupadaptor/sourcepixelbufferattributes.md)
  The attributes of buffers that the adaptor’s pixel buffer pool vends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/pixelbufferpool)*