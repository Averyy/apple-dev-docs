# delegate

**Framework**: UIKit  
**Kind**: property

The delegate of the print-interaction controller.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIPrintInteractionControllerDelegate)? { get set }
```

#### Discussion

The delegate must adopt the [`UIPrintInteractionControllerDelegate`](uiprintinteractioncontrollerdelegate.md) protocol and implement one or more of its methods. It is not retained.

## See Also

- [protocol UIPrintInteractionControllerDelegate](uiprintinteractioncontrollerdelegate.md)
  An optional set of methods that the delegate of the shared print-interaction controller implements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/delegate)*