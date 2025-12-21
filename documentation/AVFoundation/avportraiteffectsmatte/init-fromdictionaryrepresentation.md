# init(fromDictionaryRepresentation:)

**Framework**: AVFoundation  
**Kind**: init

Initializes a portrait effects matte instance from auxiliary image information in an image file.

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
convenience init(fromDictionaryRepresentation imageSourceAuxDataInfoDictionary: [AnyHashable : Any]) throws
```

## Mentions

- [Extracting Portrait Effects matte image data from a photo](extracting-portrait-effects-matte-image-data-from-a-photo.md)

#### Discussion

When using the [`Image I/O`](https://developer.apple.com/documentation/ImageIO) API to read from a HEIF or JPEG file containing a portrait effects matte, you can create an [`AVPortraitEffectsMatte`](avportraiteffectsmatte.md) object from the result of [`CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)`](https://developer.apple.com/documentation/ImageIO/CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)). This function returns a [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary) of primitive map information.

## Parameters

- `imageSourceAuxDataInfoDictionary`: A dictionary of information related to primitive portrait effects matte; obtained from  .

## See Also

- [Configuring camera capture to collect a Portrait Effects matte](configuring-camera-capture-to-collect-a-portrait-effects-matte.md)
  Prepare your app to capture a portrait effects matte when taking photos.
- [func applyingExifOrientation(CGImagePropertyOrientation) -> Self](avportraiteffectsmatte/applyingexiforientation(_:).md)
  Returns a derivative portrait effects matte after applying the specified EXIF orientation.
- [func replacingPortraitEffectsMatte(with: CVPixelBuffer) throws -> Self](avportraiteffectsmatte/replacingportraiteffectsmatte(with:).md)
  Returns a portrait effects matte by wrapping the replacement pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte/init(fromdictionaryrepresentation:))*