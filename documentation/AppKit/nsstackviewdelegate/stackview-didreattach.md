# stackView(_:didReattach:)

**Framework**: AppKit  
**Kind**: method

Called when the stack view has automatically reattached one or more previously-detached views.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
optional func stackView(_ stackView: NSStackView, didReattach views: [NSView])
```

#### Discussion

To configure a custom class to respond to the automatic reattachment of views to a stack view’s view hierarchy, implement this method in the class. This method is not called when your code explicitly adds a view to a stack view’s [`views`](nsstackview/views.md) array.

## Parameters

- `stackView`: The stack view that has reattached one or more detached views.
- `views`: An array of one or more views, managed by the stack view, that were reattached.

## See Also

- [func stackView(NSStackView, willDetach: [NSView])](nsstackviewdelegate/stackview(_:willdetach:).md)
  Called when the stack view is about to automatically detach one or more of its views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackviewdelegate/stackview(_:didreattach:))*