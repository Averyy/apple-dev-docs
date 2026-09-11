# remove(_:)

**Framework**: Core AI  
**Kind**: method

Removes and returns the output value with the specified name.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
mutating func remove(_ outputName: String) -> InferenceValue?
```

## Mentions

- [Integrating on-device AI models in your app with Core AI](integrating-on-device-ai-models-in-your-app-with-core-ai.md)

#### Return Value

The output value, or `nil` if no output with the specified name exists.

#### Discussion

After you remove a value, subsequent calls with the same name return `nil`.

## Parameters

- `outputName`: The name of the output to remove.

## See Also

- [var count: Int](inferencefunction/outputs/count.md)
  The number of outputs in this collection.
- [var names: some Collection<String>](inferencefunction/outputs/names.md)
  The names of the outputs in this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/outputs/remove(_:))*