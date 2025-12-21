# applyBackward(regionOfInterest:outputGradient:generatingInputGradient:filterParameters:)

**Framework**: Accelerate  
**Kind**: method

Applies a crop-resize filter backward to generate an input gradient.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func applyBackward(regionOfInterest: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient inputGradient: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters? = nil) throws
```

## See Also

- [func apply(input: BNNSNDArrayDescriptor, regionOfInterest: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](bnns/cropresizelayer/apply(input:regionofinterest:output:filterparameters:).md)
  Applies the layer to a set of input objects, writing the result to a set of output objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/cropresizelayer/applybackward(regionofinterest:outputgradient:generatinginputgradient:filterparameters:))*