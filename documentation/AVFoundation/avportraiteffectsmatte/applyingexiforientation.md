# applyingExifOrientation(_:)

**Framework**: AVFoundation  
**Kind**: method

Returns a derivative portrait effects matte after applying the specified EXIF orientation.

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

## Parameters

- `exifOrientation`: One of the standard EXIF orientation tags expressing how the portrait effects matte should be rotated or mirrored.

## See Also

- [Configuring camera capture to collect a Portrait Effects matte](configuring-camera-capture-to-collect-a-portrait-effects-matte.md)
  Prepare your app to capture a portrait effects matte when taking photos.
- [convenience init(fromDictionaryRepresentation: [AnyHashable : Any]) throws](avportraiteffectsmatte/init(fromdictionaryrepresentation:).md)
  Initializes a portrait effects matte instance from auxiliary image information in an image file.
- [func replacingPortraitEffectsMatte(with: CVPixelBuffer) throws -> Self](avportraiteffectsmatte/replacingportraiteffectsmatte(with:).md)
  Returns a portrait effects matte by wrapping the replacement pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte/applyingexiforientation(_:))*