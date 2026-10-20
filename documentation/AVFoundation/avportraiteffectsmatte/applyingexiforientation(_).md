# applyingExifOrientation(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns a derivative portrait effects matte after applying the specified Exif orientation.

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
func applyingExifOrientation(_ exifOrientation: CGImagePropertyOrientation) -> Self
```

```objc
- (instancetype) portraitEffectsMatteByApplyingExifOrientation:(CGImagePropertyOrientation) exifOrientation;
```

## Parameters

- `exifOrientation`: One of the standard Exif orientation tags expressing how the portrait effects matte should be rotated or mirrored.

## See Also

### Creating a Portrait Effects matte
- [Configuring camera capture to collect a Portrait Effects matte](../configuring-camera-capture-to-collect-a-portrait-effects-matte.md)
  Prepare your app to capture a portrait effects matte when taking photos.
- [convenience init(fromDictionaryRepresentation: [AnyHashable : Any]) throws](./init%28fromdictionaryrepresentation%29.md)
  Initializes a portrait effects matte instance from auxiliary image information in an image file.
- [func replacingPortraitEffectsMatte(with: CVPixelBuffer) throws -> Self](./replacingportraiteffectsmatte%28with%29.md)
  Returns a portrait effects matte by wrapping the replacement pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte/applyingexiforientation(_:))*