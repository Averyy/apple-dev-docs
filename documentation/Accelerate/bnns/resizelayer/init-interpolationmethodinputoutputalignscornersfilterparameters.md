# init(interpolationMethod:input:output:alignsCorners:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new resize layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- tvOS 14.0+

## Declaration

```swift
convenience init?(interpolationMethod: BNNS.InterpolationMethod, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, alignsCorners: Bool, filterParameters: BNNSFilterParameters? = nil)
```

#### Discussion

> ❗ **Important**:  The number of input dimensions must be equal to number of output dimensions. The resize must be in same direction for all dimensions.

 The number of input dimensions must be equal to number of output dimensions. The resize must be in same direction for all dimensions.

## Parameters

- `interpolationMethod`: The interpolation method for resizing.
- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `alignsCorners`: A Boolean value that specifies whether to align the corners of the upscaling grid to the center of scaling dimensions instead of to the edges.
- `filterParameters`: The filter runtime parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/resizelayer/init(interpolationmethod:input:output:alignscorners:filterparameters:))*