# SecTransformExecuteAsync(_:_:_:)

**Framework**: Security  
**Kind**: func

Executes transform or transform group asynchronously.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTransformExecuteAsync(_ transformRef: SecTransform, _ deliveryQueue: dispatch_queue_t, _ deliveryBlock: @escaping SecMessageBlock)
```

#### Discussion

SecTransformExecuteAsync works just like the SecTransformExecute API except that it returns results to the deliveryBlock. There may be multple results depending on the transform. The block knows that the processing is complete when the isFinal parameter is set to true. If an error occurs the block’s error parameter is set and the isFinal parameter will be set to true.

## Parameters

- `transformRef`: The transform to execute.
- `deliveryQueue`: A dispatch queue on which to deliver the results of this transform.
- `deliveryBlock`: A SecMessageBlock to asynchronously receive the results of the transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformexecuteasync(_:_:_:))*