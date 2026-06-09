# init(commandQueue:)

**Framework**: Core AI  
**Kind**: init

Initialize a compute stream which will encode its work to the provided command queue.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(commandQueue: any MTLCommandQueue)
```

#### Discussion

You can use this to encode inferences to your own metal queue.

## Parameters

- `commandQueue`: The queue which inference will be encoded to when running [`encode(inputs:states:outputViews:to:)`](inferencefunction/encode(inputs:states:outputviews:to:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/computestream/init(commandqueue:))*