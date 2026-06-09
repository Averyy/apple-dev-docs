# outputDescriptor(of:)

**Framework**: Core AI  
**Kind**: method

Returns the descriptor for the specified output.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func outputDescriptor(of outputName: String) -> InferenceValue.Descriptor?
```

#### Return Value

The descriptor for the output, or `nil` if the function doesn’t have an output with the specified name.

## Parameters

- `outputName`: The name of the output.

## See Also

- [var outputCount: Int](inferencefunctiondescriptor/outputcount.md)
  The number of outputs the function produces.
- [var outputNames: [String]](inferencefunctiondescriptor/outputnames.md)
  The names of the function’s outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunctiondescriptor/outputdescriptor(of:))*