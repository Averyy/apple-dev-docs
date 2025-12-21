# streamingAdvanceCount

**Framework**: Accelerate  
**Kind**: property

Sets streaming advancement amount for cases with dynamically shaped inputs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var streamingAdvanceCount: Int { get set }
```

#### Discussion

For models compiled with the `BNNSOption` attribute `StateMode=Streaming` enabled, where `slice_update` operations use an update parameter of dynamic shape, BNNS can’t unambigiously determine the streaming advancement size. In this case, call this function before calling [`BNNSGraphContextExecute(_:_:_:_:_:_:)`](bnnsgraphcontextexecute(_:_:_:_:_:_:).md) to set the advancement size for each frame.

This function advances the internal state pointer by `advance_count` elements in the streaming dimension before returning from [`BNNSGraphContextExecute(_:_:_:_:_:_:)`](bnnsgraphcontextexecute(_:_:_:_:_:_:).md).

> **Note**: The BNNS streaming APIs do not support models that require different advancement amounts for different states.

## Parameters

- `context`: The graph context.
- `advance_count`: An integer value that specifies the number of elements that the function advances the internal state pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/context/streamingadvancecount)*