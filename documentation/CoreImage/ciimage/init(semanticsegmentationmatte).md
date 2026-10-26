# init(semanticSegmentationMatte:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init?(semanticSegmentationMatte matte: AVSemanticSegmentationMatte)
```

```objc
- (instancetype) initWithSemanticSegmentationMatte:(AVSemanticSegmentationMatte *) matte;
```

## See Also

### Creating an Image
- [class func empty() -> CIImage](./empty%28%29.md)
  Creates and returns an empty image object.
- [init?(image: UIImage)](./init%28image%29.md)
  Initializes an image object with the specified UIKit image object.
- [init?(image: UIImage, options: [CIImageOption : Any]?)](./init%28image,options%29.md)
  Initializes an image object with the specified UIKit image object, using the specified options.
- [init?(contentsOf: URL)](./init%28contentsof%29.md)
  Initializes an image object by reading an image from a URL.
- [init?(contentsOf: URL, options: [CIImageOption : Any]?)](./init%28contentsof,options%29.md)
  Initializes an image object by reading an image from a URL, using the specified options.
- [init(cgImage: CGImage)](./init%28cgimage%29-2kvvb.md)
  Initializes an image object with a Quartz 2D image.
- [init(cgImage: CGImage, options: [CIImageOption : Any]?)](./init%28cgimage,options%29-8663h.md)
  Initializes an image object with a Quartz 2D image, using the specified options.
- [init(cgImageSource: CGImageSource, index: Int, options: [CIImageOption : Any]?)](./init%28cgimagesource,index,options%29-e2bz.md)
- [init?(data: Data)](./init%28data%29.md)
  Initializes an image object with the supplied image data.
- [init?(data: Data, options: [CIImageOption : Any]?)](./init%28data,options%29.md)
  Initializes an image object with the supplied image data, using the specified options.
- [init(bitmapData: Data, bytesPerRow: Int, size: CGSize, format: CIFormat, colorSpace: CGColorSpace?)](./init%28bitmapdata,bytesperrow,size,format,colorspace%29.md)
  Initializes an image object with bitmap data.
- [init?(bitmapImageRep: NSBitmapImageRep)](./init%28bitmapimagerep%29.md)
  Initializes an image object with the specified bitmap image representation.
- [init(imageProvider: Any, size: Int, Int, format: CIFormat, colorSpace: CGColorSpace?, options: [CIImageOption : Any]?)](./init%28imageprovider,size,_,format,colorspace,options%29.md)
  Initializes an image object based on pixels from an image provider object.
- [init?(depthData: AVDepthData)](./init%28depthdata%29.md)
- [init?(depthData: AVDepthData, options: [String : Any]?)](./init%28depthdata,options%29.md)
- [+ imageWithContentsOfURL:](./imagewithcontentsofurl_.md)
  Creates and returns an image object from the contents of a file.
- [+ imageWithContentsOfURL:options:](./imagewithcontentsofurl_options_.md)
  Creates and returns an image object from the contents of a file, using the specified options.
- [+ imageWithCGImage:](./imagewithcgimage_.md)
  Creates and returns an image object from a Quartz 2D image.
- [+ imageWithCGImage:options:](./imagewithcgimage_options_.md)
  Creates and returns an image object from a Quartz 2D image using the specified options.
- [+ imageWithCGImageSource:index:options:](./imagewithcgimagesource_index_options_.md)
- [+ imageWithData:](./imagewithdata_.md)
  Creates and returns an image object initialized with the supplied image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/init(semanticsegmentationmatte:))*