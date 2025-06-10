# delegate

**Framework**: PaperKit  
**Kind**: property

The delegate for responding to user actions.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency weak var delegate: (any MarkupToolbarViewController.Delegate)? { get set }
```

#### Discussion

Observe `selectedIndirectPointerTouchMode` or `selectedDrawingTool` to watch for mode / tool changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller/delegate-swift.property)*