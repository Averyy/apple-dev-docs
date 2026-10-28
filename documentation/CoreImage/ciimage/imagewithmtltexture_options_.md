# imageWithMTLTexture:options:

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates and returns an image object with data supplied by a Metal texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (CIImage *) imageWithMTLTexture:(id<MTLTexture>) texture options:(NSDictionary<NSString *,id> *) options;
```

## Return Value

An image object initialized with the texture data.

## Discussion

To also render using Metal, use this image with a Metal-based [`CIContext`](../cicontext.md) object created with the [`init(mtlDevice:)`](../cicontext/init%28mtldevice%29-swey.md) method, and call the [`render(_:to:commandBuffer:bounds:colorSpace:)`](../cicontext/render%28_,to,commandbuffer,bounds,colorspace%29.md) method to create an output image in another Metal texture object.

## Parameters

- `texture`: The Metal texture from which to use image data.
- `options`: A dictionary specifying image options. (See `Image Dictionary Keys`.)

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
- [+ imageWithData:](./imagewithdata_.md)
  Creates and returns an image object initialized with the supplied image data.
- [init?(data: Data)](./init%28data%29.md)
  Initializes an image object with the supplied image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/imagewithmtltexture:options:)*