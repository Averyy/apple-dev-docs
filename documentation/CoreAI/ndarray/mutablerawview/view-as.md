# view(as:)

**Framework**: Core AI  
**Kind**: method

Create a typed `MutableView` of the same storage as this raw view.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
consuming func view<T>(as type: T.Type = T.self) -> NDArray.MutableView<T> where T : BitwiseCopyable
```

#### Return Value

A mutable view of the tensor.

## Parameters

- `type`: Must be the type corresponding to the `ScalarType` of this tensor. For example if this tensor has scalar type `.int32` then you would pass `Int32.self` for type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutablerawview/view(as:))*