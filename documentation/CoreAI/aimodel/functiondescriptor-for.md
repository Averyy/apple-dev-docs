# functionDescriptor(for:)

**Framework**: Core AI  
**Kind**: method

Returns a descriptor for the specified function.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func functionDescriptor(for functionName: String) -> InferenceFunctionDescriptor?
```

#### Return Value

A descriptor for the function, or `nil` if the model doesn’t contain a function with the specified name.

#### Discussion

Use the descriptor to inspect the function’s inputs, outputs, and state names before loading it for inference.

## Parameters

- `functionName`: The name of the function to describe.

## See Also

- [func loadFunction(named: String) throws -> InferenceFunction?](aimodel/loadfunction(named:).md)
- [var functionNames: [String]](aimodel/functionnames.md)
  The names of the inference functions in this model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodel/functiondescriptor(for:))*