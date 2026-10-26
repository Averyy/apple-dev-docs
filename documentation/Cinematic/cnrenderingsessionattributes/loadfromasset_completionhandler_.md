# loadFromAsset:completionHandler:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Type Method

Loads the rendering session attributes from an asset asynchronously.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
+ (void) loadFromAsset:(AVAsset *) asset completionHandler:(void (^)(CNRenderingSessionAttributes *sessionAttributes, NSError *error)) completionHandler;
```

## Parameters

- `asset`: The Cinematic asset to load.
- `completionHandler`: Calls with the loaded Cinematic script when done, or an error if it fails. If progress cancels before it completes, the completion handler is an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnrenderingsessionattributes/loadfromasset:completionhandler:)*