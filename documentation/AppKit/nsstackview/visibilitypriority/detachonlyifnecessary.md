# detachOnlyIfNecessary

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The Auto Layout priority that results in detachment of a view when there is insufficient space in the stack view to display it fully.

**Availability**:
- macOS 10.9+

## Declaration

```swift
static var detachOnlyIfNecessary: NSStackView.VisibilityPriority { get }
```

```c
static const NSStackViewVisibilityPriority NSStackViewVisibilityPriorityDetachOnlyIfNecessary;
```

## See Also

### Priorities
- [static var mustHold: NSStackView.VisibilityPriority](./musthold.md)
  The default value, and maximum Auto Layout priority, that results in a view never detaching from the stack view.
- [static var notVisible: NSStackView.VisibilityPriority](./notvisible.md)
  The minimum Auto Layout priority that forces a view to detach from the stack view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/visibilitypriority/detachonlyifnecessary)*