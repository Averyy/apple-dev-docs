# init(span:shape:strides:)

**Framework**: Core AI  
**Kind**: init

Initialize a view from a `Span`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(span: Span<Element>, shape: [Int], strides: [Int] = [])
```

#### Discussion

The lifetime of the resulting view copies the lifetime of the provided span.

Also note that the `shape/strides` must not be able to produce offsets that go outside of the range of `span`. As such, negative strides are not supported by this initializer.

**Performance note**: Making an ndArray view from a normal VM pointer to be used as an input or backing of an [`InferenceFunction`](inferencefunction.md) could be a performance anti-pattern if you intend to pass the same underlying memory in repeatedly to many inferences. This can be a function of which compute units the model was specialized for. For example if the inference function runs compute on the GPU or Neural Engine, you may incur a copy of the view into the required memory primitive if it cannot be toll-free converted.

- span: The span to be referenced by the resulting view.
- shape: The shape of the resulting view.
- strides: The strides of the resulting view. If left empty, they will be computed as contiguous row-major.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/view/init(span:shape:strides:))*