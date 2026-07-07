# view

**Framework**: Core AI  
**Kind**: property

An immutable view of this mutable view.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@export(implementation)
var view: NDArray.View<Element> { get }
```

## See Also

- [var mutableRawView: NDArray.MutableRawView](ndarray/mutableview/mutablerawview.md)
  Returns a mutable raw view over the same data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutableview/view)*