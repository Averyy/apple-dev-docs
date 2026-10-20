# insert(_:for:)

**Framework**: Core AI  
**Kind**: method  
**Role**: Instance Method

Inserts a view of the value as the input with the specified name.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
mutating func insert(_ value: borrowing some InferenceValue.ViewRepresentable & ~Copyable, for inputName: String)
```

## Mentions

- [Integrating on-device AI models in your app with Core AI](../../integrating-on-device-ai-models-in-your-app-with-core-ai.md)

## Parameters

- `value`: The value to borrow as an input.
- `inputName`: The name of the input to set.

## See Also

### Adding inputs
- [func insert(consuming NDArray.RawView, for: String)](./insert%28_,for%29-3eg32.md)
  Inserts a raw array view as the input with the specified name.
- [func insert<Element>(consuming NDArray.View<Element>, for: String)](./insert%28_,for%29-5o5oi.md)
  Inserts a typed array view as the input with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/inputs/insert(_:for:)-2htrp)*