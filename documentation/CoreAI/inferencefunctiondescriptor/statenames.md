# stateNames

**Framework**: Core AI  
**Kind**: property

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

#### Discussion

States are function arguments that the function both reads and writes during inference. You must provide a mutable view for every state when calling [`run(inputs:states:outputViews:)`](inferencefunction/run(inputs:states:outputviews:)-14emi.md).

## See Also

- [func stateDescriptor(of: String) -> InferenceValue.Descriptor?](inferencefunctiondescriptor/statedescriptor(of:).md)
  Returns the descriptor for the specified state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunctiondescriptor/statenames)*