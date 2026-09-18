# updateArrangement(_:animated:)

**Framework**: UIKit  
**Kind**: method

Updates the arrangement of the view controller.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency final func updateArrangement<A>(_ arrangement: A, animated: Bool = false) where A : UIArrangementViewController.Arrangement
```

## Parameters

- `arrangement`: The arrangement to apply.
- `animated`: Whether to animate the arrangement transition.

## See Also

- [UIArrangementViewController.Arrangement](uiarrangementviewcontroller/arrangement.md)
  A type that describes how an arrangement view controller lays out its view controllers.
- [struct UIOverlayArrangement](uioverlayarrangement-swift.struct.md)
  An arrangement that overlays views.
- [struct UISplitArrangement](uisplitarrangement-swift.struct.md)
  An arrangement that splits views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/updatearrangement(_:animated:))*