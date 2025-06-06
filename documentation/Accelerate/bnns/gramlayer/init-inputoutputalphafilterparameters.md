# init(input:output:alpha:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new Gram matrix layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, alpha: Float, filterParameters: BNNSFilterParameters? = nil)
```

## Parameters

- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `alpha`: A value to scale the result.
- `filterParameters`: The filter runtime parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/gramlayer/init(input:output:alpha:filterparameters:))*