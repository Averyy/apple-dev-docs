# applyBackward(regionOfInterest:outputGradient:generatingInputGradient:filterParameters:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Applies a crop-resize filter backward to generate an input gradient.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
func applyBackward(regionOfInterest: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient inputGradient: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters? = nil) throws
```

## See Also

### Applying a Crop-Resize Layer
- [func apply(input: BNNSNDArrayDescriptor, regionOfInterest: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](./apply%28input,regionofinterest,output,filterparameters%29.md)
  Applies the layer to a set of input objects, writing the result to a set of output objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/cropresizelayer/applybackward(regionofinterest:outputgradient:generatinginputgradient:filterparameters:))*