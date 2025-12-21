# replacingPortraitEffectsMatte(with:)

**Framework**: AVFoundation  
**Kind**: method

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

## Parameters

- `pixelBuffer`: A pixel buffer containing a portrait effects matte image, represented as   with   color primaries and a   transfer function.

## See Also

- [Configuring camera capture to collect a Portrait Effects matte](configuring-camera-capture-to-collect-a-portrait-effects-matte.md)
  Prepare your app to capture a portrait effects matte when taking photos.
- [convenience init(fromDictionaryRepresentation: [AnyHashable : Any]) throws](avportraiteffectsmatte/init(fromdictionaryrepresentation:).md)
  Initializes a portrait effects matte instance from auxiliary image information in an image file.
- [func applyingExifOrientation(CGImagePropertyOrientation) -> Self](avportraiteffectsmatte/applyingexiforientation(_:).md)
  Returns a derivative portrait effects matte after applying the specified EXIF orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte/replacingportraiteffectsmatte(with:))*