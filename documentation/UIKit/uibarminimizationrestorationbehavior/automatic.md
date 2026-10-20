# UIBarMinimizationRestorationBehavior.automatic

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

The system determines the restoration behavior.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case automatic
```

```c
UIBarMinimizationRestorationBehaviorAutomatic
```

#### Discussion

By default, the bar restores when the user reverses scroll direction. The system selects [`UIBarMinimizationRestorationBehavior.atScrollEdge`](./atscrolledge.md) automatically for navigation items whose `preferredSearchBarPlacement` is `.integratedCentered`.

## See Also

### Restoring the bar
- [UIBarMinimizationRestorationBehavior.atScrollEdge](./atscrolledge.md)
  The bar restores only when the observed scroll view’s content reaches the scroll edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarminimizationrestorationbehavior/automatic)*