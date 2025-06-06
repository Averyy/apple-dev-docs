# delegate

**Framework**: UIKit  
**Kind**: property

The delegate of the navigation controller object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UINavigationControllerDelegate)? { get set }
```

#### Discussion

You can use the navigation delegate to perform additional actions in response to changes in the navigation interface. For more information about implementing the delegate, see [`UINavigationControllerDelegate`](uinavigationcontrollerdelegate.md).

## See Also

- [protocol UINavigationControllerDelegate](uinavigationcontrollerdelegate.md)
  The interface for an object that serves as a navigation controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/delegate)*