# stopCachingImages(for:targetSize:contentMode:options:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Cancels image preparation for the specified assets and options.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func stopCachingImages(for assets: [PHAsset], targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?)
```

```objc
- (void) stopCachingImagesForAssets:(NSArray<PHAsset *> *) assets targetSize:(CGSize) targetSize contentMode:(PHImageContentMode) contentMode options:(PHImageRequestOptions *) options;
```

#### Discussion

This method cancels image preparation for the specified assets with the specified options. Use it when image preparation that might be in progress is no longer needed. For example, if you prepare images for a collection view filled with photo thumbnails and then the user chooses a different thumbnail size for your collection view, call this method to cancel generating thumbnail images at the old size.

## Parameters

- `assets`: The array of specific [`PHAsset`](../phasset.md) objects for which image preparation is in progress but is no longer needed.
- `targetSize`: The target size with which you requested image preparation.
- `contentMode`: The content mode with which you requested image preparation.
- `options`: The options with which you requested image preparation.

## See Also

### Preparing Images
- [func startCachingImages(for: [PHAsset], targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?)](./startcachingimages%28for,targetsize,contentmode,options%29.md)
  Prepares image representations of the specified assets for later use.
- [func stopCachingImagesForAllAssets()](./stopcachingimagesforallassets%28%29.md)
  Cancels all image preparation that is currently in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcachingimagemanager/stopcachingimages(for:targetsize:contentmode:options:))*