# stateNames

**Framework**: Core AI  
**Kind**: property  
**Role**: Instance Property

The names of the function’s states.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var stateNames: [String] { get }
```

## Discussion

States are function arguments that the function both reads and writes during inference. You must provide a mutable view for every state when calling [`run(inputs:states:outputViews:)`](../inferencefunction/run%28inputs,states,outputviews%29-14emi.md).

## See Also

### Describing state
- [func stateDescriptor(of: String) -> InferenceValue.Descriptor?](./statedescriptor%28of%29.md)
  Returns the descriptor for the specified state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunctiondescriptor/statenames)*