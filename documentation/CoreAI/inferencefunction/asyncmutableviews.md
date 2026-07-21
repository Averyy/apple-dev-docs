# InferenceFunction.AsyncMutableViews

**Framework**: Core AI  
**Kind**: struct

A collection of mutable references to async states, used as the states argument to an inference function.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct AsyncMutableViews
```

## Topics

### Creating a collection
- [init()](inferencefunction/asyncmutableviews/init.md)
  Initialize an empty `AsyncMutableViews`.
### Adding values
- [func insert(inout InferenceFunction.AsyncMutableValue, for: String)](inferencefunction/asyncmutableviews/insert(_:for:).md)
  Insert the view to be used as the async mutable value for `name`.

## See Also

- [InferenceFunction.AsyncValue](inferencefunction/asyncvalue.md)
  A future which will provide an inference value once any pending write is complete.
- [InferenceFunction.AsyncMutableValue](inferencefunction/asyncmutablevalue.md)
  An async value which can be provided as a mutable argument to an inference function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncmutableviews)*