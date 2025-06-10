# setBatchSize(_:forFunction:)

**Framework**: Accelerate  
**Kind**: method

Sets the batch size for a graph.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+
- watchOS 11.0+

## Declaration

```swift
func setBatchSize(_ batchSize: Int, forFunction function: String? = nil) async
```

#### Discussion

This is a special case of `setDynamicShapes(_:forFunction:)` where the only dynamic sizes that occur are the first index of their tensor (that is, the batch dimension) and are all equal. This allows just passing a single `batchSize` constant.

This function has no effect if you pass a `batchSize` value that’s less than zero.

> **Note**: `BNNSGraphContextSetBatchSize`

## Parameters

- `batchSize`: The batch size.
- `function`: The specific function to set shapes for. You may set this to   if there is only one function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/context/setbatchsize(_:forfunction:)-4872x)*