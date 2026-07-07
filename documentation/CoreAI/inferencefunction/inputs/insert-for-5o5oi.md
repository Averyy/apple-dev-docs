# insert(_:for:)

**Framework**: Core AI  
**Kind**: method

Inserts a typed array view as the input with the specified name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func insert<Element>(_ view: consuming NDArray.View<Element>, for inputName: String) where Element : BitwiseCopyable
```

## Parameters

- `view`: A typed view of the array to use as the input value.
- `inputName`: The name of the input to set.

## See Also

- [func insert(consuming NDArray.RawView, for: String)](inferencefunction/inputs/insert(_:for:)-3eg32.md)
  Inserts a raw array view as the input with the specified name.
- [func insert(borrowing some InferenceValue.ViewRepresentable & ~Copyable, for: String)](inferencefunction/inputs/insert(_:for:)-2htrp.md)
  Inserts a view of the value as the input with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/inputs/insert(_:for:)-5o5oi)*