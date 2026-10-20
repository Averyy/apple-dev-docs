# replacingPortraitEffectsMatte(with:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns a portrait effects matte by wrapping the replacement pixel buffer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func replacingPortraitEffectsMatte(with pixelBuffer: CVPixelBuffer) throws -> Self
```

```objc
- (instancetype) portraitEffectsMatteByReplacingPortraitEffectsMatteWithPixelBuffer:(CVPixelBufferRef) pixelBuffer error:(NSError **) outError;
```

## Parameters

- `pixelBuffer`: A pixel buffer containing a portrait effects matte image, represented as [`kCVPixelFormatType_OneComponent8`](../../CoreVideo/kcvpixelformattype_onecomponent8.md) with [`kCVImageBufferColorPrimaries_ITU_R_709_2`](../../CoreVideo/kcvimagebuffercolorprimaries_itu_r_709_2.md) color primaries and a [`kCVImageBufferTransferFunction_Linear`](../../CoreVideo/kcvimagebuffertransferfunction_linear.md) transfer function.

## See Also

### Creating a Portrait Effects matte
- [Configuring camera capture to collect a Portrait Effects matte](../configuring-camera-capture-to-collect-a-portrait-effects-matte.md)
  Prepare your app to capture a portrait effects matte when taking photos.
- [convenience init(fromDictionaryRepresentation: [AnyHashable : Any]) throws](./init%28fromdictionaryrepresentation%29.md)
  Initializes a portrait effects matte instance from auxiliary image information in an image file.
- [func applyingExifOrientation(CGImagePropertyOrientation) -> Self](./applyingexiforientation%28_%29.md)
  Returns a derivative portrait effects matte after applying the specified Exif orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte/replacingportraiteffectsmatte(with:))*