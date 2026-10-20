# NSScrollView.Elasticity

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

These constants determine the elasticity behavior for an axis of the scrollview.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum Elasticity
```

```c
enum NSScrollElasticity : NSInteger;
```

## Topics

### Constants
- [NSScrollView.Elasticity.automatic](./elasticity/automatic.md)
  Automatically determine whether to allow elasticity on this axis.
- [NSScrollView.Elasticity.none](./elasticity/none.md)
  Disallow scrolling beyond document bounds on this axis.
- [NSScrollView.Elasticity.allowed](./elasticity/allowed.md)
  Allow content to be scrolled past its bounds on this axis in an elastic fashion.
### Initializers
- [init?(rawValue: Int)](./elasticity/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [NSScrollView.FindBarPosition](./findbarposition-swift.enum.md)
  These constants define the position of the find bar in relation to the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/elasticity)*