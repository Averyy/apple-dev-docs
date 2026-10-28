# assetImageGeneratorWithAsset:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new object that generates images for times within a video asset.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) assetImageGeneratorWithAsset:(AVAsset *) asset;
```

## Return Value

A new image generator.

## Parameters

- `asset`: A video asset from which to generate images.

## See Also

### Creating an image generator
- [init(asset: AVAsset)](./init%28asset%29.md)
  Creates an object that generates images for times within a video asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/assetimagegeneratorwithasset:)*