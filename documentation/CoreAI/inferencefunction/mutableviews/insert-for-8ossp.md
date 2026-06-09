# insert(_:for:)

**Framework**: Core AI  
**Kind**: method

Insert the mutable view to be used as the ndArray value named `name`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func insert<Element>(_ mutableView: consuming NDArray.MutableView<Element>, for name: String) where Element : BitwiseCopyable
```

## Parameters

- `mutableView`: A mutable view of the ndArray to be used as the value.
- `name`: The name of the value that this view should be used for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/mutableviews/insert(_:for:)-8ossp)*