# NSScrollView.Elasticity

**Framework**: AppKit  
**Kind**: enum

These constants determine the elasticity behavior for an axis of the scrollview.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum Elasticity
```

## Topics

### Constants
- [NSScrollView.Elasticity.automatic](nsscrollview/elasticity/automatic.md)
  Automatically determine whether to allow elasticity on this axis.
- [NSScrollView.Elasticity.none](nsscrollview/elasticity/none.md)
  Disallow scrolling beyond document bounds on this axis.
- [NSScrollView.Elasticity.allowed](nsscrollview/elasticity/allowed.md)
  Allow content to be scrolled past its bounds on this axis in an elastic fashion.
### Initializers
- [init?(rawValue: Int)](nsscrollview/elasticity/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSScrollView.FindBarPosition](nsscrollview/findbarposition-swift.enum.md)
  These constants define the position of the find bar in relation to the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/elasticity)*