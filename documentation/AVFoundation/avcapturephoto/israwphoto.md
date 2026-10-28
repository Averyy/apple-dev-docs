# isRawPhoto

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether this photo object contains RAW format data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isRawPhoto: Bool { get }
```

```objc
@property (readonly, getter=isRawPhoto) BOOL rawPhoto;
```

## Discussion

When you request capture in RAW format, the capture output calls your delegate’s [`photoOutput(_:didFinishProcessingPhoto:error:)`](../avcapturephotocapturedelegate/photooutput%28_,didfinishprocessingphoto,error%29.md) method one or more times, delivering both the RAW photo data and (if requested) equivalent processed photos. Use this property to distinguish between the RAW and processed results from the same capture.

## See Also

### Accessing photo pixel data
- [var pixelBuffer: CVPixelBuffer?](./pixelbuffer.md)
  The uncompressed or RAW image sample buffer for the photo, if requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/israwphoto)*