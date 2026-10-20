# init(cvPixelBuffer:properties:options:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Returns a CIFilter that will in turn return a properly processed CIImage as “outputImage”.

**Availability**:
- iOS 10.0+ - Deprecated in 27.2
- iPadOS 10.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.12+ - Deprecated in 27.2
- tvOS 10.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use new CIRAWFilter class instead.

## Declaration

```swift
init!(cvPixelBuffer pixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]! = [:])
```

```objc
+ (CIFilter *) filterWithCVPixelBuffer:(CVPixelBufferRef) pixelBuffer properties:(NSDictionary *) properties options:(NSDictionary<NSString *,id> *) options;
```

#### Discussion

Note that when using this initializer, you should pass in a CVPixelBufferRef with one of the following Raw pixel format types kCVPixelFormatType_14Bayer_GRBG, kCVPixelFormatType_14Bayer_RGGB, kCVPixelFormatType_14Bayer_BGGR, kCVPixelFormatType_14Bayer_GBRG as well as the root properties attachment from the CMSampleBufferRef.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/init(cvpixelbuffer:properties:options:)-69695)*