# UIBarMinimizationRestorationBehavior.atScrollEdge

**Framework**: UIKit  
**Kind**: case

The bar restores only when the observed scroll view’s content reaches the scroll edge.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
case atScrollEdge
```

#### Discussion

Currently this is only honored alongside `UIBarMinimizationBehaviorOnScrollDown`. With other minimization behaviors, the system falls back to [`UIBarMinimizationRestorationBehavior.automatic`](uibarminimizationrestorationbehavior/automatic.md).

## See Also

- [UIBarMinimizationRestorationBehavior.automatic](uibarminimizationrestorationbehavior/automatic.md)
  The system determines the restoration behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarminimizationrestorationbehavior/atscrolledge)*