# InferenceFunction.MutableViews

**Framework**: Core AI  
**Kind**: struct

A collection of `InferenceValue.MutableView`s which can be updated in-place by an `InferenceFunction`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct MutableViews
```

## Topics

### Creating a collection
- [init()](inferencefunction/mutableviews/init.md)
  Initialize an empty instance.
### Adding views
- [func insert(inout some InferenceValue.MutableViewRepresentable & ~Copyable, for: String)](inferencefunction/mutableviews/insert(_:for:)-1b2yx.md)
  Insert a new value to the output views.
- [func insert<Element>(consuming NDArray.MutableView<Element>, for: String)](inferencefunction/mutableviews/insert(_:for:)-8ossp.md)
  Insert the mutable view to be used as the ndArray value named `name`.
- [func insert(consuming NDArray.MutableRawView, for: String)](inferencefunction/mutableviews/insert(_:for:)-9ixpc.md)
  Insert the mutable view for the value named `name`.

## See Also

- [InferenceFunction.Inputs](inferencefunction/inputs.md)
  A collection of named input values for an inference function.
- [InferenceFunction.Outputs](inferencefunction/outputs.md)
  The output values produced by running an inference function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/mutableviews)*