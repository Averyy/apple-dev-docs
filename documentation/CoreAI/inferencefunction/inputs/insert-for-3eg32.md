# insert(_:for:)

**Framework**: Core AI  
**Kind**: method

Inserts a raw array view as the input with the specified name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func insert(_ rawView: consuming NDArray.RawView, for inputName: String)
```

## Parameters

- `rawView`: A raw view of the array to use as the input value.
- `inputName`: The name of the input to set.

## See Also

- [func insert(borrowing some InferenceValue.ViewRepresentable & ~Copyable, for: String)](inferencefunction/inputs/insert(_:for:)-2htrp.md)
  Inserts a view of the value as the input with the specified name.
- [func insert<Element>(consuming NDArray.View<Element>, for: String)](inferencefunction/inputs/insert(_:for:)-5o5oi.md)
  Inserts a typed array view as the input with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/inputs/insert(_:for:)-3eg32)*