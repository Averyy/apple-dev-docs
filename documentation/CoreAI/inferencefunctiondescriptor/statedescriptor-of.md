# stateDescriptor(of:)

**Framework**: Core AI  
**Kind**: method

Returns the descriptor for the specified state.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func stateDescriptor(of stateName: String) -> InferenceValue.Descriptor?
```

#### Return Value

The descriptor for the state, or `nil` if the function doesn’t have a state with the specified name.

## Parameters

- `stateName`: The name of the state.

## See Also

- [var stateNames: [String]](inferencefunctiondescriptor/statenames.md)
  The names of the function’s states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunctiondescriptor/statedescriptor(of:))*