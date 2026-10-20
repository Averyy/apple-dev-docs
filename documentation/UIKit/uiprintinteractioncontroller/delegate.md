# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The delegate of the print-interaction controller.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UIPrintInteractionControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UIPrintInteractionControllerDelegate> delegate;
```

#### Discussion

The delegate must adopt the [`UIPrintInteractionControllerDelegate`](../uiprintinteractioncontrollerdelegate.md) protocol and implement one or more of its methods. It is not retained.

## See Also

### Assigning the delegate
- [protocol UIPrintInteractionControllerDelegate](../uiprintinteractioncontrollerdelegate.md)
  An optional set of methods that the delegate of the shared print-interaction controller implements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/delegate)*