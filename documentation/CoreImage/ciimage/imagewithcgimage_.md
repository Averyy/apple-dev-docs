# imageWithCGImage:

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates and returns an image object from a Quartz 2D image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```objc
+ (CIImage *) imageWithCGImage:(CGImageRef) image;
```

#### Return Value

An image object initialized with the contents of the Quartz 2D image.

## Parameters

- `image`: A Quartz 2D image ([`CGImage`](../../CoreGraphics/cgimage.md)) object. For more information, see [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066) and [`CGImage`](../../CoreGraphics/cgimage.md).

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
- [+ imageWithContentsOfURL:](./imagewithcontentsofurl_.md)
  Creates and returns an image object from the contents of a file.
- [init?(contentsOf: URL, options: [CIImageOption : Any]?)](./init%28contentsof,options%29.md)
  Initializes an image object by reading an image from a URL, using the specified options.
- [+ imageWithContentsOfURL:options:](./imagewithcontentsofurl_options_.md)
  Creates and returns an image object from the contents of a file, using the specified options.
- [init(cgImage: CGImage)](./init%28cgimage%29-2kvvb.md)
  Initializes an image object with a Quartz 2D image.
- [+ imageWithCGImage:options:](./imagewithcgimage_options_.md)
  Creates and returns an image object from a Quartz 2D image using the specified options.
- [init(cgImage: CGImage, options: [CIImageOption : Any]?)](./init%28cgimage,options%29-8663h.md)
  Initializes an image object with a Quartz 2D image, using the specified options.
- [+ imageWithCGImageSource:index:options:](./imagewithcgimagesource_index_options_.md)
- [init(cgImageSource: CGImageSource, index: Int, options: [CIImageOption : Any]?)](./init%28cgimagesource,index,options%29-e2bz.md)
- [+ imageWithData:](./imagewithdata_.md)
  Creates and returns an image object initialized with the supplied image data.
- [init?(data: Data)](./init%28data%29.md)
  Initializes an image object with the supplied image data.
- [+ imageWithData:options:](./imagewithdata_options_.md)
  Creates and returns an image object initialized with the supplied image data, using the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/imagewithcgimage:)*