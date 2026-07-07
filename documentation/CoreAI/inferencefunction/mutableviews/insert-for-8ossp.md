# insert(_:for:)

**Framework**: Core AI  
**Kind**: method

Insert the mutable view to be used as the ndArray value named `name`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func insert<Element>(_ mutableView: consuming NDArray.MutableView<Element>, for name: String) where Element : BitwiseCopyable
```

## Parameters

- `mutableView`: A mutable view of the ndArray to be used as the value.
- `name`: The name of the value that this view should be used for.

## See Also

- [func insert(inout some InferenceValue.MutableViewRepresentable & ~Copyable, for: String)](inferencefunction/mutableviews/insert(_:for:)-1b2yx.md)
  Insert a new value to the output views.
- [func insert(consuming NDArray.MutableRawView, for: String)](inferencefunction/mutableviews/insert(_:for:)-9ixpc.md)
  Insert the mutable view for the value named `name`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/mutableviews/insert(_:for:)-8ossp)*