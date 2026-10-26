# loadFromAsset:completionHandler:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Type Method

Loads the Cinematic asset information.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
+ (void) loadFromAsset:(AVAsset *) asset completionHandler:(void (^)(CNAssetInfo *cinematicAssetInfo, NSError *error)) completionHandler;
```

## Parameters

- `asset`: The Cinematic asset of interest to load.
- `completionHandler`: Called when the loaded Cinematic asset loads, or with an error if it fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetinfo-8ja4t/loadfromasset:completionhandler:)*