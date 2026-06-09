# insert(_:for:)

**Framework**: Core AI  
**Kind**: method

Insert the mutable view for the value named `name`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func insert(_ mutableRawView: consuming NDArray.MutableRawView, for name: String)
```

## Parameters

- `mutableRawView`: A mutable raw view of the ndArray to be used as the value.
- `name`: The name of the value that this view should be used for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/mutableviews/insert(_:for:)-9ixpc)*