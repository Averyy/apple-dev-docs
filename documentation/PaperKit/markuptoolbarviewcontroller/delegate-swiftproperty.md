# delegate

**Framework**: PaperKit  
**Kind**: property

The delegate for responding to user actions.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency weak var delegate: (any MarkupToolbarViewController.Delegate)? { get set }
```

#### Discussion

Observe `selectedIndirectPointerTouchMode` or `selectedDrawingTool` to watch for mode / tool changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller/delegate-swift.property)*