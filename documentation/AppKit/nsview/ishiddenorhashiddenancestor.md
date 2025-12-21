# isHiddenOrHasHiddenAncestor

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view is hidden from sight because it, or one of its ancestors, is marked as hidden.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isHiddenOrHasHiddenAncestor: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the value of the [`isHidden`](nsview/ishidden.md) property is [`true`](https://developer.apple.com/documentation/Swift/true) for the current view or any of its ancestors in the view hierarchy. This property does not account for other reasons why a view might be considered hidden, such as being positioned outside its superview’s bounds, not having a window, or residing in a window that is offscreen or overlapped by another window.

## See Also

- [var isHidden: Bool](nsview/ishidden.md)
  A Boolean value indicating whether the view is hidden.
- [func viewDidHide()](nsview/viewdidhide.md)
  Invoked when the view is hidden, either directly, or in response to an ancestor being hidden.
- [func viewDidUnhide()](nsview/viewdidunhide.md)
  Invoked when the view is unhidden, either directly, or in response to an ancestor being unhidden


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/ishiddenorhashiddenancestor)*