# init(dimensions:)

**Framework**: ML Compute  
**Kind**: init

Creates a transpose layer with the dimensions you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(dimensions: [Int])
```

#### Discussion

The `dimensions` array contains an input axis source for each output axis. In other words, the `n`th element in the dimensions array specifies the input axis source for the `n`th axis in the output. You can’t transpose the batch dimension, which is typically axis 0.

## Parameters

- `dimensions`: An array that represents the ordering of dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctransposelayer/init(dimensions:))*