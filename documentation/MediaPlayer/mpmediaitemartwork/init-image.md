# init(image:)

**Framework**: Media Player  
**Kind**: init

Initializes a media item artwork instance with a full-size image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(image: UIImage)
```

#### Discussion

This method assumes that the crop rectangle of the image matches the bounds of the image, as defined by the image’s size in points. That is, this method assumes the image you supply is tightly cropped.

## Parameters

- `image`: The image to use to initialize the media item artwork instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/init(image:))*