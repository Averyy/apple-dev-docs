# outputDescriptor(of:)

**Framework**: Core AI  
**Kind**: method  
**Role**: Instance Method

Returns the descriptor for the specified output.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func outputDescriptor(of outputName: String) -> InferenceValue.Descriptor?
```

## Return Value

The descriptor for the output, or `nil` if the function doesn’t have an output with the specified name.

## Parameters

- `outputName`: The name of the output.

## See Also

### Describing outputs
- [var outputCount: Int](./outputcount.md)
  The number of outputs the function produces.
- [var outputNames: [String]](./outputnames.md)
  The names of the function’s outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunctiondescriptor/outputdescriptor(of:))*