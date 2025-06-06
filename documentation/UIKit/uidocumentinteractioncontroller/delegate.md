# delegate

**Framework**: UIKit  
**Kind**: property

The delegate you want to receive document interaction notifications.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIDocumentInteractionControllerDelegate)? { get set }
```

#### Discussion

You can implement a delegate object to track user interactions with menu items displayed by the document interaction controller. For more information, see [`UIDocumentInteractionControllerDelegate`](uidocumentinteractioncontrollerdelegate.md).

The default value of this property is `nil`.

## See Also

- [protocol UIDocumentInteractionControllerDelegate](uidocumentinteractioncontrollerdelegate.md)
  A set of methods you can implement to respond to messages from a document interaction controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/delegate)*