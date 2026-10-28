# init(image:)

**Framework**: Media Player  
**Kind**: init  
**Role**: Initializer

Initializes a media item artwork instance with a full-size image.

**Availability**:
- iOS 5.0+ - Deprecated in 10.0
- iPadOS 5.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: Use -initWithBoundsSize:requestHandler:

## Declaration

```swift
convenience init(image: UIImage)
```

```objc
- (instancetype) initWithImage:(UIImage *) image;
```

## Discussion

This method assumes that the crop rectangle of the image matches the bounds of the image, as defined by the image’s size in points. That is, this method assumes the image you supply is tightly cropped.

## Parameters

- `image`: The image to use to initialize the media item artwork instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/init(image:))*