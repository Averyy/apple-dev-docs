# loadContentsOfURL:completionHandler:

**Framework**: Core ML  
**Kind**: method  
**Role**: Type Method

Construct the model structure asynchronously given the location of its on-disk representation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```objc
+ (void) loadContentsOfURL:(NSURL *) url completionHandler:(void (^)(MLModelStructure *modelStructure, NSError *error)) handler;
```

## Parameters

- `url`: The location of its on-disk representation (.mlmodelc directory).
- `handler`: When the model structure is constructed successfully or unsuccessfully, the completion handler is invoked with a valid MLModelStructure instance or NSError object.

## See Also

### Loading a model structure
- [+ loadModelAsset:completionHandler:](./loadmodelasset_completionhandler_.md)
  Construct the model structure asynchronously  given the model asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelstructure-c.class/loadcontentsofurl:completionhandler:)*