# InferenceFunction.MutableViews

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

A collection of `InferenceValue.MutableView`s which can be updated in-place by an `InferenceFunction`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct MutableViews
```

## Topics

### Creating a collection
- [init()](./mutableviews/init%28%29.md)
  Initialize an empty instance.
### Adding views
- [func insert(inout some InferenceValue.MutableViewRepresentable & ~Copyable, for: String)](./mutableviews/insert%28_,for%29-1b2yx.md)
  Insert a new value to the output views.
- [func insert<Element>(consuming NDArray.MutableView<Element>, for: String)](./mutableviews/insert%28_,for%29-8ossp.md)
  Insert the mutable view to be used as the ndArray value named `name`.
- [func insert(consuming NDArray.MutableRawView, for: String)](./mutableviews/insert%28_,for%29-9ixpc.md)
  Insert the mutable view for the value named `name`.

## See Also

### Supporting types
- [InferenceFunction.Inputs](./inputs.md)
  A collection of named input values for an inference function.
- [InferenceFunction.Outputs](./outputs.md)
  The output values produced by running an inference function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/mutableviews)*