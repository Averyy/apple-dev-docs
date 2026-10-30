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

### Specifying the scroll view elasticity
- [var horizontalScrollElasticity: NSScrollView.Elasticity](./horizontalscrollelasticity.md)
  The scroll view’s horizontal scrolling elasticity mode.
- [var verticalScrollElasticity: NSScrollView.Elasticity](./verticalscrollelasticity.md)
  The scroll view’s vertical scrolling elasticity mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/elasticity)*