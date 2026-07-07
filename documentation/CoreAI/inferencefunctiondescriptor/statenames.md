# stateNames

**Framework**: Core AI  
**Kind**: property

The names of the function’s states.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var stateNames: [String] { get }
```

#### Discussion

States are function arguments that the function both reads and writes during inference. You must provide a mutable view for every state when calling `InferenceFunction/run(inputs:states:outputViews:)`.

## See Also

- [func stateDescriptor(of: String) -> InferenceValue.Descriptor?](inferencefunctiondescriptor/statedescriptor(of:).md)
  Returns the descriptor for the specified state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunctiondescriptor/statenames)*