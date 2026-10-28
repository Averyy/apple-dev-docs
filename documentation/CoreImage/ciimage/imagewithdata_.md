# imageWithData:

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates and returns an image object initialized with the supplied image data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```objc
+ (CIImage *) imageWithData:(NSData *) data;
```

## Return Value

An image object initialized with the supplied data, or `nil` if the method cannot create an image representation from the contents of the supplied data object.

## Parameters

- `data`: The data object that holds the contents of an image file (such as TIFF, GIF, JPG, or whatever else the system supports). The image data must be premultiplied.

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
- [+ imageWithCGImage:](./imagewithcgimage_.md)
  Creates and returns an image object from a Quartz 2D image.
- [init(cgImage: CGImage)](./init%28cgimage%29-2kvvb.md)
  Initializes an image object with a Quartz 2D image.
- [+ imageWithCGImage:options:](./imagewithcgimage_options_.md)
  Creates and returns an image object from a Quartz 2D image using the specified options.
- [init(cgImage: CGImage, options: [CIImageOption : Any]?)](./init%28cgimage,options%29-8663h.md)
  Initializes an image object with a Quartz 2D image, using the specified options.
- [+ imageWithCGImageSource:index:options:](./imagewithcgimagesource_index_options_.md)
- [init(cgImageSource: CGImageSource, index: Int, options: [CIImageOption : Any]?)](./init%28cgimagesource,index,options%29-e2bz.md)
- [init?(data: Data)](./init%28data%29.md)
  Initializes an image object with the supplied image data.
- [+ imageWithData:options:](./imagewithdata_options_.md)
  Creates and returns an image object initialized with the supplied image data, using the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/imagewithdata:)*