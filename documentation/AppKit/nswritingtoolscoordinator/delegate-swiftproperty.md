# delegate

**Framework**: AppKit  
**Kind**: property

The object that handles Writing Tools interactions for your view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
@MainActor
weak var delegate: (any NSWritingToolsCoordinator.Delegate)? { get }
```

#### Discussion

Specify this object at initialization time when creating your `NSWritingToolsCoordinator` object. The object must adopt the [`NSWritingToolsCoordinator.Delegate`](nswritingtoolscoordinator/delegate-swift.protocol.md) protocol, and be capable of modifying your view’s text storage and refreshing the view’s layout and appearance.

## See Also

- [NSWritingToolsCoordinator.Delegate](nswritingtoolscoordinator/delegate-swift.protocol.md)
  An interface that you use to manage interactions between Writing Tools and your custom text view.
- [var view: NSView?](nswritingtoolscoordinator/view.md)
  The view that currently uses the writing tools coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/delegate-swift.property)*