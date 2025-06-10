# apply(input:regionOfInterest:output:filterParameters:)

**Framework**: Accelerate  
**Kind**: method

Applies the layer to a set of input objects, writing the result to a set of output objects.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+
- Unknown ?+ - Deprecated
- Mac Catalyst ?+

## Declaration

```swift
func apply(input: BNNSNDArrayDescriptor, regionOfInterest: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters? = nil) throws
```

## See Also

- [func applyBackward(regionOfInterest: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](bnns/cropresizelayer/applybackward(regionofinterest:outputgradient:generatinginputgradient:filterparameters:).md)
  Applies a crop-resize filter backward to generate an input gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/cropresizelayer/apply(input:regionofinterest:output:filterparameters:))*