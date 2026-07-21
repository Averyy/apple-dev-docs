# UIBarMinimizationRestorationBehavior.automatic

**Framework**: UIKit  
**Kind**: case

The system determines the restoration behavior.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case automatic
```

#### Discussion

By default, the bar restores when the user reverses scroll direction. The system selects [`UIBarMinimizationRestorationBehavior.atScrollEdge`](uibarminimizationrestorationbehavior/atscrolledge.md) automatically for navigation items whose `preferredSearchBarPlacement` is `.integratedCentered`.

## See Also

- [UIBarMinimizationRestorationBehavior.atScrollEdge](uibarminimizationrestorationbehavior/atscrolledge.md)
  The bar restores only when the observed scroll view’s content reaches the scroll edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarminimizationrestorationbehavior/automatic)*