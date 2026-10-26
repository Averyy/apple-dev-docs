# preprocessAssetWithConfiguration:completionHandler:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Preprocesses the asset by generating a disparity track, writing the result to the URL specified in `configuration`. Required for assets whose `cinematicCapability` is \c CNCinematicCapabilityNeedsPreprocessing; on success \c assetInfo will be \c CNCinematicCapabilityRenderable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```objc
- (NSProgress *) preprocessAssetWithConfiguration:(CNAssetPreprocessConfiguration *) configuration completionHandler:(void (^)(CNAssetInfo *assetInfo, NSError *error)) completionHandler;
```

#### Return Value

A \c NSProgress tracking preprocessing progress.

#### Discussion

Ensure \c resourceStatus is ready before calling — download resources first if needed.

## Parameters

- `configuration`: Destination URL and whether to embed or reference source tracks.
- `completionHandler`: Called on completion; on success \c assetInfo is the new preprocessed asset and \c error is \c nil. On failure \c assetInfo is \c nil and \c error is non-nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetinfo-8ja4t/preprocessassetwithconfiguration:completionhandler:)*