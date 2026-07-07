# mutableView(as:)

**Framework**: Core AI  
**Kind**: method

Returns a mutable, typed view of this array’s elements.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func mutableView<T>(as type: T.Type = T.self) -> NDArray.MutableView<T> where T : BitwiseCopyable
```

## Mentions

- [Integrating on-device AI models in your app with Core AI](integrating-on-device-ai-models-in-your-app-with-core-ai.md)

#### Return Value

A mutable view of the array’s elements.

## Parameters

- `type`: The Swift type that corresponds to this array’s [`scalarType`](ndarray/scalartype-swift.property.md). For example, pass `Int32.self` for an array with scalar type `.int32`.

## See Also

- [func view<T>(as: T.Type) -> NDArray.View<T>](ndarray/view(as:).md)
  Returns a read-only, typed view of this array’s elements.
- [func rawView() -> NDArray.RawView](ndarray/rawview.md)
  Returns a read-only, raw view of this array’s storage.
- [func mutableRawView() -> NDArray.MutableRawView](ndarray/mutablerawview.md)
  Returns a mutable, raw view of this array’s storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutableview(as:))*