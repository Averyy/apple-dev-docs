# view

**Framework**: AppKit  
**Kind**: property

The view that currently uses the writing tools coordinator.

**Availability**:
- macOS 15.2+

## Declaration

```swift
@MainActor
weak var view: NSView? { get }
```

#### Discussion

Use this property to refer to the view that currently owns the coordinator object. The system updates this property automatically when you assign the coordinator to the [`writingToolsCoordinator`](nsview/writingtoolscoordinator.md) property of your view. The value of this property is `nil` if there is no associated view.

## See Also

- [var delegate: (any NSWritingToolsCoordinator.Delegate)?](nswritingtoolscoordinator/delegate-swift.property.md)
  The object that handles Writing Tools interactions for your view.
- [NSWritingToolsCoordinator.Delegate](nswritingtoolscoordinator/delegate-swift.protocol.md)
  An interface that you use to manage interactions between Writing Tools and your custom text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/view)*