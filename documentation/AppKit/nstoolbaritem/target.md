# target

**Framework**: AppKit  
**Kind**: property

The object that defines the action method the toolbar item calls when clicked.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
weak var target: AnyObject? { get set }
```

#### Discussion

If you set this property to `nil`, the toolbar item attempts to execute its action method on the first responder. If the first responder doesn’t implement the action method, it forwards the request up the responder chain.

If you assign a custom view to the toolbar item, modifying this property updates the `target` property of the view, if one exists. If the item doesn’t contain a custom view, the toolbar item manages the target object directly.

## See Also

- [var action: Selector?](nstoolbaritem/action.md)
  The action method to call when someone clicks on the toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/target)*