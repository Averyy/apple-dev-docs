# artwork(url:contentType:size:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Type Method

Creates an artwork instance that references an image at the given URL.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class func artwork(url: URL, contentType type: UTType, size: CGSize) -> AVPlaybackUserInterfaceContentURLArtwork
```

```objc
+ (AVPlaybackUserInterfaceContentURLArtwork *) artworkWithURL:(NSURL *) url contentType:(UTType *) type size:(CGSize) size;
```

## Parameters

- `url`: URL pointing to the artwork image resource.
- `type`: The uniform type identifier for the image data.
- `size`: The pixel dimensions of the artwork image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentartwork/artwork(url:contenttype:size:))*