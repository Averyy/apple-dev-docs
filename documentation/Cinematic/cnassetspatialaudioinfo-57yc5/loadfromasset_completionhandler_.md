# loadFromAsset:completionHandler:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```objc
+ (void) loadFromAsset:(AVAsset *) asset completionHandler:(void (^)(CNAssetSpatialAudioInfo *assetInfo, NSError *error)) completionHandler;
```

## Discussion

Returns an instance of CNAssetAudioInfo for an AVAsset object asynchronously.

## Parameters

- `asset`: An instance of AVAsset
- `completionHandler`: Completion handler to return the result


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetspatialaudioinfo-57yc5/loadfromasset:completionhandler:)*