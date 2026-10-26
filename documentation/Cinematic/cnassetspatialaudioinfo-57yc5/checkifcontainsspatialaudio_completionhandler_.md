# checkIfContainsSpatialAudio:completionHandler:

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
+ (void) checkIfContainsSpatialAudio:(AVAsset *) asset completionHandler:(void (^)(BOOL result)) completionHandler;
```

#### Discussion

Check if asset meets all the requirements to operate with Spatial Audio and its accompanying effects

## Parameters

- `asset`: An instance of AVAsset.
- `completionHandler`: Completion handler to return the result


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetspatialaudioinfo-57yc5/checkifcontainsspatialaudio:completionhandler:)*