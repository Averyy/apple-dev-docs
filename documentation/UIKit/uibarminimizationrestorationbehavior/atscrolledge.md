# UIBarMinimizationRestorationBehavior.atScrollEdge

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

The bar restores only when the observed scroll view’s content reaches the scroll edge.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
case atScrollEdge
```

```c
UIBarMinimizationRestorationBehaviorAtScrollEdge
```

## Discussion

Currently this is only honored alongside `UIBarMinimizationBehaviorOnScrollDown`. With other minimization behaviors, the system falls back to [`UIBarMinimizationRestorationBehavior.automatic`](./automatic.md).

## See Also

### Restoring the bar
- [UIBarMinimizationRestorationBehavior.automatic](./automatic.md)
  The system determines the restoration behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarminimizationrestorationbehavior/atscrolledge)*