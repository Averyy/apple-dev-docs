# notVisible

**Framework**: AppKit  
**Kind**: property

The minimum Auto Layout priority that forces a view to detach from the stack view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
static let notVisible: NSStackView.VisibilityPriority
```

## See Also

- [static let detachOnlyIfNecessary: NSStackView.VisibilityPriority](nsstackview/visibilitypriority/detachonlyifnecessary.md)
  The Auto Layout priority that results in detachment of a view when there is insufficient space in the stack view to display it fully.
- [static let mustHold: NSStackView.VisibilityPriority](nsstackview/visibilitypriority/musthold.md)
  The default value, and maximum Auto Layout priority, that results in a view never detaching from the stack view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/visibilitypriority/notvisible)*