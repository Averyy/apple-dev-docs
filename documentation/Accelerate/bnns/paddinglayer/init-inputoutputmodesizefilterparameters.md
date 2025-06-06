# init(input:output:mode:size:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new padding layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, mode: BNNS.PaddingMode, size: [(x: Int, y: Int)], filterParameters: BNNSFilterParameters? = nil)
```

#### Discussion

> ❗ **Important**:  Padding isn’t supported beyond 4D tensors.

 Padding isn’t supported beyond 4D tensors.

## Parameters

- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `mode`: The mode the operation uses to pad.
- `size`: The number of padding elements to add before and after the original data.
- `filterParameters`: The filter runtime parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/paddinglayer/init(input:output:mode:size:filterparameters:))*