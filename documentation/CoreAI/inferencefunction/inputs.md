# InferenceFunction.Inputs

**Framework**: Core AI  
**Kind**: struct

A collection of named input values for an inference function.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Inputs
```

#### Overview

Build an `Inputs` collection by calling `insert(_:for:)` for each named input the function expects, then pass it to `InferenceFunction/run(inputs:states:outputViews:)`.

## Topics

### Creating inputs
- [init()](inferencefunction/inputs/init.md)
  Creates an empty set of inputs.
### Adding inputs
- [func insert(consuming NDArray.RawView, for: String)](inferencefunction/inputs/insert(_:for:)-3eg32.md)
  Inserts a raw array view as the input with the specified name.
- [func insert(borrowing some InferenceValue.ViewRepresentable & ~Copyable, for: String)](inferencefunction/inputs/insert(_:for:)-2htrp.md)
  Inserts a view of the value as the input with the specified name.
- [func insert<Element>(consuming NDArray.View<Element>, for: String)](inferencefunction/inputs/insert(_:for:)-5o5oi.md)
  Inserts a typed array view as the input with the specified name.

## See Also

- [InferenceFunction.Outputs](inferencefunction/outputs.md)
  The output values produced by running an inference function.
- [InferenceFunction.MutableViews](inferencefunction/mutableviews.md)
  A collection of `InferenceValue.MutableView`s which can be updated in-place by an `InferenceFunction`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/inputs)*