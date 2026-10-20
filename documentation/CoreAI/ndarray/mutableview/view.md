# view

**Framework**: Core AI  
**Kind**: property  
**Role**: Instance Property

An immutable view of this mutable view.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@export(implementation)
var view: NDArray.View<Element> { get }
```

Available when `Element` conforms to `BitwiseCopyable`.

## See Also

### Converting to other views
- [var mutableRawView: NDArray.MutableRawView](./mutablerawview.md)
  Returns a mutable raw view over the same data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutableview/view)*