# init(imageProvider:size:_:format:colorSpace:options:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Initializes an image object based on pixels from an image provider object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(imageProvider provider: Any, size width: Int, _ height: Int, format: CIFormat, colorSpace: CGColorSpace?, options: [CIImageOption : Any]? = nil)
```

```objc
- (instancetype) initWithImageProvider:(id) provider size:(size_t) width :(size_t) height format:(CIFormat) format colorSpace:(CGColorSpaceRef) colorSpace options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

 An initialized [`CIImage`](../ciimage.md) object based on the data provider.

#### Discussion

Core Image retains the provider object until the image is deallocated. The image provider object will not be called until the image is rendered.

## Parameters

- `provider`: An object that implements the `CIImageProvider` protocol.
- `width`: The width of the image.
- `height`: The height of the image.
- `format`: The [`CIFormat`](../ciformat.md) of the provided pixels.
- `colorSpace`: The color space that the image is defined in. If `nil`, then the pixels will not be is not color matched to the Core Image working color space.
- `options`: A dictionary that contains various [`CIImageOption`](../ciimageoption.md) keys that affect the resulting [`CIImage`](../ciimage.md).
  The option [`providerTileSize`](../ciimageoption/providertilesize.md) controls if and how the provider object is called in tiles. The option [`providerUserInfo`](../ciimageoption/provideruserinfo.md) allows additional state to be passed to the provider object.

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
- [init?(depthData: AVDepthData)](./init%28depthdata%29.md)
- [init?(depthData: AVDepthData, options: [String : Any]?)](./init%28depthdata,options%29.md)
- [init?(portaitEffectsMatte: AVPortraitEffectsMatte)](./init%28portaiteffectsmatte%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/init(imageprovider:size:_:format:colorspace:options:))*