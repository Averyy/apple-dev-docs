# mutableRawView()

**Framework**: Core AI  
**Kind**: method  
**Role**: Instance Method

Returns a mutable, raw view of this array’s storage.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
mutating func mutableRawView() -> NDArray.MutableRawView
```

#### Return Value

A mutable raw view of the array’s underlying bytes.

## See Also

### Accessing elements
- [func view<T>(as: T.Type) -> NDArray.View<T>](./view%28as%29.md)
  Returns a read-only, typed view of this array’s elements.
- [func mutableView<T>(as: T.Type) -> NDArray.MutableView<T>](./mutableview%28as%29.md)
  Returns a mutable, typed view of this array’s elements.
- [func rawView() -> NDArray.RawView](./rawview%28%29.md)
  Returns a read-only, raw view of this array’s storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutablerawview())*