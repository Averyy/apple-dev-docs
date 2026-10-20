# stackView(_:willDetach:)

**Framework**: AppKit  
**Kind**: method

Called when the stack view is about to automatically detach one or more of its views.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
optional func stackView(_ stackView: NSStackView, willDetach views: [NSView])
```

#### Discussion

To configure a custom class to respond to the automatic detachment of views from a stack view’s view hierarchy, implement this method in the class. This method is not called when your code explicitly removes a view from a stack view’s [`views`](nsstackview/views.md) array.

## Parameters

- `stackView`: The stack view that is about to detach one or more of its views.
- `views`: An array of one or more views, managed by the stack view, that are about to be automatically detached.

## See Also

- [func stackView(NSStackView, didReattach: [NSView])](nsstackviewdelegate/stackview(_:didreattach:).md)
  Called when the stack view has automatically reattached one or more previously-detached views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackviewdelegate/stackview(_:willdetach:))*