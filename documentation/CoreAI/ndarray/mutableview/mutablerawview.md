# mutableRawView

**Framework**: Core AI  
**Kind**: property  
**Role**: Instance Property

Returns a mutable raw view over the same data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@export(implementation)
var mutableRawView: NDArray.MutableRawView { get }
```

Available when `Element` conforms to `BitwiseCopyable`.

## See Also

### Converting to other views
- [var view: NDArray.View<Element>](./view.md)
  An immutable view of this mutable view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutableview/mutablerawview)*