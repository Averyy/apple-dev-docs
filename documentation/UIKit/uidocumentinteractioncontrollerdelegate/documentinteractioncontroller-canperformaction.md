# documentInteractionController(_:canPerformAction:)

**Framework**: UIKit  
**Kind**: method

Called when a document interaction controller needs to know whether the specified action can be performed on the associated document.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
optional func documentInteractionController(_ controller: UIDocumentInteractionController, canPerformAction action: Selector?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the specified action is supported for the associated document or [`false`](https://developer.apple.com/documentation/Swift/false) if it is not. If you do not implement this method, the return value is assumed to be [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

When building the options menu (invoked, for example, by the user performing a long press gesture), a document interaction controller calls this method to find out if your app can perform various actions. If you implement this method for a given action, you must also implement the [`documentInteractionController(_:performAction:)`](uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:performaction:).md) method for that action.

The supported `action` selectors for this method are `copy:` and `print:`. (The `print:` selector is available in iOS 4.2 and later. Printing is supported only on devices that support multitasking.)

For each action that you implement in the [`documentInteractionController(_:performAction:)`](uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:performaction:).md) delegate method, return [`true`](https://developer.apple.com/documentation/Swift/true) from this method if that action is available for the document.

## Parameters

- `controller`: The document interaction controller managing an associated document.
- `action`: The selector representing the action in question.

## See Also

- [func documentInteractionController(UIDocumentInteractionController, performAction: Selector?) -> Bool](uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:performaction:).md)
  Called when a document interaction controller wants its delegate to perform a specified action with the associated document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:canperformaction:))*