# checkCinematicCapabilityForAsset:completionHandler:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Type Method

Asynchronously checks the cinematic capability of an asset. The completionHandler returns: CNCinematicCapabilityNone if a cinematic metadata track is not present. CNCinematicCapabilityRenderable if the cinematic asset can be used without preprocessing CNCinematicCapabilityNeedsPreprocessing If cinematic asset needs preprocessing before it can be used For assets that need preprocessing use [CNAssetInfo preprocessAssetWithConfiguration:completionHandler:] before using the asset

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```objc
+ (void) checkCinematicCapabilityForAsset:(AVAsset *) asset completionHandler:(void (^)(CNCinematicCapability capability)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetinfo-8ja4t/checkcinematiccapabilityforasset:completionhandler:)*