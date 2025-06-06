# delegate

**Framework**: Safari Services  
**Kind**: property

An object that provides behavior for the Safari view controller’s Done and Action buttons.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
weak var delegate: (any SFSafariViewControllerDelegate)? { get set }
```

#### Discussion

Provide a [`SFSafariViewControllerDelegate`](sfsafariviewcontrollerdelegate.md) object to respond to the Done and Action buttons.

## See Also

- [protocol SFSafariViewControllerDelegate](sfsafariviewcontrollerdelegate.md)
  A protocol used to implement custom event handling for a Safari view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller/delegate)*