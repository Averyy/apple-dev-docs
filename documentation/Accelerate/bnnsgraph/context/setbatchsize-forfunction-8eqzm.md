# setBatchSize(_:forFunction:)

**Framework**: Accelerate  
**Kind**: method

Synchronously sets the batch size for a graph.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func setBatchSize(_ batchSize: Int, forFunction function: String? = nil)
```

#### Discussion

This is a special case of `setDynamicShapes(_:forFunction:)` where the only dynamic sizes that occur are the first index of their tensor (that is, the batch dimension) and are all equal. This allows just passing a single `batchSize` constant.

This function has no effect if you pass a `batchSize` value that’s less than zero.

> **Note**: `BNNSGraphContextSetBatchSize`

## Parameters

- `batchSize`: The batch size.
- `function`: The specific function to set shapes for. You may set this to   if there is only one function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/context/setbatchsize(_:forfunction:)-8eqzm)*