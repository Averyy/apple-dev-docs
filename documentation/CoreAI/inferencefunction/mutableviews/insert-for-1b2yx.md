# insert(_:for:)

**Framework**: Core AI  
**Kind**: method

Insert a new value to the output views.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func insert(_ value: inout some InferenceValue.MutableViewRepresentable & ~Copyable, for name: String)
```

## Parameters

- `value`: The value which will be updated in-place.
- `name`: The name of the value that this view should be used for.

## See Also

- [func insert<Element>(consuming NDArray.MutableView<Element>, for: String)](inferencefunction/mutableviews/insert(_:for:)-8ossp.md)
  Insert the mutable view to be used as the ndArray value named `name`.
- [func insert(consuming NDArray.MutableRawView, for: String)](inferencefunction/mutableviews/insert(_:for:)-9ixpc.md)
  Insert the mutable view for the value named `name`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/mutableviews/insert(_:for:)-1b2yx)*