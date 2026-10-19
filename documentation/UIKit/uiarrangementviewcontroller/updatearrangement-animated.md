# updateArrangement(_:animated:)

**Framework**: UIKit  
**Kind**: method

Updates the arrangement of the view controller.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
@MainActor
@preconcurrency final func updateArrangement<A>(_ arrangement: A, animated: Bool = false) where A : UIArrangementViewController.Arrangement
```

## Parameters

- `arrangement`: The arrangement to apply.
- `animated`: Whether to animate the arrangement transition.

## See Also

- [struct UIOverlayArrangement](uioverlayarrangement-swift.struct.md)
  An arrangement that layers the primary view over the secondary view, or places the views side by side on a folded display.
- [struct UISplitArrangement](uisplitarrangement-swift.struct.md)
  An arrangement that places the primary and secondary views side by side along one or more axes.
- [UIArrangementViewController.Arrangement](uiarrangementviewcontroller/arrangement.md)
  A type that describes how an arrangement view controller lays out its view controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/updatearrangement(_:animated:))*