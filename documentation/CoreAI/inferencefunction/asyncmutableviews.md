# InferenceFunction.AsyncMutableViews

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

A collection of mutable references to async states, used as the states argument to an inference function.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct AsyncMutableViews
```

## Topics

### Creating a collection
- [init()](./asyncmutableviews/init%28%29.md)
  Initialize an empty `AsyncMutableViews`.
### Adding values
- [func insert(inout InferenceFunction.AsyncMutableValue, for: String)](./asyncmutableviews/insert%28_,for%29.md)
  Insert the view to be used as the async mutable value for `name`.

## See Also

### Asynchronous inference
- [InferenceFunction.AsyncValue](./asyncvalue.md)
  A future which will provide an inference value once any pending write is complete.
- [InferenceFunction.AsyncMutableValue](./asyncmutablevalue.md)
  An async value which can be provided as a mutable argument to an inference function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncmutableviews)*