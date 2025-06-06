# NSStackViewDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of methods you use to respond to a stack view detaching and reattaching views.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSStackViewDelegate : NSObjectProtocol
```

#### Overview

Adopt this protocol in a custom object and use it to track the addition and removal of views from the stack view’s view hierarchy. For an explanation of detachment and reattachment of a stack view’s views, see [`NSStackView`](nsstackview.md).

## Topics

### Responding to View Detachment and Reattachment
- [func stackView(NSStackView, didReattach: [NSView])](nsstackviewdelegate/stackview(_:didreattach:).md)
  Called when the stack view has automatically reattached one or more previously-detached views.
- [func stackView(NSStackView, willDetach: [NSView])](nsstackviewdelegate/stackview(_:willdetach:).md)
  Called when the stack view is about to automatically detach one or more of its views.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any NSStackViewDelegate)?](nsstackview/delegate.md)
  The delegate object for the stack view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackviewdelegate)*