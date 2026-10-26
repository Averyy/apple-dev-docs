# stopCachingImagesForAllAssets()

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Cancels all image preparation that is currently in progress.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func stopCachingImagesForAllAssets()
```

```objc
- (void) stopCachingImagesForAllAssets;
```

## See Also

### Preparing Images
- [func startCachingImages(for: [PHAsset], targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?)](./startcachingimages%28for,targetsize,contentmode,options%29.md)
  Prepares image representations of the specified assets for later use.
- [func stopCachingImages(for: [PHAsset], targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?)](./stopcachingimages%28for,targetsize,contentmode,options%29.md)
  Cancels image preparation for the specified assets and options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcachingimagemanager/stopcachingimagesforallassets())*